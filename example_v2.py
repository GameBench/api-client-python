import os

from gamebench_api_client import Client
from gamebench_api_client.api.collections import list_collections, list_collection_sessions
from gamebench_api_client.api.sessions import get_session, get_session_fps_metric

client = Client(
    base_url=os.environ['GB_API_BASE_URL'],
    httpx_args={'auth': (os.environ['GB_API_EMAIL'], os.environ['GB_API_TOKEN'])},
)

company_id = os.environ['GB_COMPANY_ID']

with client as client:
    collections = list_collections.sync(client=client, company_id=company_id)
    print(f'Found {len(collections.collections)} collections')

    first_collection = collections.collections[0]
    page = list_collection_sessions.sync(
        collection_id=first_collection.id,
        client=client,
        page=0,
        page_size=10,
    )
    print(f'Collection "{first_collection.name}" has {page.total_hits} sessions')

    if page.results:
        # The spec leaves PageResultsItem (and most metric responses) untyped,
        # so fields live in `.additional_properties` rather than as attributes.
        session_id = page.results[0].additional_properties['id']
        session = get_session.sync(session_id=session_id, client=client)
        print(f'Session {session_id} → {session.url}')

        fps = get_session_fps_metric.sync(session_id=session_id, client=client)
        if fps:
            print(f'FPS metric keys: {list(fps.additional_properties.keys())}')

    # `sync_detailed` exposes status_code and the raw response.
    detailed = get_session.sync_detailed(session_id='does-not-exist', client=client)
    print(f'Lookup of bogus id returned HTTP {detailed.status_code}')

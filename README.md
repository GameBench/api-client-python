```
python3 -m venv env
. env/bin/activate

pip install -r requirements.txt

export GB_API_BASE_URL=
export GB_API_EMAIL=
export GB_API_TOKEN=
export GB_COMPANY_ID=

python example.py
```

## Which client to use

This repo ships two API clients side by side:

- **`client.py`** — the hand-written client. Covers a mix of v1 and v2
  endpoints, plus undocumented v1 routes like `listApps`, `listAppTags`,
  `getUploadStatus`, and the soft `deleteSession`. The existing scripts in
  this repo all use it.
- **`gamebench-api-client/`** — a generated typed client produced from the
  dashboard's OpenAPI spec. Covers the v2 sessions surface plus the
  documented v1 routes (`/v1/collections`, `/v1/users/me`).

**Convention:** new code should reach for the generated client when the
endpoint it needs is in the spec. Fall back to `client.py` only for the
undocumented v1 endpoints, or for legacy scripts that already use it.

### Using the generated client

Install it into your venv from this repo (it isn't on PyPI yet):

```
./env/bin/pip install -e ./gamebench-api-client
```

The generated `AuthenticatedClient` defaults to `Authorization: Bearer`,
but the GameBench API uses HTTP Basic. Use the base `Client` with httpx
auth instead:

```python
from gamebench_api_client import Client
from gamebench_api_client.api.sessions import get_session
import os

client = Client(
    base_url=os.environ["GB_API_BASE_URL"],
    httpx_args={"auth": (os.environ["GB_API_EMAIL"], os.environ["GB_API_TOKEN"])},
)

session = get_session.sync(session_id="...", client=client)
```

See [example_v2.py](example_v2.py) for a runnable walkthrough.

Note: some response shapes (e.g. `PageResultsItem`, most metric responses)
are not yet defined in the spec, so the generated models expose them via
`additional_properties` rather than typed attributes.

### Regenerating the client

When the dashboard's spec changes, regenerate from the published spec:

```
./env/bin/pip install openapi-python-client
./env/bin/openapi-python-client generate \
    --overwrite \
    --config openapi-python-client.yaml \
    --url https://web.gamebench.net/v1/openapi.yaml
```

The generator is a dev tool and is not in `requirements.txt`.

## Clearing up old session data

```
python3 -m venv env
. env/bin/activate

pip install requests click python-dateutil

# Set to the value of your API token, or you will be prompted upon running the command
export GB_API_TOKEN=

python delete-old-sessions.py --company-id <company id> --api-email <API email>

Use python `delete-old-sessions.py --help` for usage instructions such as filtering by app package name
```

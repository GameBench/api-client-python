from client import ApiClient
import click
from dateutil.relativedelta import relativedelta
from datetime import datetime
import os
from requests.exceptions import HTTPError

def get_api_token(ctx, param, value):
    if value:
        return value
    env_token = os.environ.get('GB_API_TOKEN')
    if env_token:
        return env_token
    # Only prompt if not provided and not in env
    return click.prompt("API token", hide_input=True)

@click.command()
@click.option('--api-base-url', type=str, default=os.environ.get('GB_API_BASE_URL', 'https://web.gamebench.net'), required=True)
@click.option('--company-id', type=str, default=os.environ.get('GB_COMPANY_ID'), required=True)
@click.option('--api-email', type=str, default=os.environ.get('GB_API_EMAIL'), required=True)
@click.option('--api-token', callback=get_api_token, required=False)
@click.option('--months', '-m', type=int, default=24)
@click.option('--app-package-name', '-a', type=str, default=(), multiple=True)
@click.option('--dry-run', is_flag=True)
@click.option('--force', '-f', is_flag=True)
def delete_old_sessions(api_base_url, company_id, api_email, api_token, months=24, app_package_name=None, dry_run=False, force=False):
    """
    Delete old sessions.

    Please note session deletion is irreversible. It's also asynchronous so there may be a delay before the session is actually deleted.
    """
    client = ApiClient(api_base_url=api_base_url, company_id=company_id, auth=(api_email, api_token))

    x_months_ago = datetime.now() + relativedelta(months=-months)

    # print(x_months_ago.isoformat())

    filters = {
        'timePushedEnd': int(x_months_ago.timestamp() * 1000),
    }

    if app_package_name:
        filters['appPackageName'] = app_package_name

    result = client.listSessions(filters=filters)

    print('Found {} sessions older than {} matching {}'.format(result['totalHits'], x_months_ago.isoformat(), filters))

    if dry_run or result['totalHits'] == 0:
        return

    if not force and not click.confirm('Do you want to continue? {} sessions will be *permanently* deleted'.format(result['totalHits'])):
        print('Aborting')
        return

    session_ids = []

    page = 0

    while page <= result['totalPages']:
        result = client.listSessions(filters=filters, page=page)

        for session in result['results']:
            session_ids.append(session['id'])

        page += 1

    for session_id in session_ids:
        print('Deleting session {}'.format(session_id))
        try:
            client.permanentlyDeleteSession(session_id)
        except HTTPError as e:
            if e.response.status_code == 404:
                print('Session {} not found'.format(session_id))
                continue
            raise e

if __name__ == '__main__':
    delete_old_sessions()

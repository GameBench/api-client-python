from client import ApiClient
import os
import sys
from pathlib import Path

session_dir = os.path.join("tmp", "sessions")

Path(session_dir).mkdir(parents=True, exist_ok=True)

required_env_vars = [
    'SRC_GB_API_BASE_URL',
    'SRC_GB_COMPANY_ID',
    'SRC_GB_API_EMAIL',
    'SRC_GB_API_TOKEN',
    'SRC_GB_APP_PACKAGE_NAME',
    'DEST_GB_API_BASE_URL',
    'DEST_GB_COMPANY_ID',
    'DEST_GB_API_EMAIL',
    'DEST_GB_API_TOKEN',
]

for required_env_var in required_env_vars:
    value = os.environ.get(required_env_var)
    if value == None or value == '':
        print('{} environment variable must be set'.format(required_env_var))
        sys.exit(1)

src_client = ApiClient(os.environ.get('SRC_GB_API_BASE_URL'), os.environ.get('SRC_GB_COMPANY_ID'), (os.environ.get('SRC_GB_API_EMAIL'), os.environ.get('SRC_GB_API_TOKEN')))
dest_client = ApiClient(os.environ.get('DEST_GB_API_BASE_URL'), os.environ.get('DEST_GB_COMPANY_ID'), (os.environ.get('DEST_GB_API_EMAIL'), os.environ.get('DEST_GB_API_TOKEN')))

filters = {
    'appPackageName': [os.environ.get('SRC_GB_APP_PACKAGE_NAME')],
}

page = 0

while True:
    result = src_client.listSessions(page, filters)
    print(result['page'], result['totalPages'], len(result['results']))

    for session in result['results']:
        session_zip_path = Path(os.path.join(session_dir, session['id'] + '.zip'))
        print(session['id'], session_zip_path)
        if not session_zip_path.is_file():
            src_client.exportSession(session['id'], session_zip_path)

        dest_client.uploadSession(session_zip_path)

    page = page + 1
    if page == result['totalPages']:
        break

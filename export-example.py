from client import ApiClient
import os
import sys

if len(sys.argv) != 2:
    print('Please provide session ID as first argument')
    sys.exit(1)

session_id = sys.argv[1]

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

session = client.getSession(session_id)
client.exportSession(session_id, 'session_%s.zip' % session_id)

client.downloadSessionCsv(session_id, 'session_%s.csv' % session_id)

from client import ApiClient
import os
import sys

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

session_id = sys.argv[1]

frametimes = client.getSessionFrametimes(session_id)

print(frametimes)

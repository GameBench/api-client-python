from client import ApiClient
import os

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')), os.environ.get('GB_COMPANY_ID'))

session = client.getSession('fb16412b-a174-4c9a-acb3-8e5e728ed3e3')
client.exportSession('fb16412b-a174-4c9a-acb3-8e5e728ed3e3', 'session.zip')

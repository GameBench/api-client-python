from client import ApiClient
import os

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

sessions = client.listSessions()

session = client.getSession('84759304-3add-47f9-b0bc-7461aff9cb8a')

additionalFiles = client.listSessionAdditionalFiles('84759304-3add-47f9-b0bc-7461aff9cb8a')

for additionalFile in additionalFiles['additionalFiles']:
    print(additionalFile['filename'])
    additionalFileContents = client.getSessionAdditionalFileContents('84759304-3add-47f9-b0bc-7461aff9cb8a', additionalFile['filename'])
    print(additionalFileContents)
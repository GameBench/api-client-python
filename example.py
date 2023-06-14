from client import ApiClient
import os

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

# filters = {
#     'userEmail': ['example@gamebench.net'],
#     'tags': [
#         'foo:bar'
#     ],
#     'durationStart': 0,
#     'durationEnd': 0,
#     'title': '',
#     'notes': '',
#     'dateStart': 0,
#     'dateEnd': 0,
#     'timePushedStart': 0,
#     'timePushedEnd': 0,
#     'projects': ['project id', 'project id'],
#     'deviceModels': ['device model 1', 'device model 2'],
#     'deviceManufacturers': [],
#     'imported': True,
#     'appName': [],
#     'appPackageName': [],
#     'appVersion': [],
# }

filters = {}
page = 0

sessions = client.listSessions(page, filters)

session = client.getSession('84759304-3add-47f9-b0bc-7461aff9cb8a')

additionalFiles = client.listSessionAdditionalFiles('84759304-3add-47f9-b0bc-7461aff9cb8a')

for additionalFile in additionalFiles['additionalFiles']:
    print(additionalFile['filename'])
    additionalFileContents = client.getSessionAdditionalFileContents('84759304-3add-47f9-b0bc-7461aff9cb8a', additionalFile['filename'])
    print(additionalFileContents)

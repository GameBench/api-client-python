from client import ApiClient
import os

pro_net_ids = {}

def process(session):
  if 'proNet' not in session['tags']:
    return

  pro_net_id = session['tags']['proNet']

  if pro_net_id in pro_net_ids:
    pro_net_ids[pro_net_id].append(session['id'])
  else:
    pro_net_ids[pro_net_id] = [session['id']]

def populate_pro_net_ids_by_company(company_id):
  print('Fetching sessions for', company_id)
  client = ApiClient(os.environ.get('GB_API_BASE_URL'), company_id, (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

  filters = {
  }

  page = 0

  while True:
      result = client.listSessions(page, filters)

      for session in result['results']:
          process(session)

      page = page + 1

      if page >= result['totalPages']:
          break

  # print(pro_net_ids)

populate_pro_net_ids_by_company(os.environ.get('GB_COMPANY_ID_1'))
populate_pro_net_ids_by_company(os.environ.get('GB_COMPANY_ID_2'))

for key, value in pro_net_ids.items():
  print(key, *["https://web.gamebench.net/dashboard/global/sessions/" + v + "/Summary" for v in value])

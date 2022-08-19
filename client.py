import requests

class ApiClient:
    def __init__(self, api_base_url, company_id, auth):
       self.api_base_url = api_base_url
       self.company_id = company_id
       self.auth = auth

    def listSessions(self, page = 0):
        url = self.api_base_url + '/v1/sessions?company=' + self.company_id + '&page=' + str(page)
        r = requests.get(url, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def getSession(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def listSessionAdditionalFiles(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/additional-files?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def getSessionAdditionalFileContents(self, session_id, file_name):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/additional-files/' + file_name + '?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.text

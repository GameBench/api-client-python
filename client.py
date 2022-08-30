import requests

class ApiClient:
    def __init__(self, api_base_url, company_id, auth):
       self.api_base_url = api_base_url
       self.company_id = company_id
       self.auth = auth

    def listSessions(self, page = 0, filters = {}):
        url = self.api_base_url + '/v1/advanced-search/sessions?company=' + self.company_id + '&page=' + str(page)
        r = requests.post(url, auth=self.auth, json={'sessionInfo': filters})
        r.raise_for_status()
        sessions_result = r.json()['sessionPage']
        return {
            'results': sessions_result['records'],
            'page': sessions_result['number'],
            'size': sessions_result['size'],
            'totalPages': sessions_result['totalPages'],
            'totalHits': sessions_result['totalRecords'],
        }

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

    def getSessionLatencyResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/latency?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def getSessionFpsResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/fps?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()        

    def getSessionNetworkRttResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/network-rtt?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json() 
        
    def getSessionNetworkRttJitterResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/network-rtt-jitter?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def getSessionNetworkResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/network?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

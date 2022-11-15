import requests
import logging
import shutil

class ApiClient:
    def __init__(self, api_base_url, company_id, auth, debug = False):
       self.api_base_url = api_base_url
       self.company_id = company_id
       self.auth = auth

       if debug:
           try:
               from http.client import HTTPConnection
           except ImportError:
               from httplib import HTTPConnection

           HTTPConnection.debuglevel = 1
           logging.basicConfig()
           logging.getLogger().setLevel(logging.DEBUG)
           requests_log = logging.getLogger("urllib3")
           requests_log.setLevel(logging.DEBUG)
           requests_log.propagate = True

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

    def deleteSession(self, session_id):
        r = requests.delete(self.api_base_url + '/v1/sessions/' + session_id + '?company=' + self.company_id, auth=self.auth)
        return r.ok

    def getSession(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def setSessionAsShared(self, session_id):
        r = requests.post(self.api_base_url + '/v1/sessions/' + session_id + '/share?company=' + self.company_id, auth=self.auth)
        return r.ok

    def listSessionAdditionalFiles(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/additional-files?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def getSessionAdditionalFileContents(self, session_id, file_name):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/additional-files/' + file_name + '?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.content

    def getSessionBatteryResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/battery?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

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

    def exportSession(self, session_id, dest):
        with requests.get(self.api_base_url + '/v1/sessions/export/sessions/' + session_id + '?company=' + self.company_id, auth=self.auth, stream=True) as r:
            with open(dest, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

    def downloadSessionCsv(self, session_id, dest):
        with requests.get(self.api_base_url + '/v1/sessions/' + session_id + '/export/csv?company=' + self.company_id, auth=self.auth, stream=True) as r:
            with open(dest, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

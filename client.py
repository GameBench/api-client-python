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
        req_body = {'sessionInfo': {}, 'appInfo': {}}

        if 'userEmail' in filters:
            req_body['sessionInfo']['userEmail'] = filters['userEmail']

        if 'tags' in filters:
            req_body['sessionInfo']['tags'] = filters['tags']

        if 'durationStart' in filters:
            req_body['sessionInfo']['durationStart'] = filters['durationStart']

        if 'durationEnd' in filters:
            req_body['sessionInfo']['durationEnd'] = filters['durationEnd']

        if 'title' in filters:
            req_body['sessionInfo']['title'] = filters['title']

        if 'notes' in filters:
            req_body['sessionInfo']['notes'] = filters['notes']

        if 'dateStart' in filters:
            req_body['sessionInfo']['dateStart'] = filters['dateStart']

        if 'dateEnd' in filters:
            req_body['sessionInfo']['dateEnd'] = filters['dateEnd']

        if 'timePushedStart' in filters:
            req_body['sessionInfo']['timePushedStart'] = filters['timePushedStart']

        if 'timePushedEnd' in filters:
            req_body['sessionInfo']['timePushedEnd'] = filters['timePushedEnd']

        if 'projects' in filters:
            req_body['projects'] = filters['projects']

        if 'deviceModels' in filters:
            req_body['devices'] = filters['deviceModels']

        if 'deviceManufacturers' in filters:
            req_body['manufacturers'] = filters['deviceManufacturers']

        if 'imported' in filters:
            req_body['imported'] = filters['imported']

        if 'appName' in filters:
            req_body['appInfo']['name'] = filters['appName']

        if 'appPackageName' in filters:
            req_body['appInfo']['package'] = filters['appPackageName']

        if 'appVersion' in filters:
            req_body['appInfo']['version'] = filters['appVersion']

        r = requests.post(url, auth=self.auth, json=req_body)
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
    
    def getSessionCpuResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' +
                         session_id + '/cpu?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def getSessionGpuResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id +
                         '/gpu/other?company=' + self.company_id, auth=self.auth)
        r.raise_for_status()
        return r.json()

    def getSessionInstPowerResults(self, session_id):
        r = requests.get(self.api_base_url + '/v1/sessions/' + session_id +
                         '/power?company=' + self.company_id, auth=self.auth)
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

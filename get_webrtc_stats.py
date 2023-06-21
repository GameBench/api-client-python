# Python sample code for extracting WebRTC stats from the most recent session for a given app package
#
# Example command:
#
#    python get_webrtc_stats.py net.gamebench.webrtcdemo | jq
#

from client import ApiClient
import sys,json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

# Package ID must be on the command line
if len(sys.argv)<2 :
    print('Error: no package id')
    exit(-1)

# Get the most recent session for the given app package
client = ApiClient() 
sessions = client.listSessions(0, {'appPackageName':[sys.argv[1]]})
session = sessions['results'][0]

# Extract the sessions WebRTC stats data
data = client.getSessionAdditionalFileContents(session['id'], 'WebRTCStats.json').decode("utf-8") 

# Print it out but as a properly-formatted JSON array
print('[')
first = True
while (len(data)):
    res = json.JSONDecoder().raw_decode(data)
    if first: first=False 
    else: print(',')
    print(data[:res[1]])
    data = data[res[1]:]
print(']')
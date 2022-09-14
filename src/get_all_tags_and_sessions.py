import os
import json
from tqdm import tqdm
from client import ApiClient
from datetime import datetime

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

# Convert Unix to datetime object on Windows
def unix_to_datetime(x):   
    try:
        date = datetime.fromtimestamp(int(x)/1000).strftime('%Y-%m-%d')
    except:
        date = x
    return date

filters = {}

# Initial API call starts at Page 0 to get the 
# total pages required
page = 0
sessions = client.listSessions(page, filters)

print(f"Total sessions to process: {sessions['totalHits']}")
print(f"Total pages to process: {sessions['totalPages']}")

# Get all sessions and extract all possible tags
all_sessions = {}
all_tags = {}

for page in tqdm(range(0, sessions["totalPages"])):
    sessions = client.listSessions(page, filters)
    for session in sessions["results"]:
        
        for tag in session["tags"].items():
            if tag[0] not in all_tags.keys():
                all_tags[tag[0]] = [tag[1]]
            elif tag[1] not in all_tags[tag[0]]:
                all_tags[tag[0]].append(tag[1])
            else:
                pass
        all_sessions[session["id"]] = session

with open("all_tags.json", "w") as outfile:
    json.dump(all_tags, outfile)

with open("all_sessions.json", "w") as outfile:
    json.dump(all_sessions, outfile)

json_all_sessions = json.dumps(all_sessions, indent = 4) 
json_all_tags = json.dumps(all_tags, indent = 4)
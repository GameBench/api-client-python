from client import ApiClient
import os
from datetime import datetime, timedelta
from glob import glob
import sys

def process(session):
    additionalFiles = client.listSessionAdditionalFiles(session['id'])

    if not additionalFiles['additionalFiles']:
        return

    for additionalFile in additionalFiles['additionalFiles']:
        if additionalFile['filename'] == 'WebRTCStats.csv':
            print(session['id'], session['sessionDateTimestamp'])
            # print(additionalFile['filename'])
            additionalFileContents = client.getSessionAdditionalFileContents(session['id'], additionalFile['filename'])
            # print(additionalFileContents)

            sessionDateTimestamp = datetime.strptime(session['sessionDateTimestamp'].replace('Z', '+0000'), '%Y-%m-%dT%H:%M:%S.%f%z')
            # print(sessionDateTimestamp)

            if splitByDay:
                filename = sessionDateTimestamp.strftime('sessions_%Y_%m_%d.csv')
                # print(filename)

                decoded = additionalFileContents.decode(encoding='utf-8')

                if decoded.startswith('timestamp,'):
                    decoded = decoded.split('\n', 1)[1]

                if not os.path.isfile(filename):
                    with open(filename, 'w') as fh:
                        fh.write('timestamp,framesPerSecond,bytesReceived,packetsReceived,packetsLost,framesDecoded,framesDropped,totalDecodeTime,totalProcessingDelay,jitter,currentRoundTripTime\n')

                with open(filename, 'a') as fh:
                   fh.write(session['id'] + '\n')
                   fh.write(decoded)
            else:
                filename = sessionDateTimestamp.strftime('sessions.csv')

                decoded = additionalFileContents.decode(encoding='utf-8')

                if decoded.startswith('timestamp,'):
                    decoded = decoded.split('\n', 1)[1]

                if not os.path.isfile(filename):
                    with open(filename, 'w') as fh:
                        fh.write('timestamp,framesPerSecond,bytesReceived,packetsReceived,packetsLost,framesDecoded,framesDropped,totalDecodeTime,totalProcessingDelay,jitter,currentRoundTripTime\n')

                with open(filename, 'a') as fh:
                   fh.write(session['id'] + '\n')
                   fh.write(decoded)

client = ApiClient(os.environ.get('GB_API_BASE_URL'), os.environ.get('GB_COMPANY_ID'), (os.environ.get('GB_API_EMAIL'), os.environ.get('GB_API_TOKEN')))

splitByDay = len(sys.argv) == 2 and sys.argv[1] == '1'

pathnames = glob('*.csv')

for pathname in pathnames:
    print('Removing %s' % pathname)
    os.remove(pathname)

dateStart = datetime.utcnow() - timedelta(days=7)
dateEnd = datetime.utcnow()

print('Finding sessions between %s and %s' % (dateStart, dateEnd))

filters = {
    'dateStart': round(dateStart.timestamp() * 1000),
    'dateEnd': round(dateEnd.timestamp() * 1000),
}

page = 0

while True:
    result = client.listSessions(page, filters)

    for session in result['results']:
        process(session)

    page = page + 1

    if page >= result['totalPages']:
        break

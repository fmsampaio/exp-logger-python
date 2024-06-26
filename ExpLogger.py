import json
import requests

from LogEntry import LogEntry

BASE_API_URL = 'https://exp-logger-api-5bed46122227.herokuapp.com'

def logEntry(logEntry):
    jsonData = logEntry.toJson()

    response = requests.post(
        url = f'{BASE_API_URL}/log_entries/',
        data = jsonData
    )

    return response.status_code == 201

def log(projectId, experimentName, logMessage, logDetails=""):
    entry = LogEntry(
        projectId=projectId,
        experimentName=experimentName,
        logMessage=logMessage,
        logDetails=logDetails
    )
    logEntry(entry)



if __name__ == '__main__':
    success = log(
        projectId = 2,
        experimentName= "RA_Video_22_NDP",
        logMessage="Starting execution [2]"
    )

    if success:
        print('Logged!')
    else:
        print('Error! Not logged.')

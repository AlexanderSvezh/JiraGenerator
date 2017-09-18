import requests
import json

login=<login>'
password=<pass>
auth=(login,password)

url='https://jira.lpr.jet.msk.su/rest/api/2/issue/LOAD-36/worklog'
headers={'Content-Type': 'application/json'}

set_data=json.dumps(
    {
      "comment": "I did some work here.",
      "started": "2017-09-06T00:00:12.707+0000",
      "timeSpent": "1h"
    })
print(url)
# print(set_data)
print(auth)
print(headers)
r = requests.post(url, auth=auth, data=set_data, headers=headers)
print(r.status_code)

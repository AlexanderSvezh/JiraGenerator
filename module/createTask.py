import requests
import json

login=<login>
password=<pass>
auth=(login,password)

url='https://jira.lpr.jet.msk.su/rest/api/2/issue/'
headers={'Content-Type': 'application/json'}

def getrequest(task):
    r = requests.get(url+task, auth=auth)
    print('get',r.status_code)
    rr=r.json()['fields']
    return(rr)

def putrequest(task,data):
    r = requests.put(url+task, auth=auth, headers=headers, data=data)
    print('put',r.status_code)

# form=json.dumps(rr, indent=4, sort_keys=4)
# print(form)

def create_subtask():
    project_name='LOAD'
    parent_name='LOAD-35'
    title_task='Sub-task (REST API JIRA)'
    descript='test for REST'
    data_create=json.dumps({
        "fields":
        {
            "project":
            {
                "key": project_name
            },
            "parent":
            {
                "key": parent_name
            },
            "summary": title_task,
            "description": descript,
            "priority":
                {
                    "name":"Enhancement"
                },
            "customfield_12300":[
            {
                "name":"aa.svezhentsev"
            },
            {
                "name":"ds.drepina"
            }],
            "components":[
            {
                "name": "PDP"
            }],
            "assignee":
            {
                "name": "aa.svezhentsev"
            },
            "issuetype":
            {
                "id": "5"
            }
        }
    })
    print(data_create)
    r=requests.post(url, auth=auth, headers=headers, data=data_create)
    print(r.json()['key'])

def new_task():
    project_name='LOAD'
    title_task='New task of LOAD'
    descript='test'
    istype_name='Task'
    data_new=json.dumps({
        "fields": {
           "project":
           {
              "key": project_name
           },
           "summary": title_task,
           "description": descript,
           "issuetype": {
              "name": istype_name
           }
        }
    })
    print(data_new)
    requests.post(url, auth=auth, headers=headers, data=data_new)

def set_estimate():
    orig="2h"
    remain="3h 30m"
    task='LOAD-36'
    set_data=json.dumps({
       "fields": {
            "timetracking":
            {
               "originalEstimate": orig,
               "remainingEstimate": remain,
            }
        }
    })
    putrequest(task,set_data)

def add_worklogs():
    task='LOAD-36'
    text_comment='test comment 3.'
    start_data='2017-09-06'
    spenttime="10"
    work_data=json.dumps(
    {
      "comment": text_comment,
      "started": start_data+'T00:00:00.000+0000',
      "timeSpent": spenttime+"m"
    })
    workurl=url+task+'/worklog'
    r=requests.post(workurl, auth=auth, data=work_data, headers=headers)
    print(r.json()['self'])

# create_subtask()
# new_task()
# set_estimate()
# add_worklogs()

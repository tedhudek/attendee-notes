# Quick & dirty Python script to parse the schedule JSON and auto-create
# directories in the proper structure with READMEs containing abstracts.

import json
import os
import pprint as pp

schedule_json = open('schedule.json', 'r').read()
schedule = json.loads(schedule_json)
sessions = schedule.get('sessions')

for session in sessions:
    day = session.get('day')
    if not os.path.exists(day):
        os.makedirs(day)
    talks = session.get('sessions') # namespaces :(
    for talk in talks:
        time = talk.get('start_time')
        title = talk.get('title')
        dir_name = time + ' ' + title
        if not os.path.exists(day + '/' + dir_name):
            os.makedirs(day + '/' + dir_name)
        f = open(day + '/' + dir_name + '/README.md', 'w+')
        abstract = talk.get('abstract', 'No abstract!')
        f.write(abstract.encode('ascii', 'ignore'))
        f.close()

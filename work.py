from jira import JIRA
import os
import sys
from Developer import Developer
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf8')

iterationCode = input("Please input iteration version: ")
credentials = (os.environ['JIRA_USERNAME'], os.environ['JIRA_PASSWORD'])
jqlQuery = 'project="NEO - Neo project" and Sprint = "'+str(iterationCode)+'" and Sprint not in futureSprints()'

options = {
    'server': os.environ['JIRA_ENDPOINT'],
    'verify': False,
}

jira = JIRA(options=options, basic_auth=credentials)
tasks = jira.search_issues(jqlQuery)

developers = {}

for task in tasks:
    issue = jira.issue(task)

    if "Deployment Ticket of Iteration "+str(iterationCode) in issue.fields.summary:
        continue

    workLogs = jira.worklogs(issue.key)

    for workLog in workLogs:
        if not workLog.updateAuthor.active:
            continue

        updateAuthor = workLog.updateAuthor.name

        if not developers.get(updateAuthor):
            developers[updateAuthor] = Developer(updateAuthor)

        developers[updateAuthor].add_ticket(issue)
        developers[updateAuthor].add_work(workLog)


for name, developer in developers.items():
        print(developer)

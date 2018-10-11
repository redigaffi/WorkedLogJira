from jira import JIRA
import sys
from Developer import Developer
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf8')

iterationCode = input("Please input iteration version: ")
credentials = ('username', 'password')
jqlQuery = 'project="NEO - Neo project" and Sprint = "'+str(iterationCode)+'" and Sprint not in futureSprints()'

options = {
    'server': 'https://tracker.site.com:8550/',
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

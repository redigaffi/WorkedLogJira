from jira import JIRA
import timestring
import datetime
import sys
from issueSummary import issueSummary

reload(sys)
sys.setdefaultencoding('utf8')

userKey = 'user'
credentials = (userKey, 'password')
jqlQuery = 'project="NEO - Neo project" AND updatedDate >= startOfDay() AND updatedDate < endOfDay()'

options = {
    'server': 'https://tracker.vendoservices.com:8550/'
}

# Instantiate Jira library
jira = JIRA(options=options, basic_auth=credentials)
tasks = jira.search_issues(jqlQuery)

# Collection of logged works
myWorkLogged = {}
todayDateObj = timestring.Date(datetime.datetime.today())
todayDate = str(todayDateObj.year)+"-"+str(todayDateObj.month)+"-"+str(todayDateObj.day)

for task in tasks:
    issue = jira.issue(task)
    workLogs = jira.worklogs(issue.key)

    # Iterate over worklogs for each task
    for workLog in workLogs:

        workCreatedTimeObj = timestring.Date(workLog.created)
        workCreatedTime = str(workCreatedTimeObj.year) + "-" + str(workCreatedTimeObj.month) + "-" + str(workCreatedTimeObj.day)

        if not workCreatedTime == todayDate:
            continue

        workLogUserKey = jira.search_users(workLog.updateAuthor.name, maxResults=1)[0]

        if workLogUserKey.key == userKey:

            if issue.key not in myWorkLogged:
                myWorkLogged[issue.key] = []

            myWorkLogged[issue.key].append(workLog)

issueSummaries = []
for issue, loggedTimes in myWorkLogged.items():
    issueSummaryTmp = issueSummary(issue, jira.issue(issue).fields.summary)

    for loggedTime in loggedTimes:
        issueSummaryTmp.addSeconds(loggedTime.timeSpentSeconds)

        issueSummaryTmp.timeToString()
    issueSummaries.append(issueSummaryTmp)


# Print issue summary in a human way
for issueSummary in issueSummaries:
    print issueSummary








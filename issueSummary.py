# Class that contain issue, description and logged work.
class issueSummary:
    def __init__(self, issueCode, issueDescription):
        self.issueCode = issueCode
        self.issueDescription = issueDescription
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def addSeconds(self, seconds):
        self.seconds += seconds


    def getSeconds(self):
        return self.seconds


    def timeToString(self):
        self.minutes = self.seconds/60
        self.hours = self.minutes/60
        self.minutes = self.minutes-(self.hours*60)


    def __str__(self):
        resultString = self.issueCode + " - " + self.issueDescription + " ("

        if self.hours > 0:
            resultString += str(self.hours)+"h "

        if self.minutes > 0:
            resultString += str(self.minutes)+"m"

        resultString += ")"

        return resultString


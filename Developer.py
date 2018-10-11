class Developer:
    def __init__(self, developerName):
        self.developerName = developerName
        self.tickets = {}
        self.workedLog = {}


    def add_ticket(self, ticket):
        if not self.tickets.get(ticket.key) and ticket.fields.timeoriginalestimate is not None and ticket.fields.timeoriginalestimate > 0:
            self.tickets[ticket.key] = ticket

    def add_work(self, worklog):
        if not self.workedLog.get(worklog.id) and worklog.updateAuthor.name == self.developerName:
            self.workedLog[worklog.id] = worklog

    def __str__(self):
        ticket_count = 0
        total_original_estimations = 0
        total_working_hours = 0

        ticketList = ""
        for ticketCode, issue in self.tickets.items():
            ticketList += "\n"+ticketCode
            ticket_count += 1
            total_original_estimations += float(issue.fields.timeoriginalestimate)


        for workedLogId, worklog in self.workedLog.items():
            total_working_hours += float(worklog.timeSpentSeconds)

        total_original_estimations /= 3600
        total_working_hours /= 3600

        return "Developer: " + self.developerName + "\nTicket Amount: " + str(ticket_count) + "\nOriginal Estimates: " + str(total_original_estimations) + "h\nLogged Hours: " + str(total_working_hours)+ "h" + "\nFocus Factor: "+ str((total_original_estimations/total_working_hours)*100) + "%\nTickets: "+ticketList+"\n"
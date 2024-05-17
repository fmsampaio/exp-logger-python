class LogEntry:
    def __init__(self, projectId, experimentName, logMessage, logDetails=""):
        self.projectId = projectId
        self.experimentName = experimentName
        self.logMessage = logMessage
        self.logDetails = logDetails
    
    def toJson(self):
        returnable = {
            'project_id' : self.projectId,
            'experiment_name' : self.experimentName,
            'log_message' : self.logMessage,
            'log_details' : self.logDetails
        }
        return returnable
    

if __name__ == '__main__':
    entry = LogEntry(
        projectId = 1,
        experimentName= "RA_Video_22_NDP",
        logMessage="Starting execution"
    )
    print(entry.toJson())
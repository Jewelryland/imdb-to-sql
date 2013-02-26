import os
from datetime import datetime

class Log:
    def __init__(self):
        root_dir = "log"
        if not os.path.exists(root_dir):
        
            os.makedirs(root_dir)

        now = datetime.now()
        filename = "%s/%s.log" % (root_dir, now.strftime("%y-%m-%d-%H-%M-%S"))
        self.log_file = open(filename, "w")
        
        
    def info(self, log_message):
        self.log_file.write("%s %s %s\n" %(datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3], "INFO", log_message))

        
    def warning(self, log_message):
        self.log_file.write("%s %s %s\n" %(datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3], "WARNING", log_message))

        
    def error(self, log_message):
        self.log_file.write("%s %s %s\n" %(datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")[:-3], "ERROR", log_message))


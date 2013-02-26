from log import Log

logger = Log()
logger.info("Test")


import os
command = "gzip -cd %s > %s" % ("alternate-versions.list.gz", "alternate-versions.list")
ret = os.system(command)
if ret:
    logger.error("Error in extraction;alternate-versions.list.gz")
else:
    logger.info("alternate-versions.list.gz extraction success")
    print "Error in extraction"


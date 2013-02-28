from log import Log

from movie_list import MovieList

logger = Log()
logger.info("Logger Initialized")
#
#
#import os
#command = "gzip -cd %s > %s" % ("alternate-versions.list.gz", "alternate-versions.list")
#ret = os.system(command)
#if ret:
#    logger.error("Error in extraction;alternate-versions.list.gz")
#else:
#    logger.info("alternate-versions.list.gz extraction success")
#    print "Error in extraction"



ml = MovieList(logger)
import os
import re

import Queue
import threading

from mysql import MySQL

class MovieList:
    def __init__(self, logger):
        database_name = "reelphil"
        
        self.logger = logger
        self.movie = open("movies.txt", "w")
        self.series = open("series.txt", "w")
        self.sql = MySQL(database_name)
        self.start()
        
    def start(self):
        original_filename = "movies.list.gz"
        extract_filename = "movies.list"
        command = "gzip -cd %s > %s" % (original_filename, extract_filename)
        #ret = os.system(command)
        #if ret:
        #    self.logger.error("Error in extraction of %s" % original_filename)
        #    return
        #else:
        #    self.logger.info("%s extraction success" % original_filename)
            
        
        #queue = Queue.Queue()
        #
        #parser = Parse(queue)
        #crawler = CrawlData(queue)
        
        self.last_series = ""
        
        self._extract_movie_list(extract_filename)

    def _extract_movie_list(self, extract_filename):
        count = 0
        
        file_break = 10000
        file_count = 0
        
        file = open(extract_filename, 'r')
        temp_file = open("temp/%s-%d.txt" %(extract_filename, file_count), "w")
        for i in range(16):
            line = file.readline()
        while line:
            self._is_series(line)
            line = file.readline()
            #return
            
        file.close()
        
    def _is_series(self, line):
        reg = ".*(\d{4}-[\d{4}|?{4}]).*"
        compiled = re.compile(reg)
        match = compiled.findall(line)
        
        if match:
            self._parse_series(line)
        else:
            self._parse_movie(line)
    
    def _parse_movie(self, line):
        line = line.strip()
        
        # check for series
        try:
            tokens = line.split('"')
            film_name = tokens[1].replace('"', '')
            if film_name == self.last_series:
                self._parse_series(line)
                return
        except:
            self.logger.info("%s is not a movie " % line)
            print "%s is not a movie " % line
        #end check
        
        self.last_series = ""
        tokens = line.split("\t")
        film_detail = []
        for token in tokens:
            if token:
                film_detail.append(token)
                
        try:
            film_name = film_detail[0]
            release_year = film_detail[1]
            #self.movie.write("%s\t%s\n" % (film_name, release_year))
            #query = "INSERT INTO (title, year) VALUES('%s', '%s')" % (film_name, release_year)
            #try:
            #    self.sql.query(query)
            #except:
            #    self.logger.error("%s query raised error" % query)
        except:
            self.logger.error("%s has some error" % line)
    
    def _parse_series(self, line):
        string = line.strip()
        line = string
        play_name = ""
        release_date = ""
        eposide_name = ""
        season_eposide = ""
        
        error = ""
        
        
        try:
            first = string.index('"')
            string = string[first+1:]
            second = string.index('"')
            play_name = string[:second]

            string = string[second+1:]
        except:
            e = "\tplay_name(%s)" % play_name
            error += e
            
        #------------------------------------------------
        try:
            first = string.index('(')
            string = string[first+1:]
            second = string.index(')')
            release_date = string[:second]

            string = string[second+1:]
        except:
            error += "\trelease_date"
        #------------------------------------------------
        try:
            first = string.index('{')
            string = string[first+1:]
            second = string.index('}')
            dummy = string[:second]
            eposide_name = dummy
        
        #try:
            first = dummy.index("(")
            eposide_name = dummy[:first]
            dummy = dummy[first+1:]
            season_eposide = dummy.replace("#", "").replace("(", "").replace(")", "")
            string = string[second+1:]
        except:
            error += "\teposide_name and season&eposid no"
        
        #------------------------------------------------
        try:
            string = string.strip()
            show_date = string
        except:
            error += "\tshow_date"
        #------------------------------------------------
        
        # log if any error occurs
        if error:
            self.logger.error("%s has following error : %s" %(line, error))

        self.movie.write("%s\t%s\n" % (film_name, release_year))
        
        #query = "INSERT INTO (title, year, season, eposide, ) VALUES('%s', '%s')" % (film_name, release_year)
        #try:
        #    self.sql.query(query)
        #except:
        #    self.logger.error("%s query raised error" % query)
        
        self.last_series = play_name
        self.series.write("%s\t%s\t%s\t%s\t%s\n" % (play_name, release_date, eposide_name, season_eposide, show_date))
        
        
#class Parse(threading.Thread):
#    def __init__(self, queue):
#        self.queue = queue
#        self.loop = True
#        threading.Thread.__init__(self)
#        
#    def run(self):
#        while(self.loop):
#            pass
#        
#        
#    def stop(self):
#        self.loop = False
#    
#class CrawlData(threading.Thread):
#    def __init__(self, queue):
#        self.queue = queue
#        self.loop = True
#        threading.Thread.__init__(self)
#        
#    def run(self):
#        while(self.loop):
#            pass
#        
#    def stop(self):
#        self.loop = False
#        
#    def _extract_file(self):
#        pass
#        
#if __name__ == '__main__':
#    MovieList()
import re

#string = '"#1 Single" (2006) {Cats and Dogs (#1.4)}		2006'
#string = '"(La) nouvelle Maud" (2010) {(#1.1)}			2010-????'
#
#play_name = ""
#release_date = ""
#eposide_name = ""
#season_eposide = ""
#
#
#first = string.index('"')
#string = string[first+1:]
#second = string.index('"')
#play_name = string[:second]
#
#string = string[second+1:]
#
#
##------------------------------------------------
#first = string.index('(')
#string = string[first+1:]
#second = string.index(')')
#release_date = string[:second]
#
#string = string[second+1:]
#
##------------------------------------------------
#
#first = string.index('{')
#string = string[first+1:]
#second = string.index('}')
#dummy = string[:second]
#
#first = dummy.index("(")
#eposide_name = dummy[:first]
#dummy = dummy[first+1:]
#season_eposide = dummy.replace("#", "").replace("(", "").replace(")", "")
#
#string = string[second+1:]
#
##------------------------------------------------
#
#string = string.strip()
#show_date = string
#
##------------------------------------------------
#
#print
#print
#print "play name        : ", play_name
#print "release_date     : ", release_date
#print "eposide_name     : ", eposide_name
#print "Season.Eposide   : ", season_eposide
#print "Show Date        : ", show_date
#





##########################################
###       check if it is series        ###
##########################################




#line = '"!Next?" (1994)						1994-1995'
#line1 = '"!Next?" (1994)						1994-?'
#
#reg = ".*(\d{4}-[\d{4}|?{4}]).*"
#com = re.compile(reg)
#
#m = com.findall(line)
#print line
#if m:
#    print "is series"
#else:
#    print "is movie"
#    
#m = com.findall(line1)
#print line1
#if m:
#    print "is series"
#else:
#    print "is movie"





line = '"077 hizir - Acil servis" (1988)			1988-????'

tokens = line.split("\t")
print tokens
print

for token in tokens:
    if token:
        print token
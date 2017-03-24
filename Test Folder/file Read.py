import codecs
import os

path = 'C:\Users\JonyC\Documents\GitHub\PAC-Proj1\NodeLists'
for filename in os.listdir(path):
    print(filename)
    os.chdir(path)
    data = codecs.open(filename,'r','utf-8')
    line = data.readline()

    while line:
        print line.encode('utf-8')
        userID = line[:line.find(' ')].encode('utf-8')
        userName = line[line.find(' ')+1:].encode('utf-8')
        print "userID, userName ", userID, userName
        line = data.readline()
    data.close

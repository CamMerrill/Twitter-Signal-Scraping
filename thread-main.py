import auth
import tweepy
import csv
import sys

from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

concurrent = 10

def doWork():
    while True:
        userName = q.get()
	#GetDataFromTL
	#WriteData to CSV
        q.task_done()

inputFileName = str(sys.argv[1:])
inputFile = open(inputFileName[2:-2], "r")

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for line in inputFile:
        q.put(line)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)

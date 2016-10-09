
import imp
import sys
import subprocess
import os


foo = imp.load_source('module.name', 'google/spiders/data.py')


searchURL ="https://www.google.fr/search?q="+ str(sys.argv[2])
#searchEngine = str(sys.argv[2])
searchLanguage = str(sys.argv[3])
if searchLanguage == 'en':
    foo.domains = "google.com"
    searchURL ="https://www.google.com/search?q="+ str(sys.argv[2])

if searchLanguage == 'fr':
    foo.domains = "google.fr"
    searchURL ="https://www.google.fr/search?q="+ str(sys.argv[2])

foo.urls = searchURL

print (searchLanguage)
print (foo.domains)
print (foo.urls)

## call date command ##
outputFilename = str(sys.argv[1])
cmnd = "scrapy crawl googleSearch -a domain='" + foo.domains + "' -a url='" + foo.urls+ "' -o " + outputFilename + ".csv -t csv"
print (cmnd)

#os.system("python google/spiders/data.py")
p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, shell=True)

## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
#Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate. The optional input argument should be a string to be sent to the child process, or None, if no data should be sent to the child.
(output, err) = p.communicate()

## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
#print ("Command output : ", err)
print ("Command exit status/return code : ", p_status)

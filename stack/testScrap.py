#import commands
#onAC_Power=True if comands.getstatus("on_ac_power")==0 else False

#import os
#os.system("scrapy crawl stack -o items12.json -t json")
'''
import sys
sys.path.append('/stack/spiders')
import stack_spider

print (stack_spider.a)
print (stack_spider.name)
'''
import imp

foo = imp.load_source('module.name', 'stack/spiders/stack_spider.py')
b= foo.stack_spider()
print (b.name)
b.name = 'Ankit'
print ("2", b.name)
'''

import subprocess
#subprocess.run(["ls", "-la"])
#CompletedProcess(args='ls -la', returncode=0)
#print (a)


## call date command ##
p = subprocess.Popen("scrapy crawl stack -o items1234.json -t json", stdout=subprocess.PIPE, shell=True)

## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
#Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate. The optional input argument should be a string to be sent to the child process, or None, if no data should be sent to the child.
(output, err) = p.communicate()

## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
#print ("Command output : ", err)
print ("Command exit status/return code : ", p_status)
'''

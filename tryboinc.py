import subprocess
import os
import time
from subprocess import call
from os import environ

account_key = (os.environ.get('ACCOUNT_KEY'))

try:
    call(['sudo', 'apt', 'install', 'boinc', 'y'],
         stdout=open(os.devnull,'wb'), stderr=STDOUT)
    time.sleep(360)
except:
    print('errors')
    pass

try:
    call(['boinc', '--abort_jobs_on_exit', '--attach_project', 'www.worldcommunitygrid.org', 'ACCOUNT_KEY'],
         stdout=open(os.devnull,'wb'), stderr=STDOUT)
except:
    print('errorsagain')
    pass
import subprocess
import os
import time
from subprocess import call
from os import environ

#CODE IS UNFINISHED, THIS IS JUST A TEMPLATE TO WORK ON. UNTESTED.
#Get your key from the IBM grid profile, and prepare it according to the computing hosts you want to use, or just replace ACCOUNT_KEY as your needs are and privacy permits.
#The program will try to install boinc, then sleeps for 5 minutes to allow for installation time. Next it connects to the IBM grid and starts contributing.

account_key = (os.environ.get('ACCOUNT_KEY'))

try:
    subprocess.run(['sudo', 'apt install boinc -y'])
    time.sleep(360)
except:
    print('errors')
    pass

try:
    subprocess.run(['boinc', '--allow_multiple_clients --abort_jobs_on_exit --attach_project www.worldcommunitygrid.org (ACCOUNT_KEY)'])
except:
    print('errorsagain')
    pass

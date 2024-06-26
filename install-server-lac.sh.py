import os
import sys
import subprocess
import string
import random

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'

f = open(bashfile, 'w')
s = """cd /root/.config/
mkdir unity3d
cd unity3d
mkdir MA
cd MA
mkdir LAC
cd LAC
wget https://lacrimesonline.com/builds/LAC/ServerConfig.txt
cd /$HOME
mkdir LACINSTALL
cd LACINSTALL
wget https://lacrimesonline.com/builds/LAC/LAC_Linux_v1.7.1.zip
unzip LAC_Linux_v1.7.1.zip
chmod +x LAC_Linux_v1.7.1.x86_64
screen -S test
./LAC_Linux_v1.7.1.x86_64
"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)

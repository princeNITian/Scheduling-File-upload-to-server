import paramiko
import random
from datetime import datetime

import os,glob,shutil

path = "C:\\Users\\princ\\Desktop\\6th_sem\\Devlopment\\Django\\deepak\\to_upload\\"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            # files.append(os.path.join(r, file))
            files.append(file)
# files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='216.10.240.65',username='prince',password='Prince@543',port=22)
sftp_client = ssh.open_sftp()
#print(dir(sftp_client).__dir__())

# To download we use the next line
#sftp_client.get('/home/learn7sd/public_html/prince/index.html','learn_index.html')

# by changing directory without giving full path
def download(filename):
    # temp = str(random.randrange(1,100)) + filename
    # temp = '/downloaded/' + temp
    sftp_client.chdir('/home/learn7sd/public_html/deepak')
    sftp_client.get(filename,'downloaded/'+filename)
    print("Downloaded: ",filename)

# To upload
def upload(filename):
    baseDir = '/home/learn7sd/public_html/deepak/'
    temp = baseDir + filename
    filename = 'to_upload/'+filename
    sftp_client.put(filename,temp)
    print('Uploaded: ', filename,"at dir: ",baseDir)
    dest = shutil.move(filename, 'uploaded/')
    print("moved to : ",dest)

# while True:
#     #Check time
#     now = datetime.now()
#     time = now.strftime("%H:%M:%S")
#     # print("time:", time)
#     if time=="01:01:00":
#         download('transfer.py')
#         print("Success")
#         break




# To download a file just call download() with the file name
# Let's download all the files which is uploaded which resides in uploaded directory
def downloadAll():
    path1 = "C:\\Users\\princ\\Desktop\\6th_sem\\Devlopment\\Django\\deepak\\uploaded\\"
    files1 = []
    for r, d, f in os.walk(path1):
        for file in f:
            if '.txt' in file:
                # files.append(os.path.join(r, file))
                files1.append(file)
    for f in files1:
        download(f)
        # print(f)
    print("DownloadAll Succeed.")

# Invoke downloadAll() which will call download function
#downloadAll()


#########################     SCHEDULING GOES HERE     ###############
schedule = '19:54:30'
print('Infinite while loop is running: ')
print("It will terminate after scheduling time: ",schedule)
while True:
    #Check Time
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    # print("time:",time)
    if time == schedule:
        for f in files:
            upload(f)
            # download
            #download(f)
        break


sftp_client.close()
ssh.close()
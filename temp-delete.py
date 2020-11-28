import os,subprocess
file_size = os.path.getsize('C://Users//AppData//Local//Temp//')#write Temp path
print("{} kb of data will be removed".format(file_size))
del_dir = r'C:\Users\ag612\AppData\Local\Temp'

process = subprocess.Popen('rmdir /S /Q {}'.format(del_dir), shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
_ = process.communicate()
return_code = process.returncode
if return_code == 0:
    print('cleaned')
else:
    print('Fail: Unable to Clean Windows Temp Folder')

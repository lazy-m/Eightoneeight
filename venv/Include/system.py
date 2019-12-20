import os
import requests

print(os.sep)

dirs = 'E:\\'
files = os.listdir(dirs)

for files in files:
    print(dirs + os.sep + files)

url = "https://www.baidu.com/img/bd_logo1.png"

print(isinstance(url, str))
# my_dir ='C:\\Users\\cnclick\\Desktop\\美女'
# re = requests.get(url)
# #判断目录是否存在
# print(os.path.exists(my_dir))
# if not os.path.exists(my_dir) :
#     os.makedirs(my_dir)
#
# with open(my_dir+'\\'+url.split('/')[-1],"wb") as img:
#     img.write(re.content)

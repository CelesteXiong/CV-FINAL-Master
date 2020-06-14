import zipfile
import os
startdir = "/data/cv_final/CT-Predict"  #要压缩的文件夹路径
file_news = startdir +'.zip' # 压缩后文件夹的名字
z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) 
for dirpath, dirnames, filenames in os.walk(startdir):
#     print( filenames)
    fpath = dirpath.replace(startdir,'') #这一句很重要，不replace的话，就从根目录开始复制
    fpath = fpath and fpath + os.sep or ''
    for filename in filenames:
        z.write(os.path.join(dirpath, filename),fpath+filename)
        print ('successful!')
z.close()
# unzip
import os
# import shutil
import zipfile
def unzip_file(zip_src, dst_dir):
    '''
      src_dir：你要压缩的文件夹的路径
      zip_name：压缩后zip文件的路径及名称
    '''
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')


path = '/data/COVID-CT/Images-processed/CT_NonCOVID.zip'
unzip_file(path, '/data/COVID-CT/Data')
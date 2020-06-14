import os
import glob
import gzip
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pylab as plt
# 读取.nii文件 
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
import numpy as np

# 查看当前文件路径
path = '/data/data'
file_paths = glob.glob(os.path.join(path, '*.gz'))
print(file_paths)

# 解压数据文件，数据文件格式为.nii.gz
for file in file_paths:
    print(file)
    file = file.split('/')[-1]
    print(file)
    new_file_name = file.replace(".gz", "")
    print(new_file_name)
    # 开始解压
    g_file = gzip.GzipFile(file)
    print(g_file)
    #读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
    new_file_name = os.path.join(path, new_file_name)
    open(new_file_name, "wb+").write(g_file.read())
    g_file.close()

# 读取数据文件 
file1 = 'tr_im.nii'
file2 = 'tr_mask.nii'
file3 = 'val_im.nii/val_im.nii'
files = [file1, file2]
train_data_dir = 'data/data/train/data'
valid_data_dir = 'data/data/valid/data'

# 提取训练集和验证集的数据
for file in files:
    img = nib.load(file)
    width,height,queue=img.dataobj.shape
    j = 0
    for i in range(0, queue, 1):
        img_arr = img.dataobj[:,:,i]
        if i<70:
            # cur_file = '/%s.npy'%(i+1)
            filename = train_data_dir + cur_file
            np.save('train/data/%s.npy'%(i+1), img_arr)
        else:
            filename = valid_data_dir + cur_file
            np.save('valid/data/%s.npy'%(j+1), img_arr)
            j = j+1
        print(img_arr)
    print (img)


# 提取训练集和验证集的label
img_label = nib.load(file3)
width,height,queue=img_label.dataobj.shape
### 编写label
def convert(array):
    a = np.copy(array)
    a[a!=0] = 3
    a[a==0] = 1
    a[a==3] = 0
    
    b = np.copy(array)
    b[b!=1] = 3
    b[b==3] = 0
    
    c = np.copy(array)
    c[c!=2] = 3
    c[c==2] = 1
    c[c==3] = 0
    
    new_array = np.concatenate((a,b,c),axis=0).reshape(3,512,512)
    new_array.shape
    # (3, 512, 512)
    return new_array

j = 0
for i in range(0, queue, 1):
    img_arr = img_label.dataobj[:,:,i]
    new_arr = convert(img_arr)
    if i<70:
        cur_file = '/%s.npy'%(i+1)
#         filename = train_data_dir + cur_file
        np.save('train/label/%s.npy'%(i+1), new_arr)
    else:
#         filename = valid_data_dir + cur_file
        np.save('valid/label/%s.npy'%(j+1), new_arr)
        j = j+1
    print(img_arr)
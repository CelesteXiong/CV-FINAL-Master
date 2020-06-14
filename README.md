# cv_final

to do:

1. [x] 2D 网络数据集
2. [x] Project COVIT-CT 迁移学习
3. [x] 3D 网络数据集
4. [x] 3D resnet 
5. [ ] seg

## 1. Data

### 1.1 [wuhan](http://ncov-ai.big.ac.cn/download?lang=en)

1. 数据处理 (两种方式):
   - [x] 对于 2D network()
     - 对于一个病人, 挑选其所有检查里居中的检查结果
     - 对于一个检查结果, 挑选出一张肺部中心的照片(即所有照片中最中间的肺部切片)
     - 最后的结果是, 每个病人对应一张照片, 相同类别的照片放在一个文件夹下
     - 文件夹组织

        ```python
        - train
            - CP
              - img1.png
              - img2.png
            - Normal
            - COVID19
        - val
        - test
        ```

   - 对于 3D network
     - 对于一个病人, 挑选其所有检查里居中的检查结果
     - 对于一个检查结果, 挑选出一张肺部中心的照片(即所有照片中最中间的肺部切片), 即靠近中心的左右各十张图片
     - 最后的结果是, 每个病人对应一个文件夹, 内有 21 张(10 + 10 + 1)照片, 相同类别的照片放在一个文件夹下
     - 文件夹组织

        ```python
        - train
            - CP
              - patient_id
                - img1.png
                - img2.png
            - Normal
            - COVID19
        - val
        - test
        ```

2. 使用`pytorch DataLoader` 从文件夹中读取数据, 文件夹名称作为标签

## 2.Project

### 2.1 COVID-CT

1. 迁移学习: 使用`Self-trans`模型权重, 初始化`DenseNet129`
2. 结果:
   - 1
      - train: 386
      - val: 111
      - tets: 56
      - The epoch is 10, average recall: 0.6875, average precision: 1.0000,average F1: 0.8148, average accuracy: 0.8214, average AUC: 1.0000

   -  

### 2.2 Few-shot adaptive net


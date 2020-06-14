# cv_final


## 1. Data
### Class:

- novel coronavirus pneumonia (NCP)
- common pneumonia
- normal controls.

### Sources:

1. COVID-19 CT Segmentation Dataset([COVID19-CT](http://medicalsegmentation.com/covid19/))
   - 40+ subjects, 512 \* 512 \* 100 array for all
2. 2019 Novel Coronavirus Resource ([2019nCoVR](http://ncov-ai.big.ac.cn/download?lang=en))
   - NCP-Data: 336 subjects, 512 \* 512 \* [40-100] images per subject
   - Normal-Data: 165 subjects, 512 \* 512 \* [40-100] images per subject
3. UCSD CT Scan Dataset about COVID-19([UCSD COVID19-CT](https://github.com/UCSD-AI4H/COVID-CT.git))
   - 349 images from 300+ subjects, 512 \* 512 per image

### Preprocess:
1. 对于 2D network
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
2. 对于 3D network
 - 对于一个病人, 挑选其所有检查里居中的检查结果
 - 对于一个检查结果, 挑选出一张肺部中心的照片(即所有照片中最中间的肺部切片), 即靠近中心的左右各2张图片
 - 最后的结果是, 每个病人对应一个文件夹, 内有 4 照片, 相同类别的照片放在一个文件夹下
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

## 2.Project

### Segmentation

### Classification



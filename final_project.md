# Project指南 

## 1）重要时间点

- 开题报告（5分）：`2020年5月10日`

- demo（5分）：`2020年6月9日`

- 最终报告（20分）：`2020年6月12日`


## 2）开题报告

在开题报告中，请简要说明如下内容，字数为500～1000字。

- 题目（确切题目可以在最终报告中更改）
- 小组成员（1～3人，列出姓名和学号。总体原则是，小组成员越多，我们对project成果要求越高，比如工作量、模型的原创性、改进程度、实验结果的提高、实际应用等等）
- 课题要解决的问题，以及课题的意义（即解决这个问题有什么用，比如，可以是好玩，也可以是改变世界<img src="img/WechatIMG4622.jpeg" alt="laugh" width="20"/>）
- 有哪些相关工作可以参考（请列举2到3篇非常相关的论文的工作）
- 技术路线（模型概述，代码来源，模型改进方案等，目前不需要非常精确的描述）
- 实验手段（数据来源，评价指标，预期结果等）

开题报告命名为`“学号-proposal.pdf”`，多人小组只需写一个学号。到时会开放服务器给大家上传。


## 3）demo

由于本学期非毕业班将不会返校，所以我们采用线上demo形式，要求如下。

- 每组5～10分钟
- 5～10页ppt，说明课题、模型细节、实验设置、实验结果
- 现场演示：自由发挥


## 4）最终报告

最终报告将是project打分的最主要依据，请以论文的标准认真撰写。在报告中你要详细阐述如下内容，请使用**[模板] (http://106.75.225.141/chieh/2020_ecnu_dase_cv_assignment/blob/master/utility/%E5%AD%A6%E5%8F%B7-report.docx)**，篇幅**不超过10页**。请不要更改字体和行距。

- 题目
- 作者（姓名+学号）
- 摘要
- 绪论：详细说明课题意义，研究内容，现有方案及其缺陷（可选），简述你的研究方案以及本课题的contribution
- 相关工作：相关文献调研
- 模型和算法细节：详细说明你的模型结构，画出模型结构图，编写相关公式，编写必要的算法（请参考文献中的写法）
- 实验：实验设置（数据、超参设置、评价指标等），实验结果（主要结果、消融实验、调参实验等）（请参考文献中的写法，最好有比较实验，证明你的模型的优势）
- 应用效果（可选）：app，网站，小程序等
- 结论：讨论并总结课题、未来工作等。
- 参考文献
- 附录：1）请详细列出每位小组成员的具体贡献。2）请将所有代码和数据上传到gitlab，并在附录中给出链接。可以在附录中编写仓库readme。3）其他

最终报告命名为“学号-report.pdf”，多人小组只需写一个学号。到时会开放服务器给大家上传。



## 5）候选project（图像识别/分类/检测）

- [细粒度鸟类分类] (https://www.lintcode.com/ai/Bird_Classification/overview)

- [人脸器官检测] (https://www.lintcode.com/ai/detection-facial-keypoints/overview)

- [新冠肺炎识别] (https://www.kaggle.com/bachrr/covid-chest-xray)

- [垃圾分类1] (https://www.kaggle.com/techsash/waste-classification-data)

- [垃圾分类2] (https://pan.baidu.com/s/1HDCmcJFhdXQa_C7UKg7esw)


## 6）自选project
你也可以参考各类资源（论文、博客解读、git项目、机器学习比赛等等），自己选定project题目和寻找数据集。这里有部分参考资源。

### 6.1）论文

#### `论文读法：先看论文中的图片及其描述，了解大概做什么；然后依次看abstract，method/model，experiments/results/performance；然后去搜索博客解读，最好看英文博客或者知乎，CSDN能不看就不看；最后决定要不要细看原文。`

- 图像分类

[ImageNet Classification with Deep Convolutional Neural Networks] (https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)

[ImageNet Large Scale Visual Recognition Challenge] (https://arxiv.org/abs/1409.0575)

[Going Deeper with Convolutions] (https://arxiv.org/abs/1409.4842)

[Very Deep Convolutional Networks for Large-Scale Image Recognition] (https://arxiv.org/abs/1409.1556)

[Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition] (https://arxiv.org/abs/1406.4729)

[Densely Connected Convolutional Networks] (https://arxiv.org/abs/1608.06993)

[Learning Transferable Architectures for Scalable Image Recognition] (https://arxiv.org/abs/1707.07012)

- 目标检测

[Rich feature hierarchies for accurate object detection and semantic segmentation] (https://arxiv.org/abs/1311.2524)

[Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks] (https://arxiv.org/abs/1506.01497)

[Mask R-CNN] (https://arxiv.org/abs/1703.06870)

- 图像分割

[Fully Convolutional Networks for Semantic Segmentation] (https://arxiv.org/abs/1411.4038)

[Learning Deconvolution Network for Semantic Segmentation] (https://arxiv.org/abs/1505.04366)

[DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs] (https://ieeexplore.ieee.org/abstract/document/7913730)

- 图像描述

[Show and Tell: A Neural Image Caption Generator] (https://arxiv.org/abs/1411.4555)

[Show, Attend and Tell: Neural Image Caption Generation with Visual Attention] (https://arxiv.org/abs/1502.03044)

[DenseCap: Fully Convolutional Localization Networks for Dense Captioning] (https://arxiv.org/abs/1511.07571)

[Long-term Recurrent Convolutional Networks for Visual Recognition and Description] (https://arxiv.org/abs/1411.4389)

[Deep Visual-Semantic Alignments for Generating Image Descriptions] (https://cs.stanford.edu/people/karpathy/deepimagesent/)


- 图片生成

[Generative adversarial nets] (http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)

[Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks] (https://arxiv.org/abs/1511.06434)

[Conditional Image Synthesis with Auxiliary Classifier GANs] (https://arxiv.org/abs/1610.09585)

- 风格转换

[Image Style Transfer Using Convolutional Neural Networks] (http://openaccess.thecvf.com/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)

[Image-to-Image Translation with Conditional Adversarial Networks] (http://openaccess.thecvf.com/content_cvpr_2017/papers/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.pdf)

[Unpaired image-to-image translation using cycle-consistent adversarial networks] (http://openaccess.thecvf.com/content_ICCV_2017/papers/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.pdf)


### 6.2）数据集

[Meta Pointer] (http://www.cvpapers.com/datasets.html)

[Yet another Meta pointer] (http://riemenschneider.hayko.at/vision/dataset/)

[ImageNet] (http://http//image-net.org/) 图像识别大型数据集

[SUN Database] (http://groups.csail.mit.edu/vision/SUN/) 目标检测

[Places Database] (http://places.csail.mit.edu/) 场景识别

[Microsoft COCO] (http://mscoco.org/) 图像识别，分割和描述

[LFW] (http://vis-www.cs.umass.edu/lfw/) 人脸标注数据集

[MPII Human Pose] (http://human-pose.mpi-inf.mpg.de/) 人体姿势数据集

### 6.3）其他

[Papers with code] (https://paperswithcode.com/area/computer-vision)

[awesome-deep-vision] (https://github.com/kjw0612/awesome-deep-vision)
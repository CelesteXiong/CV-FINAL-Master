# Classification

## 2D

### DenseNet 169 baseline

1. on UCSD COVID19-CT data set: classification\2D_Network-with-Self_trans\baseline.ipynb

### DenseNet Transfer Learning

1. on UCSD COVID19-CT data set: classification\2D_Network-with-Self_trans\UCSD.ipynb

2. on 2019nCoVR data set: classification\2D_Network-with-Self_trans\2D2019nCovR.ipynb

## 3D ResNet18

1. on 2019nCoVR data set: classification\3D_Network\3D2019nCovR.ipynb

## Result
|                                                  | Accuracy | F1     | AUC    |
| ------------------------------------------------ | -------- | ------ | ------ |
| 在UCSD COVIT-CT 上训练的DenseNet169 baseline     | 0.72     | 0.70   | 0.81   |
| 在UCSD COVIT-CT 上训练的DenseNet-169(Self-Trans) | 0.74     | 0.75   | 0.75   |
| 在COVID19-CT 上训练的DenseNet-169(Self-Trans)    | 0.9411   | 0.9565 | 0.9775 |
| 在COVID19-CT 上训练的3D ResNet18                 | 0.9019   | 0.9275 | 0.9100 |


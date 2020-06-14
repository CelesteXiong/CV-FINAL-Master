运行环境：
pytorch 1.3
torchvision 0.2
python 3.6.5


运行方式：
cd segmentation  // 进入文件夹
python train.py --config "segmentation/config/default.config"
// config后面的文件路径保证是绝对路径

data_preprocess.py // 数据预处理文件
// 数据集来源：http://medicalsegmentation.com/covid19
# 微信跳一跳

卷积神经网络判断棋子和目标块的坐标

## 写在前面

目前的网络已经达到3500分的水平。
![example](https://raw.githubusercontent.com/zyayoung/image-repository/master/jump_example.png)

为1080p分辨率开发

## Requirements

- PIL
- tensorflow
- keras
- jupyter

## 为什么要建立这个项目？

之前写过朴素算法的跳一跳脚本，因为特殊情况不好处理，干脆尝试使用卷积神经网络处理。
卷积神经网络在类似问题上有极大潜力。

## 仓库内包含什么有用的东西？

- 验证卷积神经网络解决此类问题的可行性
- 方便修改的数据处理+网络训练脚本ExperimentSpace/CreatModel.ipynb(使用jupyter-notebook打开)
- 预先采集的2500个训练数据data.pkl.gz
- 预先训练的模型model.h5
- 全自动玩游戏的脚本play.py(需要调整比例系数)

## 数据预处理

数据保存在ExperimentSpace/data.pkl.gz中

数据读取方法：
```
f=gzip.open('data.pkl.gz')
X_train,y_train = pickle.load(f)
f.close()
```

数据简介：

- 原始数据是2500张png截图，文件名包含训练需要的数据：编号,x,y,x,y
- 对数据分别进行裁剪、缩放、边缘过滤、灰度
```
img = img.crop((0, 500, 1080, 1300))
img = img.resize((img.width/resize_ratio, img.height/resize_ratio), Image.ANTIALIAS)
img = img.filter(ImageFilter.CONTOUR).convert('L')
img = np.array(img)/255.0
```

![example2](https://raw.githubusercontent.com/zyayoung/image-repository/master/jump_example2.png)

- 打包成pickle.gz的形式
```
f=gzip.open('data.pkl.gz','wb')
X_train = np.array(X_train,dtype='float32').reshape(-1,100,135,1)
y_train = np.array(y_train,dtype='float32').reshape(-1,4)
pickle.dump((X_train,y_train),f)
f.close()
```

详见[CreatModel.ipynb](https://github.com/zyayoung/wechat_DLjump/blob/master/ExperimentSpace/CreatModel.ipynb)

## 我的网络结构

```
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
conv2d_1 (Conv2D)            (None, 100, 135, 48)      1776
_________________________________________________________________
activation_1 (Activation)    (None, 100, 135, 48)      0
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 50, 68, 48)        0
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 50, 68, 64)        76864
_________________________________________________________________
activation_2 (Activation)    (None, 50, 68, 64)        0
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 50, 68, 64)        102464
_________________________________________________________________
activation_3 (Activation)    (None, 50, 68, 64)        0
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 50, 68, 64)        102464
_________________________________________________________________
activation_4 (Activation)    (None, 50, 68, 64)        0
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 50, 68, 64)        102464
_________________________________________________________________
activation_5 (Activation)    (None, 50, 68, 64)        0
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 25, 34, 64)        0
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 25, 34, 64)        102464
_________________________________________________________________
activation_6 (Activation)    (None, 25, 34, 64)        0
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 13, 17, 64)        0
_________________________________________________________________
flatten_1 (Flatten)          (None, 14144)             0
_________________________________________________________________
dense_1 (Dense)              (None, 4)                 56580
_________________________________________________________________
activation_7 (Activation)    (None, 4)                 0
=================================================================
Total params: 545,076
Trainable params: 545,076
Non-trainable params: 0
_________________________________________________________________
None
```

我觉得网络的结构和输出设计是最重要的，并且需要很多的尝试。

从原理上来说输出坐标更合理。横纵坐标和距离是非线性关系，应该在神经网络给出两个坐标之后再用两点之间距离公式计算出距离。

现在我的样本数量扩充到了2500， 推荐在github上找一个成熟项目，修改成自动获取样本的程序。

## clone之后该做什么？

- 解压model.h5.zip
- 运行play.py
- 探索ExperimentSpace/CreatModel.ipynb
- 尝试下载其他人的项目，制作数据采集程序（可选）
- 修改网络，训练网络


Gave me a star and do whatever you want.

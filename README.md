# 微信跳一跳

卷积神经网络判断棋子和目标块的坐标

## 写在前面

这个项目的目的是尝试用神经网络判断位置，而不是为了刷分。如果你是为了在排行榜上排到第一才来的，那么请在github上找1k+stars的项目。

为1080p分辨率开发

## Requirements

- PIL
- tensorflow
- keras
- jupyter

## 为什么要建立这个项目？

之前写过朴素算法的跳一跳脚本，因为特殊情况不好处理，干脆尝试使用卷积神经网络处理。

## 仓库内包含什么有用的东西？

按照价值从高到低排列：

- 验证了卷积神经网络解决此类问题的可行性
- 方便修改的数据处理+网络训练脚本ExperimentSpace/CreatModel.ipynb(使用jupyter-notebook打开)
- 预先采集的977个训练数据data.pkl.gz
- 预先训练的模型model.h5
- 全自动玩游戏的脚本play.py

## clone之后该做什么？

- 解压model.h5.zip
- 运行play.py
- 探索ExperimentSpace/CreatModel.ipynb
- 尝试下载其他人的项目，制作数据采集程序（可选）
- 修改网络，训练网络


Gave me a star and do whatever you want.

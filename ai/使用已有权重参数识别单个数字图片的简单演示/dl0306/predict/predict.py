#!/usr/bin/env python
import pickle
import numpy as np
from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)
try:
    from mnist import load_mnist
except load_mnist:
    raise


def sigmoid(x1):
    """
    @fn sigmoid()
    @brief sigmoid激活函数
    @details 将爆开映射到(0,1)之间
    @param
    @return
    """
    return 1 / (1 + np.exp(-x1))


def softmax(a):
    """
    @fn softmax()
    @brief 归一化指数函数
    @details 使每一个元素的范围在(0,1)之间，多用于多分类问题中。
    @param
    @return
    """
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y2 = exp_a / sum_exp_a
    return y2


def get_data():
    """
    @fn get_data()
    @brief 获取MNIST数据集数据函数
    @details 通过调用mnist模块中的load_mnist函数获取MNIST数据集数据。
    @return x_train 训练图像数据
    @return t_train 训练标签数据
    @return x_test 测试图像数据
    @return t_test 测试标签数据
    """
    (x_train, t_train), (x_test, t_test) =\
        load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_train, t_train, x_test, t_test


def init_network():
    """
    @fn init_network()
    @brief 读入权重参数函数
    @details 读取已经事先准备好的权重参数的pkl文件。
    @return network1 权重参数
    """
    with open("../weight/sample_weight.pkl", 'rb') as f:
        network1 = pickle.load(f)

    return network1


def predict(network1, x1):
    """
    @fn predict()
    @brief 神经网络推导函数
    @details 使用权重参数和测试数据进行三层神经网络推导。
    @param network1 权重参数
    @param x1 单个测试用图像数据
    @return y1 推导出的结果
    """
    w1, w2, w3 = network1['W1'], network1['W2'], network1['W3']
    b1, b2, b3 = network1['b1'], network1['b2'], network1['b3']
    a1 = np.dot(x1, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y1 = softmax(a3)
    print(y1)
    p = np.argmax(y1)

    return p

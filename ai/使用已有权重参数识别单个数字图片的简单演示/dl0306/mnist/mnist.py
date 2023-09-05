#!/usr/bin/env python3
import urllib.request  # HTTP请求库之请求模块
import os.path
import gzip
import pickle  # 持久化模块。把数据转化为二进制数据流存储于文件中，便于以后调用
import os
import numpy as np


# MNIST数据集文件下载地址
url_base = 'http://yann.lecun.com/exdb/mnist/'
# MNIST数据集的四个压缩文件，分别为：训练图像文件、训练标签文件、测试图像文件、测试标签文件。
# MNIST数据集的一般使用方法是：先用训练图像进行学习，再用学习到的模型度量能在多大程度上对测试图像进行正确的分类。
key_file = {
    'train_img': 'train-images-idx3-ubyte.gz',
    'train_label': 'train-labels-idx1-ubyte.gz',
    'test_img': 't10k-images-idx3-ubyte.gz',
    'test_label': 't10k-labels-idx1-ubyte.gz'
}

# 通过当前文件所在绝对路径获取当前目录名称
dataset_dir = os.path.dirname(os.path.abspath(__file__))
# 要保存的pkl文件的名称
save_file = dataset_dir + "/mnist.pkl"

train_num = 60000  # 训练数据的数量
test_num = 10000  # 测试数据的数量
img_dim = (1, 28, 28)  # 存放图像数据的数组。MNIST中的图像为28*28的灰度图像。
img_size = 784  # 每个图像的大小，即28*28。


def _download(file_name):
    """
    @fn _download()
    @brief 下载函数
    @details 用于从网络下载指定的文件。
    @param file_name 要下载的文件名称
    """
    file_path = dataset_dir + "/" + file_name

    # 如果文件已经存在就退出
    if os.path.exists(file_path):
        return

    print("Downloading " + file_name + " ... ")
    # 从指定网址下载文件
    urllib.request.urlretrieve(url_base + file_name, file_path)
    print("Done")


def download_mnist():
    """
    @fn download_mnist()
    @brief 下载MNIST数据集函数
    @details 遍历MNIST数据集文件名称表，调用下载函数来下载。
    """
    for v in key_file.values():
        _download(v)


def _load_label(file_name):
    """
    @fn _load_label()
    @brief 载入标签文件函数
    @details 载入指定名称的标签压缩文件，解压并转化为需要的格式后返回数据。
    @param file_name 标签压缩文件名称
    @return labels 标签文件数据
    """
    file_path = dataset_dir + "/" + file_name

    print("Converting " + file_name + " to NumPy Array ...")
    with gzip.open(file_path, 'rb') as f:
        # uint8是一个字节。offset是偏移量，标签文件前8位是文件类型与数据数量，不是真正的数据，因此这里要偏移8个字节。
        labels = np.frombuffer(f.read(), np.uint8, offset=8)
    print("Done")

    return labels


def _load_img(file_name):
    """
    @fn _load_img()
    @brief 载入图像文件函数
    @details 载入指定名称的图像压缩文件，解压并转化为需要的格式后返回数据。
    @param file_name 图像压缩文件名称
    @return data 图像文件数据
    """
    file_path = dataset_dir + "/" + file_name

    print("Converting " + file_name + " to NumPy Array ...")
    with gzip.open(file_path, 'rb') as f:
        # 图像文件前16位是文件类型、数据数量和图像由几乘几构成，不是真正的数据，因此这里要偏移16个字节。
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    data = data.reshape(-1, img_size)
    print("Done")

    return data


def _convert_numpy():
    """
    @fn _convert_numpy()
    @brief 以字典形式读取MNIST数据的函数
    @details 以字典形式读取各个MNIST数据集数据。
    @return dataset MNIST数据集数据字典
    """
    dataset = {
        'train_img': _load_img(key_file['train_img']),
        'train_label': _load_label(key_file['train_label']),
        'test_img': _load_img(key_file['test_img']),
        'test_label': _load_label(key_file['test_label'])}

    return dataset


def init_mnist():
    """
    @fn init_mnist()
    @brief MNIST数据集初始化函数。
    @details 对MNIST数据集数据进行初始化。第一次执行时时间会长一些，因为要从网上下载、解压、转换并保存为pkl文件。
    """
    download_mnist()
    dataset = _convert_numpy()
    print("Creating pickle file ...")
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)
    print("Done!")


def _change_one_hot_label(x1):
    """
    @fn _change_one_hot_label()
    @brief 把标签数据转换为one-hot形式。
    @details one-hot表示是仅正确解标签为1，其余皆为0的数组，如[0,0,1,0,0,0,0,0,0,0]。
    @param x1 标签数据
    @return t one-hot形式的标签数组
    """
    # 本程序中，训练标签文件中有60000个数据，测试标签文件中10000个数据。
    # np.zeros函数生成了(60000, 10)或(10000, 10)的数组，数值均为0，在不指定数据类型的情况下，默认为float64。
    t = np.zeros((x1.size, 10))
    for idx, row in enumerate(t):
        # x1[idx]即每个标签数据的实际值，如1、3、7等。
        # row[x1[idx]]是根据标签的实际值定义到相应位置，并赋值为1，
        # 这样就把本来是0至9的数值映射到前面定义的数组t上。
        # 当然，转换后的数组是x1.size*10的，占用空间比x1大得多，但数值仅为0与1，从这方面看又有特殊的用处。
        row[x1[idx]] = 1

    return t


def load_mnist(normalize=True, flatten=True, one_hot_label=False):
    """
    @fn load_mnist()
    @brief 读入MNIST数据集函数
    @details 综合载入MNIST数据集数据。
    @param normalize 将图像的像素值正规化为0.0~1.0
    @param flatten 是否将图像展开为一维数组
    @param one_hot_label
        one_hot_label为True的情况下，标签作为one-hot数组返回
        one-hot数组是指[0,0,1,0,0,0,0,0,0,0]这样的数组
    @return MNIST数据
    """
    if not os.path.exists(save_file):
        init_mnist()

    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /= 255.0

    if one_hot_label:
        dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
        dataset['test_label'] = _change_one_hot_label(dataset['test_label'])

    if not flatten:
        for key in ('train_img', 'test_img'):
            # reshape函数把图像数据转换为(-1,1,28,28)的数组，-1表示不知道这一维具体数值是多少，由实际数据决定。
            dataset[key] = dataset[key].reshape(-1, 1, 28, 28)

    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])


if __name__ == '__main__':
    init_mnist()

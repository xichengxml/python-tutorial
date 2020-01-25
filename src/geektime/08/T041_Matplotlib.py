import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sbn


# ---------------------------
# @description
# pip3 install matplotlib -i https://pypi.douban.com/simple
# pip3 install seaborn -i https://pypi.douban.com/simple
# @author xichengxml
# @date 2019/10/7 下午 07:30
# ---------------------------


# 画直线
def draw_line():
    plt.plot([1, 2, 3], [2, 4, 8])


# 使用numpy和matplotlib绘制正弦曲线
def draw_sin():
    # 生成-π到π之间的100个点
    x = np.linspace(-np.pi, np.pi, 100)
    plt.plot(x, np.sin(x))


# 绘制多条曲线
def draw_multi():
    # -2π到2π
    x = np.linspace(-np.pi * 2, np.pi * 2, 100)
    # dpi代表图片精细度，dpi越大文件越大，杂志要300以上
    plt.figure(1, dpi=50)
    for i in range(1, 5):
        plt.plot(x, np.sin(x / i))


# 绘制直方图
def draw_hist():
    data = [1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5]
    plt.figure(1, dpi=50)
    # 只要传入数据, 直方图就会统计数据出现的次数
    plt.hist(data)


# 绘制散点图
def draw_scatter():
    x = np.arange(1, 10)
    y = x
    plt.figure()
    # 颜色，形状
    plt.scatter(x, y, c='r', marker='o')


# seaborn是matplot的美图秀秀版
def draw_seaborn():
    iris = pd.read_csv('../../resources/iris/iris_training.csv')
    # 设置样式
    sbn.set(style='white', color_codes=True)
    # 设置绘图格式为散点图
    sbn.jointplot(x='120', y='4', data=iris, size=5)
    # 绘制曲线
    sbn.distplot(iris['120'])


# 绘制不同颜色的散点图
def draw_color_seaborn():
    iris = pd.read_csv('../../resources/iris/iris_training.csv')
    # 设置样式
    sbn.set(style='white', color_codes=True)
    sbn.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "setosa", "versicolor").add_legend()


if __name__ == '__main__':
    graph_type = input('请输入要绘制的图类型: line--直线; sin--正弦曲线; multi--多条曲线; '
                       'hist--直方图; scatter--散点图\n')
    if graph_type == 'line':
        draw_line()
    elif graph_type == 'sin':
        draw_sin()
    elif graph_type == 'multi':
        draw_multi()
    elif graph_type == 'hist':
        draw_hist()
    elif graph_type == 'scatter':
        draw_scatter()
    elif graph_type == 'seaborn':
        draw_seaborn()
    elif graph_type == 'color_seaborn':
        draw_color_seaborn()

    # 只是让pandas 的plot() 方法在pyCharm上显示
    plt.show()

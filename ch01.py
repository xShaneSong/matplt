import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
# y = np.cos(x)
# 展示变量的趋势变化
# plt.plot(x, y, ls = '-', lw = 2, label = 'plot figure')

# y = np.random.rand(1000)
# 录找变量之间的关系
# plt.scatter(x, y, label = 'scatter figure')

# x,y轴的数据显示范围
# plt.xlim(0.05, 10)
# plt.ylim(0, 1)

y = np.sin(x)
plt.plot(x, y, ls="-.", lw = 2, c = "c", label="plot figure")

# 标签文本
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# 网格线
plt.grid(linestyle = ":", color = "r")

# # 水平参考线
# plt.axhline(y = 0.0, c = "r", ls = "--", lw = 2)
# plt.axvline(x = 4.0, c = "r", ls = "--", lw = 2)

# 垂直于x轴的参考区域
plt.axvspan(xmin = 4.0, xmax = 6.0, facecolor = "y", alpha = 0.3)
plt.axhspan(ymin = 0.0, ymax = 0.5, facecolor = "y", alpha = 0.8)

# 添加图形内容细节的指向型注释文本
plt.annotate("maximum", xy = ((np.pi/2) + 1.0, .8), weight = "bold", color = "b",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color = "b"))

# 添加图形内容细节的无指向型注释文本
plt.text(3.10, 0.09, "y=sin(x)", weight = "bold", color = "b")

# 添加图形内容标题
plt.title("y=sin(x)")

# 标示不同图形的文本标签图例
plt.legend()

plt.show()


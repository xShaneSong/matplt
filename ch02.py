#-*- coding:utf-8 -*

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# mpl.rcParams["font.sans-serif"] = ["SimHei"]
# mpl.rcParams["axes.unicode_minus"] = False

# some simple data
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [3, 1, 4, 5, 8, 9, 7, 2]

# 柱状图
# plt.bar(x, y, align="center", color="c",
#         tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/")

# 条形图
# plt.barh(x, y, align="center", color="c",
#         tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/")

# boxWeight = np.random.randint(0, 10, 100)
# x = boxWeight

# bins = range(0, 11, 1)
# 直方图
# plt.hist(x, bins = bins, color="g", histtype="bar", rwidth=1, alpha=0.6)

# # set x, y_axis label
# plt.xlabel("箱子编号")
# plt.ylabel("箱子编号(kg) ")

# 饼图
# kinds = "A", "B", "C", "D"
# colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]
# soldNums = [0.04, 0.45, 0.15, 0.35]
# plt.pie(soldNums, labels=kinds, autopct="%3.1f%%", startangle=60, colors=colors)
# plt.title("不同类型箱子的销售数量占比")

# 极线图
# barSlices = 12
# theta = np.linspace(0.0, 2 * np.pi, barSlices, endpoint=12)
# r = 30*np.random.random(barSlices)
# plt.polar(theta, r, color="chartreuse", linewidth=2, marker="*", mfc="b", ms=10)

# 气泡图
# a = np.random.randn(100)
# b = np.random.randn(100)
# colormap:RdYlBu
# plt.scatter(a, b, s=np.power(10*a + 20 * b, 2), c = np.random.rand(100), cmap=mpl.cm.RdYlBu , marker="o")

#棉棒图
# x = np.linspace(0.5, 2* np.pi, 20)
# y = np.random.randn(20)
# plt.stem(x, y, linefmt="-.", markerfmt="o", basefmt="-")


# 箱线图
# mpl.rcParams["font.sans-serif"] = ["FangSong"]
# mpl.rcParams["axes.unicode_minus"] = False
# x = np.random.randn(1000)
# plt.boxplot(x)
# plt.xticks([1], ["随机数生成器AlphaRM"])
# plt.ylabel("随机数值")
# plt.title("随机生成器抗干扰能力的稳定性")
# plt.grid(axis="y", ls=":", lw=1, color="gray", alpha=0.4)

# 误差棒图
x = np.linspace(0.1, 0.6, 6)
y = np.exp(x)
plt.errorbar(x, y, fmt="bo:", yerr=0.2, xerr=0.02)
plt.xlim(0, 0.7)

plt.show()

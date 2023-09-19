#-*- coding:utf-8 -*

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 堆积柱状图
# x = [1, 2, 3, 4, 5]
x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]
# plt.bar(x, y, align="center", color="#66c2a5",
#          tick_label=["A", "B", "C", "D", "E"], label="A")
# plt.bar(x, y, align="center", color="#8da0cb",
#          bottom=y, label="B")

# 堆积条形图
# plt.barh(x, y, align="center", color="#66c2a5",
#          tick_label=["A", "B", "C", "D", "E"], label="A")
# plt.barh(x, y, align="center", color="#8da0cb",
#          left=y, label="B")

# 多数据并列柱状图
# bar_width = 0.35
# tick_label=["A", "B", "C", "D", "E"]
# plt.bar(x, y, bar_width, align="center", color="#66c2a5",
#           label="A", alpha = 0.5, hatch="///")
# plt.bar(x + bar_width, y1, bar_width, align="center", color="#8da0cb",
#          label="B", alpha=0.5, hatch="\\")
# plt.xticks(x + bar_width /2, tick_label)

# 多数据平行条形图
# plt.barh(x, y, bar_width, align="center", color="#66c2a5",
#           label="A", alpha = 0.5)
# plt.barh(x + bar_width, y1, bar_width, align="center", color="#8da0cb",
#          label="B", alpha=0.5)
# plt.yticks(x + bar_width /2, tick_label)

# 堆积折线图
# x = np.arange(1, 6, 1)
# y = [0, 4, 3, 5, 6]
# y1 = [1, 4, 3, 2, 7]
# y2 = [3, 4, 1, 6, 5]

# labels = ["BluePlant", "BrownPlant", "GreenPlant"]
# colors = ["#8da0cb", "#fc8d62", "#66c2a5"]
# plt.stackplot(x, y, y1, y2, labels=labels, colors=colors)

# 间断条形图
# plt.broken_barh([(30, 100), (180, 50), (260, 70)], (20, 8), facecolors="#1f78b4")
# plt.broken_barh([(60, 90), (190, 20), (230, 30), (280, 60)], (10, 8),
#                  facecolors=("#7fc97f", "#beaed4", "#fdc086", "#ffff99"))
# plt.xlim(0, 360)
# plt.ylim(5, 35)
# plt.xticks(np.arange(0, 361, 60))
# plt.yticks([15, 25], ["A", "B"])
# plt.grid(ls="-", lw=1, color="gray")

# 阶梯图
# x = np.linspace(1, 10, 10)
# y = np.sin(x)
# plt.step(x, y, color="#8dd3c7", where="pre", lw=2)
# plt.xlim(0, 11)
# plt.xticks(np.arange(1, 11, 1))
# plt.ylim(-1.2, 1.2)

# 直方图
# scoresT = np.random.randint(0, 100, 100)
# x = scoresT
# bins = range(0, 101, 10)
# plt.hist(x, bins = bins, color="#377eb8", histtype="bar" , rwidth=5)

# 饼图
# labels = ["A", "B", "C", "D"]
# students = [0.35, 0.15, 0.20, 0.30]
# colors = ["#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
# explode = (0.1, 0.1, 0.1, 0.1)
# plt.pie(students, explode=explode, labels=labels, autopct="%3.1f%%", 
#         startangle=45, shadow=True, colors=colors, pctdistance=0.7, labeldistance=1.2)

# 箱线图
# testA = np.random.randn(5000)
# testB = np.random.randn(5000)
# testList = [testA, testB]
# labels = ["AlphaRM", "BetaRM"]
# colors = ["#1b9e77", "#d95f02"]
# whis = 1.6
# width = 0.35
# bplot = plt.boxplot(testList, whis=whis, widths=width, sym="o", labels=labels, patch_artist=True)
# for patch, color in zip(bplot["boxes"], colors):
#     patch.set_facecolor(color)
# plt.grid(axis="y", ls=":", lw = 1, color="gray", alpha = 0.4)

# 误差棒图
x = np.linspace(0.1, 0.6, 10)
y = np.exp(x)
error = 0.05 + 0.15 * x
lower_error = error
upper_error = 0.3 * error
error_limit = [lower_error, upper_error]
plt.errorbar(x, y, yerr=error_limit, fmt=":o", 
             ecolor="y", elinewidth=4, ms=5, mfc="c", mec="r", capthick=1, capsize=2)
plt.xlim(0, 0.7)

plt.xlabel("X")
plt.ylabel("Y")

plt.legend()
plt.show()


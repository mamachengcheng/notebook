import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 5, endpoint=True)
c = np.cos(x)
s = np.sin(x)

# plt.plot(x, c, color="green", linewidth=1.0, linestyle="-", label="cos")    # 普通图

# plt.plot(x, s, color="blue", linewidth=1.0, linestyle="-", label="sin")     # 普通图

plt.scatter(x, c)                                                           # 散点图

# plt.bar(x, c, facecolor='#ff9999', edgecolor='white')                       # 条形图

# plt.ylim(-1.0, 1.0)                                                         # 设置横轴上下限
#
# plt.xlim(-4.0, 4.0)                                                         # 设置纵轴上下限
#
# plt.xticks(np.linspace(-4, 4, 9, endpoint=True))                            # 设置横坐标
#
# plt.yticks(np.linspace(-1, 1, 5, endpoint=True))                            # 设置纵坐标
#
# plt.legend(loc="upper left")                                                # 设置图例位置
#
# ax = plt.gca()
#
# ax.spines['right'].set_color('none')
#
# ax.spines['top'].set_color('none')
#
# ax.xaxis.set_ticks_position('bottom')
#
# ax.spines['bottom'].set_position(('data', 0))
#
# ax.yaxis.set_ticks_position('left')

# ax.spines['left'].set_position(('data', 0))



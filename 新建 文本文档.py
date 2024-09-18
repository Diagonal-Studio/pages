import math
import matplotlib.pyplot as plt
import numpy as np

# 定义J型增长函数
def j_growth(r, N0, t):
    return N0 * math.exp(r * t)

# 定义逻辑斯蒂增长函数
def logistic_growth(r, K, N0, t):
    return K / (1 + math.exp(-r * (t - 5)))

# 参数设置
r = 1  # 增长率
K = 1500  # 环境容纳量
N0 = 1  # 初始种群数量
t_max = 50  # 最大时间
t = np.linspace(0, t_max, 400)  # 创建时间数组

# 计算J型增长和逻辑斯蒂增长的种群数量
N_j = [j_growth(r, N0, ti) for ti in t]
N_logistic = [logistic_growth(r, K, N0, ti) for ti in t]

# 绘制曲线
plt.figure(figsize=(10, 5))
plt.plot(t, N_j, label='J型增长 (Exponential Growth)')
plt.plot(t, N_logistic, label='逻辑斯蒂增长 (Logistic Growth)', linestyle='dashed')
plt.title('J型增长与逻辑斯蒂增长曲线')
plt.xlabel('时间')
plt.ylabel('种群数量')
plt.legend()
plt.grid(True)
plt.show()
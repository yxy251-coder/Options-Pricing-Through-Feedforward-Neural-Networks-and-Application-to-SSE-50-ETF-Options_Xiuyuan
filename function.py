from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np
import pandas as pd
from pandas import DataFrame
import math
import matplotlib.pyplot as plt

def prediction_visualization(y_t, y_p, window_lenth, right_move):
	x = range(0, len(y_t))[right_move:right_move+window_lenth]
	y1 = y_t[right_move:right_move+window_lenth]
	y2 = y_p[right_move:right_move+window_lenth]
	plt.figure(figsize = (10, 8), dpi = 80)    # 定义一个图像窗口
	plt.plot(x, y1, color = "blue", linewidth = 1, linestyle = "-", label = "true value") # 绘制曲线 y1
	plt.plot(x, y2, color = "red", linewidth = 1, linestyle = "--", label = "prediction value") # 绘制曲线 y2
	plt.xlabel("data point")
	plt.ylabel("option price")
	plt.legend(loc = "upper right")
	plt.show()

def mape(y_true, y_pred):
	n = len(y_true)
	mape = sum(np.abs((y_true - y_pred)/y_true))/n*100
	return mape

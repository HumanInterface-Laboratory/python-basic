import math         # mathモジュールをインポート
import numpy as np  # numpyモジュールをインポート
from matplotlib import pyplot as plt    # matplotlibモジュールからpyplotをインポート

# 0から2πまでの範囲でsin関数を作成
pi = math.pi    # mathモジュールのπを取得
x = np.linspace(0, 2*pi, 100)   # 0から2πまでの範囲を100分割
y = np.sin(x)   # sin関数を作成

# グラフを描画
plt.plot(x, y)
plt.show()

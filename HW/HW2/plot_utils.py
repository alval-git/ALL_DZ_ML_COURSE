import matplotlib.pyplot as plt
import numpy as np

def real_and_predict_target_plot(y_pred, y_real, target):
  plt.figure(figsize=(30, 15))
  plt.scatter(range(100), y_real[:100], color='green', label='real')
  plt.scatter(range(100), y_pred[:100], color = 'red', label='predicted')
  plt.ylabel(target)
  plt.xlabel('id')
  plt.title(f'real and predicted values of {target}')
  plt.xticks(ticks= np.arange(0, 100, 1))
  plt.yticks(ticks= np.arange(8, 15, 0.5))
  plt.grid(True)
  plt.legend()
  plt.show()

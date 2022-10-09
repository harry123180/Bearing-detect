path = 'data\\normal.output16.csv'
#f = open(path, 'r')
from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
import csv
def open_file(file_path,start=1,final=1024):
    list1, list2, list3 = [],[],[]
    count = 0
    with open(file_path, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for i in rows:
            print(i[0],i[1],i[2])
            if(count>start and count<final):
                #pre = i.split(" ")
                #print(pre[0], pre[1], pre[2])
                list1.append(float(i[1]))
                list2.append(float(i[2]))
                #list3.append(float(i[3]))
            count+=1

    return list1,list2,list3
def fftx(data,N,Samping_Rate):

    fft_y = fft(data)
    abs_y = np.abs(fft_y)  # 取複數的絕對值，即複數的模(雙邊頻譜)
    #angle_y = np.angle(fft_y)  # 取複數的角度
    normalization_y = abs_y / N  # 歸一化處理（雙邊頻譜）
    normalization_half_y = normalization_y[range(int(N / 2))]  # 由於對稱性，只取一半區間（單邊頻譜）
    xf = fftfreq(N, 1 / Samping_Rate)[:N // 2]
    return xf,normalization_half_y
    #plt.plot(xf, normalization_half_y, alpha=0.9)
data1,data2,data3 = open_file(file_path = path)
""" ***********************  """
y_data1 = np.array(data1)
y_data2 = np.array(data2)
#y_data3 = np.array(data3)
plt.ion()
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(211)#2個圖 橫版只放1 1號位置
ax2 = fig.add_subplot(212)#2個圖 橫版只放1 2號位置
#ax3 = fig.add_subplot(313)#2個圖 橫版只放1 2號位置
""" ***********************  """
a1,b1= fftx(y_data1,128,1000)
a2,b2= fftx(y_data2,128,1000)
#a3,b3= fftx(y_data3,256,1000)
ax1.plot(a1,b1)
ax2.plot(a2,b2)
#ax3.plot(a3,b3)
fig.show()
plt.pause(100)
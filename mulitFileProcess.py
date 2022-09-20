
from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
def open_file(start=0,final=1024,path=''):
   # path = 'output.txt'
    f = open(path, 'r')
    list1, list2, list3 = [],[],[]
    count = 0
    for i in f.readlines():
        if(count>start and count<final):
            i.strip('\n')
            pre = i.split(" ")
            #print(pre[0], pre[1], pre[2])
            list1.append(float(pre[0]))
            list2.append(float(pre[1]))
            list3.append(float(pre[2]))
        count+=1
    f.close()
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
def OA(Amplitude):
    total_square = 0
    for i in range(len(Amplitude)):
        total_square = total_square+pow(Amplitude[i],2)
    return 0.8165*pow(total_square,0.5)
file = open('result.txt', 'w')
file.write("1axis_OA            2axis_OA            3axis_OA \n")
for cnt in range(100):
    data1,data2,data3 = open_file(path = 'output'+str(cnt)+'.txt')
    """ ***********************  """
    y_data1 = np.array(data1)
    y_data2 = np.array(data2)
    y_data3 = np.array(data3)
    file.write(str(OA(data1))+" "+str(OA(data2))+" "+str(OA(data3))+'\n')
file.close()

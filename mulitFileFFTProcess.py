from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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

x = []
y = []
z = []
for cnt in range(100):
    data1,data2,data3 = open_file(path = 'output'+str(cnt)+'.txt')
    """ ***********************  """
    y_data1 = np.array(data1)
    y_data2 = np.array(data2)
    y_data3 = np.array(data3)
    a1, b1 = fftx(y_data1, 1024, 1000)
    x.append(a1)
    y.append(np.ones((512)) * cnt)
    z.append(b1)

fig = plt.figure(figsize=(8,6))
ax3d = plt.axes(projection="3d")
ax3d = plt.axes(projection='3d')
print(np.shape(np.array(x)),np.shape(np.array(y)),np.shape(np.array(z)))
surf=ax3d.plot_surface(np.array(x), np.array(y), np.array(z), rstride=7, cstride=7, cmap="viridis")
fig.colorbar(surf, ax=ax3d)
ax3d.set_title('Surface Plot in Matplotlib')
ax3d.set_xlabel('X')
ax3d.set_ylabel('Y')
ax3d.set_zlabel('Z')

#plt.savefig("Customized Surface Plot.png")

plt.show()
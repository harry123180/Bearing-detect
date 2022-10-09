path = 'data\\normal.output16.csv'
#f = open(path, 'r')
from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
import csv
def open_file(file_path,start=1,final=128):
    list1, list2, list3 = [],[],[]
    count = 0
    with open(file_path, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for i in rows:
            #print(i[0],i[1],i[2])
            if(count>start and count<final):
                #pre = i.split(" ")
                #print(pre[0], pre[1], pre[2])
                list1.append(float(i[1]))
                list2.append(float(i[2]))
                #list3.append(float(i[3]))
            count+=1

    return np.array(list1),np.array(list2)
def fftx(data,N,Samping_Rate):

    fft_y = fft(data)
    abs_y = np.abs(fft_y)  # 取複數的絕對值，即複數的模(雙邊頻譜)
    #angle_y = np.angle(fft_y)  # 取複數的角度
    normalization_y = abs_y / N  # 歸一化處理（雙邊頻譜）
    normalization_half_y = normalization_y[range(int(N / 2))]  # 由於對稱性，只取一半區間（單邊頻譜）
    xf = fftfreq(N, 1 / Samping_Rate)[:N // 2]
    return xf,normalization_half_y
    #plt.plot(xf, normalization_half_y, alpha=0.9)
def save_CSV(new_file_path,write_data_list):
    with open(new_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 寫入二維表格
        writer.writerows(write_data_list)

""" ***********************  """
#y_data3 = np.array(data3)
""" ***********************  """

re_counter = 0
for counter in range(1,5969):
    if( (counter>=1 and counter <=500) or (counter>=3001 and counter <= 4511)):

        data_type = 'normal'
        pathname= 'data\\'+data_type+'.output'+str(counter)+'.csv'
        data1, data2 = open_file(file_path=pathname)
        a1, b1 = fftx(data1, 128, 1000)
        a2, b2 = fftx(data2, 128, 1000)
        wr_list = [['timestamp', 'accX', 'accZ']]
        for h in range(len(a1)):
            wr_list.append([h,b1[h],b2[h]])
        new_path_name = 'FFT_data\\'+data_type+'_FFT.output'+str(re_counter)+'.csv'
        save_CSV(new_path_name,wr_list)
        re_counter+=1
    elif ((counter>=501 and counter <=1001) or (counter>=5501 and counter <= 5969)):
        data_type = 'bad'
        pathname = 'data\\' + data_type + '.output' + str(counter) + '.csv'
        data1, data2 = open_file(file_path=pathname)
        a1, b1 = fftx(data1, 128, 1000)
        a2, b2 = fftx(data2, 128, 1000)
        wr_list = [['timestamp', 'accX', 'accZ']]
        for h in range(len(a1)):
            wr_list.append([h, b1[h], b2[h]])
        new_path_name = 'FFT_data\\' + data_type + '_FFT.output' + str(re_counter) + '.csv'
        save_CSV(new_path_name, wr_list)
        re_counter += 1

    elif ((counter>=2001 and counter <=2423) or (counter>=4601 and counter <= 5111)):
        data_type = 'ceramics'
        pathname = 'data\\' + data_type + '.output' + str(counter) + '.csv'
        data1, data2 = open_file(file_path=pathname)
        a1, b1 = fftx(data1, 128, 1000)
        a2, b2 = fftx(data2, 128, 1000)
        wr_list = [['timestamp', 'accX', 'accZ']]
        for h in range(len(a1)):
            wr_list.append([h, b1[h], b2[h]])
        new_path_name = 'FFT_data\\' + data_type + '_FFT.output' + str(re_counter) + '.csv'
        save_CSV(new_path_name, wr_list)
        re_counter += 1
    print(re_counter)




import serial  # 引用pySerial模組
import csv

COM_PORT = 'COM4'    # 指定通訊埠名稱
BAUD_RATES = 115200   # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠
state = False
signal=[[],[],[]]
count =0
label = ['normal','bad','ceramics']
which = 0 #這個改當前軸承是哪一類
sample_count = 0
def conver(org):
    return round(float(org),2)
try:
    while True:
        while ser.in_waiting:          # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()   # 用預設的UTF-8解碼
            if (state == True):
                signal[0].append(data.split()[0])
                signal[1].append(data.split()[1])
                signal[2].append(data.split()[2])
                count +=1
            if(data =="START"):
                state = True
            elif ( count > 255):
                count =0
                with open(label[which]+'.output'+str(sample_count)+'.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['time','accX', 'accY', 'accZ'])
                    for cnt1 in range(255):
                        writer.writerow([cnt1,conver(signal[0][cnt1]), conver(signal[1][cnt1]), conver(signal[2][cnt1])])



except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件
    print('再見！')
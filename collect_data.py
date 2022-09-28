import serial  # 引用pySerial模組
import csv

COM_PORT = 'COM3'  # 指定通訊埠名稱
BAUD_RATES = 115200  # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)  # 初始化序列通訊埠

state = False
signal = [[], [], []]
count = 0
label = ['normal', 'bad', 'ceramics']

which = 1  # 這個改當前軸承是哪一類
sample_count = 1046  # 第幾筆DATA


def conver(org):
    return round(float(org), 2)


try:
    while True:

        while ser.in_waiting:  # 若收到序列資料…
            data_raw = ser.readline()  # 讀取一行
            data = data_raw.decode()  # 用預設的UTF-8解碼

            # print(len(data) < 18,state)
            if (state == True):
                # print(data)
                # print(data.split()[1])
                signal[0].append(data.split()[1])
                signal[1].append(data.split()[2])
                signal[2].append(data.split()[3])
                count += 1
            if (len(data) < 18):
                # print("Get")
                state = True
            elif (count > 255):
                state = False
                count = 0
                sample_count += 1
                try:
                    with open(label[which] + '.output' + str(sample_count) + '.csv', 'w', newline='') as csvfile:
                        print(label[which] + '.output' + str(sample_count) + '.csv')
                        writer = csv.writer(csvfile)
                        writer.writerow(['time', 'accX', 'accY', 'accZ'])
                        for cnt1 in range(255):
                            writer.writerow(
                                [cnt1, conver(signal[0][cnt1]), conver(signal[1][cnt1]), conver(signal[2][cnt1])])
                        signal = [[], [], []]
                        csvfile.close()
                except:
                    ser.close()  # 清除序列通訊物件
                    print("ERROR")

except KeyboardInterrupt:
    ser.close()  # 清除序列通訊物件
    print('再見！')
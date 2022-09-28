import os
from edge_impulse_linux.runner import ImpulseRunner
import serial  # 引用pySerial模組

COM_PORT = 'COM3'  # 指定通訊埠名稱
BAUD_RATES = 115200  # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)  # 初始化序列通訊埠
runner = None

def data_proccsser():
    count=0
    read_data =[]
    try:
        while True:
            while ser.in_waiting:  # 若收到序列資料…
                data_raw = ser.readline()  # 讀取一行
                data = data_raw.decode()  # 用預設的UTF-8解碼
                if (state == True):
                    read_data.append(data.split()[1]) #X
                    read_data.append(data.split()[3]) #Z
                    count += 1
                if (len(data) < 18):
                    state = True
                if(len(data)<3):
                    state = False
                    return read_data
    except KeyboardInterrupt:
        ser.close()  # 清除序列通訊物件
        print('再見！')

def main():
    model = 'modelfile.eim'

    #features_file = io.open(args[1], 'r', encoding='utf8')
    features = data_proccsser()
    #features_file.read().strip().split(",")
    if '0x' in features[0]:
        features = [float(int(f, 16)) for f in features]
    else:
        features = [float(f) for f in features]


    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)

    print('MODEL: ' + modelfile)


    runner = ImpulseRunner(modelfile)
    try:
        model_info = runner.init()
        print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')

        res = runner.classify(features)
        print("classification:")
        print(res["result"])
        print("timing:")
        print(res["timing"])

    finally:
        if (runner):
            runner.stop()

if __name__ == '__main__':
    main()
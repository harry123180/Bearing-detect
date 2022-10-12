import random
import csv
def dt():
    return round(random.uniform(-20, 20),2)
for i in range(100):
    file_name = 'good.sample'+str(i+100)+'.csv'
    # 開啟輸出的 CSV 檔案
    with open(file_name , 'w', newline='') as csvfile:
      # 建立 CSV 檔寫入器
      writer = csv.writer(csvfile)

      # 寫入一列資料
      writer.writerow(['timestamp','accX', 'accY', 'accZ'])
      for j in range(256):
      # 寫入另外幾列資料
          writer.writerow([j, dt(), dt(),dt()])

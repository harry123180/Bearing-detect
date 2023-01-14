from os import listdir
from os.path import isfile, isdir, join
import csv
# 指定要列出所有檔案的目錄
mypath = "D:\AWORKSPACE\Github\Bearing-detect\data"
savepath = "D:\AWORKSPACE\Github\Bearing-detect\onlytwoTypeData"
# 取得所有檔案與子目錄名稱
files = listdir(mypath)

# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    #print("f的type=",type(f))
    if(f[0]=='c'):
      print("檔案：", f)
    if (f[0] == 'n'):
      print("檔案：", f)
  elif isdir(fullpath):
    print("目錄：", f)
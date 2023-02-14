from os import listdir,sep,rename
from os.path import isfile, isdir, join
import csv
# 指定要列出所有檔案的目錄
mypath = "D:\AWORKSPACE\Github\Bearing-detect\onlytwoTypeData_FFT"
savepath = "D:\AWORKSPACE\Github\Bearing-detect\onlytwoTypeData_FFT"
# 取得所有檔案與子目錄名稱
files = listdir(mypath)

# 以迴圈處理
counter=0
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    counter+=1
    #print("f的type=",type(f))
    if(f[0]=='c'):

      # 设置旧文件名（就是路径+文件名）
      oldname = savepath + sep + f  # os.sep添加系统分隔符
      # 设置新文件名
      newname = savepath + sep + 'bad.FFT_output' + str(counter) + '.csv'
      rename(oldname, newname)  # 用os模块中的rename方法对文件改名
      print("檔案：", f," 檔案名稱: ",newname)
    if (f[0] == 'n'):
      #print("檔案：", f)
      # 设置旧文件名（就是路径+文件名）
      oldname = savepath + sep + f  # os.sep添加系统分隔符
      # 设置新文件名
      newname = savepath + sep + 'normal.FFT_output' + str(counter) + '.csv'
      rename(oldname, newname)  # 用os模块中的rename方法对文件改名
      print("檔案：", f, " 檔案名稱: ", newname)
  elif isdir(fullpath):
    print("目錄：", f)




'''
注釋
'''
# 注釋



# .py必要
# -*- coding: UTF-8 -*-
#!/usr/bin/python



# 引用庫
import os
from copy import Error
try:
    ##################### import 寫在這裡 ################################

    OK = '_ATWImportThis = OK'
except ImportError:
    ##################### import 寫在這裡同上一樣 ################################

    OK = '_ATWImportThis = Error'



# Start = 加內容在這 
def Start2022():


    # try = 嚐試執行以下代碼, 如錯誤執行except
    try:
        print('寫在這裡')
        NowOK = 'Start2022() = OK'


        ##################### 寫在這裡 ################################




    # 返回 _Error function 的內容
    except Exception as e:
        for 行 in _Error(e):
            print(行)
        NowOK = 'Start2022() = Error'


    # 返回 NowOK
    return NowOK







# 錯誤時顯示文件位置及行數
def _Error(e):
    異常內容 = [
        '========= _Error ===========',
        e,      # Error說明,
        e.__traceback__.tb_frame.f_globals["__file__"], # 位置
        e.__traceback__.tb_lineno,  # 行
        '========= \ ==========='
    ]
    return 異常內容






'''
程式入口 = if __name__ == "__main__":

    py文件有2個用法

    1=直接打開

    2=引用(import)

    使用程式入口,當直接打開便會執行程式入口內的內容

    主要目的是引用時不用執行到無用的程式碼
'''
if __name__ == "__main__":
    print(Start2022())
    os.system("pause") 
    
    





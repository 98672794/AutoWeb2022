



##################### Start_2022PyT ################################
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

    ######################################################################
    ##################### import 寫在這裡 ################################
    ######################################################################

    # Python 連接到 Google 表格
    import pygsheets    # import 這次會使用到的 pygsheets庫

    OK = '_ATWImportThis = OK'
except ImportError:     # 如不能 import , install pygsheets庫
    ######################################################################
    ##################### import 寫在這裡同上一樣 #########################
    ######################################################################
    os.system('pip install pygsheets')  # install pygsheets庫
    import pygsheets

    OK = '_ATWImportThis = Error'














# Start = 加內容在這 
def Start2022():

    Talk = '''
            ****************
        將 Python 連接到 Google 表格 
        歡迎您 

        請將您的 金鑰json 放在同文件夾
        和準備好 Google 表格 網址

        *您必須先授權表格給服務帳戶
        
        說明
        https://github.com/98672794/Teaching2022/blob/main/6.1%20如何將%20Python連接到Google表格.md
    
        '''

    # try = 嚐試執行以下代碼, 如錯誤執行except
    try:

        NowOK = 'Start2022() = OK'
        ######################################################################
        ####################### Code 寫在這裡 ################################
        ######################################################################

        # index
        print(Talk)
        while True: # 不能空值loo
            Your金鑰json = input('請填寫金鑰json文件名\n*必須放在同文件夾\n(不需要 .json)')
            if Your金鑰json == '': continue    # 不能空值

            YourGoogleSheetUrl = input('請填寫Google 表格網址\n*您必須先授權表格給服務帳戶\n')
            if YourGoogleSheetUrl == '': continue    # 不能空值

            break
        Your金鑰json = Your金鑰json + '.json'   # 加副檔名


        # 連接到 Google 表格
        gc = pygsheets.authorize(service_file=Your金鑰json)     # gc 這邊是告訴 Python 我們的授權金鑰 json 放置的位子
        sht = gc.open_by_url(YourGoogleSheetUrl)        # 利用 Python 開啟 GoogleSheet
        print('##################')
        print('文件')
        print(YourGoogleSheetUrl)
        print('內的工作表=')
        print(sht.worksheets())     # 取得此GoogleSheet內的工作表
        print('##################')



        # 取得 Sheet 清單
        while True: # 不能空值loo
            Sheet清單序號 = input('請填寫工作表名')
            if Sheet清單序號 == '': continue    # 不能空值
            break
        wks = sht.worksheet_by_title(Sheet清單序號)






        # index2
        Talk = '''
            ****************
            請選擇功能

            0 ====== 更新工作表名稱
            1 ====== 讀取工作表
            2 ====== 寫入一格內容
            3 ====== 寫入一直欄
            4 ====== 刪除工作表內容
            5 ====== 隱藏工作表

            將Google文檔轉換為MicrosoftWord文檔

            '''
        while True: # 請選擇動作loo
            print('##################')
            print('直在編輯:',wks)
            print(Talk)
            Goto = input('請選擇動作\n')


            # 更新工作表名稱
            if Goto == '0':
                # 讀取
                表名 = input('請填寫工作表的新名稱\n')
                wks.title = 表名
                continue


            # 讀取工作表
            if Goto == '1':
                # 讀取
                print('將會顯示 2列及 3欄的內容')
                print(wks.get_row(2,include_tailing_empty=False))
                print(wks.get_col(3,include_tailing_empty=False))
                continue


            # 寫入一格內容
            if Goto == '2':
                # 寫入一格內容
                print("將會在A1,A2,A3 寫入 '5','10','=A1+A2'")
                wks.update_value('A1',5)      #  Store  5 at A1
                wks.update_value('A2',10)     #  Store 10 at A2
                wks.update_value('A3','=A1+A2',True) # Add data at A1 and A2 and store at A3
                continue


            # 寫入一直欄
            if Goto == '3':
                # 寫入
                print("將會在欄數由上至下寫入'ab','cd','ef'")

                try:    # 只可填寫數字loop
                    直欄數 = input('請填寫直欄數:A欄=1,B欄=2...\n')
                except:
                    print('只可填寫數字')
                    continue

                wks.update_col(int(直欄數),['ab','cd','ef']) # add list to 2nd column
                continue


            # 刪除工作表內容
            if Goto == '4':
                # 寫入
                刪除格 = input("請填寫要刪除內容的儲存格,如:\n A1,B10 = 刪除A1至B10\n")
                刪除格a = 刪除格.split(',')  # 用,分隔input data
                wks.clear(刪除格a[0],刪除格a[1]) # clear data from grid B3 to C5
                continue


            # 隱藏工作表
            if Goto == '5':
                # 隱藏
                wks.hidden = True
                continue



















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



# Opening the file and adding data https://www.plus2net.com/python/pygsheets.php
# https://www.maxlist.xyz/2018/09/25/python_googlesheet_crud/
##################### / Start_2022PyT ################################





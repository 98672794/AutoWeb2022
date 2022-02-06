

'''
winpy3

0Start
runThe.py
ATW202202061852
mokaki
https://98672794.github.io/


README()

Start()-|
        |
        |-ifUser--autoRun
        |-hv_atw----index
        |-not-----makeAcc
    -Er-|
    |
    _Error(e)







_atw - |0.atw / coed
       |--.py
       |--.html
       |--.job







'''




#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os 





##################################################
############### 開始執行同層的py檔 0Start.RunThePY()
def RunThePY():

    # 預設run
    BasePY = 'ATWError'

    # 說明
    Talk = [
        ' Start.RunThePY()  ',
        ' 開始執行同層的py檔  ',
        ' ======== ',
        ' 限同層 = 只檔名 ',
        ' ======== ',
        ' 請填寫同層的py檔名'
    ]
    for txt in Talk:
        print (txt)

    # 入py名
    PYname = input('\n')
    if PYname == '':
        PYname = BasePY
    
    # 轉全名.py
    dd = [
        "python ",
        "./",
        ".py"
        ]
    print ('開始執行',PYname,dd[2])
    NowRunThisPY = ((dd[1] + PYname + dd[2]))

    # Run py
    os.system((dd[0] + NowRunThisPY))

    return PYname

































##################################################
############### 請選擇功能 0Start.Start()
def Start():
    #print ('開始執行_Start')

    # 說明
    Talk = [
        '\n   =========== AutoWeb index 歡迎您 ===========',
        '\n   請選擇功能\n',
        '\n   0 ====== RunThePY\n   開始執行同層的py檔\n',
        '\n   ===========================================',
        '\n   0 ====== Auto Setting\n   修改您的資料\n',
        '\n   1 ====== Auto pip Import\n   自动安装所需的Python依赖包（pip install 包）\n',
        '\n   2 ====== Auto WebPage template\n   自動下載mobanwang網頁模板(XXX維護中XXX)\n',
        '\n   3 ====== Auto Sales\n   自動搵客，自動獲取工作相關的廣告資料\n',
        '\n   4 ====== Auto chromedriver\n   自动下載最新 chromedriver\n',
        '\n   5 ====== VIP KEY[ADMIN]\n   自动生成VIP驗證碼\n',
        '*** 只可填寫數字 ***\n'
    ]

    # Goto Fun loop 
    while True:
        print ('loop  Start')

        # 只可填寫數字
        try:
            for txt in Talk[0:-2]:
                print (txt)        # 說明
            Goto = int(input())
            pass    # 下步
        except:
            print(Talk[-1])
            continue    # 回 Goto Fun loop 

        ################################## Sel 0  開始執行同層的py檔  
        if Goto == 0:
            print ('********** Sel 0 *************') 
            print (' / END',RunThePY(),'.py')
            print ('********** /Sel 0 *************') 
            continue    # 回 Goto Fun loop 

















def _Error(e):
    #print(e)
    #print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    #print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数

    异常 = 'Error***'
    + (e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    +(e.__traceback__.tb_lineno)                        # 发生异常所在的行数
    +'***'
    
    return 异常













if __name__ == "__main__":
    Start()
    os.system("pause")






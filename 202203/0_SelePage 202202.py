

'''
win py3

1SelePage2022
1SelePage2022.py
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
############### 開始執行同層的py檔 1SelePage2022.RunThePY()
def RunThePY():

    # 預設run
    BasePY = 'ATWError'

    # 說明
    Talk = [
        ' 1SelePage2022.RunThePY()  ',
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
        '*** 只可填寫數字 ***\n'
    ]

    # RunThePY loop 
    while True:
        print ('***********************') 
        print (' / END',RunThePY(),'.py')
        print ('***********************') 
        continue    # 回 RunThePY loop 




















if __name__ == "__main__":
    Start()



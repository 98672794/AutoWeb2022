

'''
winpy3

1index
執行Github中的.py
ATW20220204
mokaki
https://98672794.github.io/


README()
Start() 
    if User autoRun
    hv _atw index
    not     makeAcc


    _Error(e)

'''

# -*- coding: UTF-8 -*-
##########################################################################import

import re


import ATWSteChrome
import ATWFolder
import ATWError
import ATW_OUT
import ATWREADME










###################################################################################
############################################################# 1index 說明
def README(): 
    ThisREADME = [
        '*** 1index.README ***', # PYfileName
        '000 =\n        000(000)',
        '000 =\n        000(000)',
        '000 =\n        000(000)',
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202051218',
        'https://98672794.github.io/'

    ]

    ATWREADME._READYourME(ThisREADME)















#######################################################################
##################################################### Start = 開始 分頁0
def Start():
    print ("\n*** Sta3213rt ***\n")

    
    t = [
        ' ====     AutoWeb 歡迎您     ==== ',
        ' ==== AutoWeb for WINDOWS OS ==== ',
        ' ====  ==== ',
        ' ==== 您好 請填寫您的 ATW密匙 再按 ENTER ==== ',
        ' ==== 恭賀新禧 ==== ',
        ' ==== 恭賀新禧 ==== ',
        'mokaki',
        'https://98672794.github.io/',
        '202202042044',
        ' ==== 恭賀新禧 ==== ',
        '1index.',
        '000 =\n    0000',
        '000 =\n    0000',
        '000 =\n    0000',
        '000 =\n    0000'
    ]
    for txt in t:
        print ("\n   ",txt,"\n")


    print ("\n*** /Start ***\n")

    ATW_OUT._OUT()





def St00art():

    #### ./ 在當前文件夾创工作目錄 if not ####
    NowJobFolder = ATWFolder._MakeJobFolder('_atw')
    # NowJobFolder = 文件夾 全路徑

    #### selenium chrome 配置 ####
    #                                             冇下載
    ATWSteChrome._SteChrome(NowJobFolder,'chrome')
    #                                             admin login whatsapp
    ATWSteChrome.chrome.get('https://98672794.github.io/')






















if __name__ == "__main__":
    Start()
    #README()







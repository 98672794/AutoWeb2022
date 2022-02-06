﻿

'''
winpy3

1index
執行Github中的.py
ATW20220204
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

'''

# -*- coding: UTF-8 -*-
##########################################################################import

import re
from getpass import getpass # 填寫密匙時將不會顯示


import ATWSteChrome
import ATWFolder
import ATWError
import ATWREADME
import ATW_LoginATW








###################################################################################
############################################################# 1index 說明
def README(): 
    ThisREADME = [
        '*** 1index.README ***', # PYfileName
        'Start() =\n        整緊',
        '000 =\n        000(000)',
        '000 =\n        000(000)',
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202051218',
        'https://98672794.github.io/'

    ]

    ATWREADME._READYourME(ThisREADME)














密匙檔路徑 = '_atw' #202202051729

#######################################################################
##################################################### Start = 開始 分頁0
def Start():

    try:
        Talk = [
            ' AutoWeb歡迎您',
            ' AutoWeb for WINDOWS OS',
            ' ****************************************** ',
            '        您必須小心保存您的 ATW密匙、ATW密文 ',
            '        任何人只要同時取得 ATW密匙、ATW密文 ',
            '                         ，即可取得所有資產 ',
            ' 您亦必須在可信的地方另外備份，以防意外丟失 ',
            '     因ATW密匙、ATW密文一旦丟失將永不能復原 ',
            '                     其所有資產也將永遠消失 ',
            ' ****************************************** ',
            ' 您好 請填寫您的 密匙 再按ENTER ',
            ' 為保您資產安全，填寫密匙時將不會顯示 ',
            ' ATW密文(0.atw)，必須存放在 _atw/0.atw ',
            ' ',
            ' 0 === Translation language \n',
            ' (任何字符) \n',
            '*** 最少8個字 ***\n'
        ]
        # 翻譯 all Talk
        #TalkToYou = ATWLanguage._AutoWeb翻譯功能(Talk,'en')    ##zh-Hant

        while True: # 驗答 loop
            for txt in Talk[0:-2]:
                print (txt)
            UserKey = getpass(prompt=Talk[-2]) # 寫密匙時將不會顯示
            # 少於8個字
            if len(UserKey) < 8:
                print(Talk[-1])
                continue    # 回驗答 loop
            break


        #### ./ 在當前文件夾创工作目錄 if not ####
        NowJobFolder = ATWFolder._MakeJobFolder(密匙檔路徑)
        # NowJobFolder = 文件夾 全路徑




        print('qqqqqqqqqqqq=')
        # 登入ATW
        ATW_LoginATW._LoginATW('ATWKeyname-@=',UserKey,NowJobFolder)     
        #   (v1,ATW密匙),sel,_UnLockATWv1,_UnLockATWv2,_UnLockATWsel)

        #########if YouAcTo == 'NewAc':

        print('qqqqqqqqqqqq=')
        ATWREADME.os.system("pause")

        # Goto _index
        #_index(UnLockData)


        ##############新言


    except Exception as e:
        ATWError._Error(e)
        ATWREADME.os.system("pause")
        pass































def St00art():

    #### ./ 在當前文件夾创工作目錄 if not ####
    NowJobFolder = ATWFolder._MakeJobFolder(密匙檔路徑)
    # NowJobFolder = 文件夾 全路徑

    #### selenium chrome 配置 ####
    #                                             冇下載
    ATWSteChrome._SteChrome(NowJobFolder,'chrome')
    #                                             admin login whatsapp
    ATWSteChrome.chrome.get('https://98672794.github.io/')






















if __name__ == "__main__":
    Start()
    ATWREADME.os.system("pause")












# -*- coding: UTF-8 -*-
#!/usr/bin/python


# import ATWTxtAndList    # List get txt 
#import ATWSteChrome
#import ATWFolder
import ATWError
import ATW2022
#import ATW_OUT
#import ATWREADME
import ATWLanguage  # 翻譯 




###################################################################################
############################################################# 0_Start_2022 說明
def README(): 
    ThisREADME = '''
win py3
            _\|/_
            (o o)
    +----oOO-{_}-OOo--------------------------+
    |                                         |
    |                                         |
    |        202202122151                     |
    |        this for start ATW2022.py        |
    |         ------------------------        |
    |         ------------------------        |
    |        202202112232                     |
    |        ATW2022.py                       |
    |        轉少少引用                       |
    |         ------------------------        |
    |        AutoWeb 202108031646 GODMOD      |
    |        完全修改唔到                     |
    |         ------------------------        |
    |        mokaki                           |
    |        https://98672794.github.io/      |
    |                                         |
    |                                         |
    |                                         |
    +----------------------------------------*/
    https://boxes.thomasjensen.com/examples.html


##################################### Folder Url
Now job
    ATWexe
        _atw         KeyFolder
            0.atw         coed
            job         自動搵fb
    _ATWpy
    _ATWhtml
    ..


##################################### Fun MAP
Import
README()
Start2022()
    ATW2022.InputData()
    _index(,)
        0
            ATWLanguage._AutoWeb翻譯功能()
            ATW2022._AutoWebKeySetting()
        3
            ATW2022._AutoWWebSales()

            

'''
    print(ThisREADME)




#######################################################################
##################################################### Start = 開始 分頁0
def Start2022():
    
    # ATW文件夾位置
    #KeyFolder2 = input('if you need make KeyFolder . pls inp FolderName')
    
    KeyFolder2 = input('AutoWeb 2022 歡迎您 pls enter ')
    if not KeyFolder2:  # 入空值
        KeyFolderName = '_atw'  #   _atw/0.atw 密匙檔路徑
    else:
        KeyFolderName = KeyFolder2

    try:
        #print('0_Start_2022=202202121828')
        d = ATW2022._2022_ATW_0_Start_2022ToATW2022InputData(KeyFolderName)
        _index(d[0],d[1])
    except Exception as e:
        for 异常 in ATWError._Error(e):
            print(异常)
        NowKO = 'Start() Run  = Error'
    # /
    return NowKO




































#################################################################### _index 選擇功能




Loop_AutoWWebSales = 0
def _index(v1,BassLan): 
    #global Loop_AutoWWebSales
    #BassLan = 'zh-Hant'

    Talk = '''
        ****************
    AutoWe index 歡迎您 
    請選擇功能

    0 ====== Auto Setting OK\n       修改您的資料
        ===
    2 ====== Auto WebPage template\n       自動下載mobanwang網頁模板(XXX維護中XXX)
    3 ====== Auto Get Job 2021 OK\n       自動獲取FACEBOOK公開群的相關廣告資料
        ===
        /****************
    '''

    while True:
        # 歡迎您

        # Goto Fun
        try:
            Goto = int(input(ATWLanguage._AutoWeb翻譯功能(Talk,BassLan)))
        except:
            print(ATWLanguage._AutoWeb翻譯功能('只可填寫數字',BassLan))
            continue

        if Goto == 0:   # if0=修改
            while True:
                print(ATWLanguage._AutoWeb翻譯功能('修改您的資料',BassLan))
                try:
                    Talk2 = '\n   請問您要修改?\n   0 === 語言\n   1 === 您的存檔\n\n'
                    sel_AutoWebSetting = int(input(ATWLanguage._AutoWeb翻譯功能(Talk2,BassLan)))
                except:
                    print(ATWLanguage._AutoWeb翻譯功能('只可填寫數字',BassLan))
                    continue
                if sel_AutoWebSetting == 0:
                    # 0 = 新用戶修改語言
                    新言 = ATWLanguage._AutoWebChangeLanguage(BassLan)   # 新言 = 目標語言
                    BassLan = 新言

                    # Start 轉 ATW2022 Language
                    print(ATW2022._2022_ATW_0_Start_2022ToATW2022bLanguageSetting(BassLan))
                    print(' Start 轉 ATW2022 Language 奉qqqq')

                    break
                if sel_AutoWebSetting == 1:
                    ATW2022._AutoWebKeySetting('','',v1)    #奉qqqqqqqqqqqqqqqqqqqq
                else:
                    continue    # not 0 1 re
                break   # 出if0=修改

        if Goto == 1:
            print('1on val 2131')
            continue

        if Goto == 2:
            #自動下載 MoBanWang 網頁模板
            print('Auto WebPage template 2021')
            print(ATWLanguage._AutoWeb翻譯功能('自動下載 MoBanWang 網頁模板\n   維護中。。。',BassLan))
            continue

        if Goto == 3:
            # AutoWeb Auto Get Job
            print('Auto Get Job 2021')
            print(ATWLanguage._AutoWeb翻譯功能('自動搵客，自動獲取FACEBOOK公開群的相關廣告資料',BassLan))
            # 驗證登入
            #UserKey = getpass(prompt=talk2+talk1+talk7)
            Loop_AutoWWebSales = 0
            ATW2022._AutoWWebSales(v1)    #奉qqqqqqqqqqqqqqqqqqqq
    
        continue    # 回歡迎您



































if __name__ == "__main__":
    while True: # Start loop for all
        #README()
        print(Start2022())  
        #ATW2022.os.system("pause")
        continue    # 回 Start loop








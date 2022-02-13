



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
import ATW自動下載模板2022  # 自動下載 MoBanWang 網頁模板 
import 自動覆客_OK2022  # whatsapp自動客服機器人


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
    _index(,,)
        0
            ATWLanguage._AutoWeb翻譯功能()
            ATW2022._AutoWebKeySetting()
        1

        2
            ATW自動下載模板2022._2022_ATW_0_Start_2022ToATW自動下載模板2022()   

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
        NowKO = _index(d[0],d[1],KeyFolderName)
    except Exception as e:
        for 异常 in ATWError._Error(e):
            print(异常)
        NowKO = 'Start() Run  = Error'
    # /
    return NowKO



































###################################################################################
#################################################################### _index 選擇功能




Loop_AutoWWebSales = 0
def _index(v1,BassLan,KeyFolderName): 
    #global Loop_AutoWWebSales
    #BassLan = 'zh-Hant'

        Talk = '''
            ****************
        AutoWe index 歡迎您 
        請選擇功能

        0 ====== Auto Setting \n       修改您的資料
        1 ====== Auto reply whatsapp\n       whatsapp自動客服機器人
        2 ====== Auto WebPage template\n       自動下載mobanwang網頁模板
        3 ====== Auto Get Job 2021 \n       自動獲取FACEBOOK公開群的相關廣告資料

        '''
    
        NowKO = 'Start() _index2022  = ok'
        while True: # 歡迎您
            # Goto Fun sel
            try:
                Goto = int(input(ATWLanguage._AutoWeb翻譯功能(Talk,BassLan)))
            except:
                print(ATWLanguage._AutoWeb翻譯功能('只可填寫數字',BassLan))
                continue

            if Goto == 0:   # 修改
                _indexIs0(v1,BassLan)
            if Goto == 1:   # whatsapp自動客服機器人
                _indexIs1(v1,BassLan)
            if Goto == 2:   # 自動下載 MoBanWang 網頁模板
                _indexIs2(BassLan,KeyFolderName)
            if Goto == 3:   # 自動搵客，自動獲取FACEBOOK公開群的相關廣告資料
                _indexIs3(v1,BassLan)
            continue    # 回歡迎您
        







# if0=修改
def _indexIs0(v1,BassLan): 
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
            break

        if sel_AutoWebSetting == 1:
            ATW2022._AutoWebKeySetting('','',v1)
        else:
            continue    # not 0 1 re
        break   # 出if0=修改

# whatsapp自動客服機器人
def _indexIs1(v1,BassLan): 
    print(ATWLanguage._AutoWeb翻譯功能('whatsapp自動客服機器人',BassLan))

    # 檢查 創 ATW User Key
    UserKeDemo = 自動覆客_OK2022._2022_AutoWhatsappReplyTextListKeyDemo
    UKS2 = _GetAllUserKey(v1,BassLan,'WhatsappAutoReplyTextList',UserKeDemo)
    
    # 1 ATW Login wts
    自動覆客_OK2022.AdminLoginWTS()
    
    # 2 ATW 等客Loop
    自動覆客_OK2022._2022startToLoop(UKS2)

    print('------------ / 不再回來 ------------------\n') 



# 自動下載 MoBanWang 網頁模板
def _indexIs2(BassLan,KeyFolderName): 
    print(ATWLanguage._AutoWeb翻譯功能('自動下載 MoBanWang 網頁模板',BassLan))
    OK = ATW自動下載模板2022._2022_ATW_0_Start_2022ToATW自動下載模板2022(KeyFolderName)   
    print('------------ /模板',OK,'已自動下載完成 ------------------\n') 


# 自動搵客，自動獲取FACEBOOK公開群的相關廣告資料
def _indexIs3(v1,BassLan): 
    # AutoWeb Auto Get Job
    print(ATWLanguage._AutoWeb翻譯功能('自動搵客，自動獲取FACEBOOK公開群的相關廣告資料',BassLan))
    # 驗證登入
    #UserKey = getpass(prompt=talk2+talk1+talk7)
    Loop_AutoWWebSales = 0
    ATW2022._AutoWWebSales(v1)  
    print('------------ /自動搵客2022 ------------------\n')  
    


































###################################################################################
#################################################################### _ATWLogin


# 檢查 ATW User Key 在否
def _GetAllUserKey(v1,BassLan,keyname,UserKeDemo): 

    Say0 = '''
    請填寫您的///
    如有多項請用 , 分隔。///
    '''

    Say_WhatsappAutoReplyTextList = '''
    請填寫您的///
    Whatsapp自動回覆信息內容///
    請用 ',' 分開每項 和 用 @@ 代替換行///
    '''

    dot = '\n********** User Key Demo ************\n'
    
    keynameBB = keyname + '-@='     # 合 keyname


    # 各 keyname 不同說明
    if keyname == 'WhatsappAutoReplyTextList':
        Say = Say_WhatsappAutoReplyTextList
        Say99 = (ATWLanguage._AutoWeb翻譯功能(Say,BassLan)).split('///') 
        tk2 = Say99[0]+Say99[1]+Say99[2]
    else:
        Say = Say0
        Say99 = (ATWLanguage._AutoWeb翻譯功能(Say,BassLan)).split('///') 
        tk2 = Say99[0]+keyname+Say99[1]

    while True: 
        ATW2022._LoginATW(keynameBB,v1) # 取 UnLockData
        if ATW2022.UnLockData == '沒有NODATA內容':
            # go to set
            NewKeyVal = input(dot+UserKeDemo+dot+tk2)
            # del " '
            NewKeyVal = NewKeyVal.replace("'", "").replace('"', '').replace(' ', '')
            ATW2022._AutoWebKeySetting(keynameBB,NewKeyVal,v1)
            continue
        break
    
    return ATW2022.UnLockData
































if __name__ == "__main__":
    while True: # Start loop for all
        #README()
        print(Start2022())  
        #ATW2022.os.system("pause")
        continue    # 回 Start loop








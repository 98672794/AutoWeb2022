


'''
            _\|/_
            (o o)
    +----oOO-{_}-OOo--------------------------+
    |                                         |
    |        但冇 reture 點算                                 |
    |        win py3                          |
    |        AutoWeb 202108031646 GODMOD      |
    |        完全修改唔到                       |
    |                                         |
    |        ATW2022.py 202202080051          |
    |        轉少少引用                        |
    |                                         |
    |                                         |
    |       mokaki                            |
    |        https://98672794.github.io/      |
    |                                         |
    |                                         |
    |                                         |
    +----------------------------------------*/
    https://boxes.thomasjensen.com/examples.html



##################################### Folder Url
ATWexe
    _atw  - |0.atw / coed    KeyFolder 
            |--.py
            |--.html
            |--.job



##################################### Fun MAP
Import
Data
InputData()
    _AutoWebLanguageSetting()
    _SetFolder()
    _LoginATW()
    if 自動搵客.py:
        _AutoWWebSales()
    else:
        _index() admin
            if 0:
                _AutoWebKeySetting()    修改您的資料
            if 1:   qqqqqq 隱
                _AutoImportinputData()  自动安装所需的Python依赖包
            if 2:
                00000()             自動下載 MoBanWang 網頁模板
            if 3:
                _AutoWWebSales()    自動搵客
            if 4: qqqqqq 隱
                _InputChromeAutoUpData()    自动下載最新chromedriver
            if 5: qqqqqqqqqqq
                _VIPUser()      開始自动生成VIP驗證碼
    _MakeTalk()     製talk





'''
# -*- coding: UTF-8 -*-




# Import###########################################################################
###################################################################################
import os
import requests
import urllib
import sys
import hashlib
import urllib.request
from urllib.request import urlretrieve
import time
from PyClassicRound import classic_round
import rarfile
import io
from PIL import Image
from threading import *
from fontTools.ttLib import TTFont
import binascii
import datetime
import re
import random
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import json
import logging
import zipfile
from win32com import client as wincom_client
from getpass import getpass
from zhon.hanzi import punctuation
import copy
import arrow
from deep_translator import (GoogleTranslator,PonsTranslator,LingueeTranslator,MyMemoryTranslator,YandexTranslator,DeepL,QCRI,single_detection,batch_detection)

# ATW2022
import ATWLanguage  # 翻譯 
import ATWError




# Data ###########################################################################
# 今日 各用途
today = datetime.datetime.today()
nowtime = arrow.now()   





# talk頭尾分格
Talk0 = '\n   ' 
TalkEND = '\n\n'
AllTalk0 = '\n   ===================\n'

# 设置翻译
UserLanguage = 'zh-Hant'
LanguageText = '您好'

# 官方FB群
ATWOwnFBGroups = 'groups/186019250178867'
























# 2022 ########################################################################
###############################################################################

# AutoWeb 2022 入口 setKeyFolder 填寫ATW密匙    ################################
def _2022_ATW_0_Start_2022ToATW2022InputData(Start2022KeyFolderName): 
    global KeyFolder
    
    try:

        KeyFolder = Start2022KeyFolderName
        #print('KeyFolder=',KeyFolder)
        #_OUT()
        NowKO = InputData()
    except Exception as e:
        for 异常 in ATWError._Error(e):
            print(异常)
        NowKO = 'Error'
    # /
    return NowKO





# 翻譯功能 0_Start_2022 to ATW2022 ###########################################
def _2022_ATW_0_Start_2022ToATW2022bLanguageSetting(新言): 
    global UserLanguage
    UserLanguage = 新言
    return 





















# UserUI###########################################################################
###################################################################################
########################################################## AutoWeb 入口 填寫 ATW密匙

# 唔好攪人啦
talk2 = '   ATW密文(0.atw)，必須存放在_atw/0.atw    \n\n'

talk3 = '   ** 您必須小心保存您的 ATW密匙、ATW密文 。\n'
talk4 = '      任何人使用 ATW密匙、ATW密文 打開本程式，\n      就可操作帳戶內的所有資產，無需其他驗證。\n\n'
talk5 = '   ** 您必須在可信的地方另外備份，以防意外丟失 。\n'
talk6 = '      因ATW密匙、ATW密文一旦丟失將永不能復原，\n      其內所有資產也將永遠消失 。\n\n'


talk1 = '  ===== 您好 請填寫您的 ATW密匙 再按 ENTER =====\n   (任何字符)\n\n'
talk7 = '   為保您資產安全，填寫密匙時將不會顯示   \n'
talk8 = 'AutoWeb 2022 歡迎您\n*** just for WINDOWS OS ***\n'
talk9 = '*** 只可填寫數字 ***\n'
talk10 = '\n   0 === Translation language (原文:zh-Hant) \n'
talk11 = '*** 最少8個字 ***\n'

# 202202080021 唔需要重做 利用一切
KeyFolder = '_atw'
KeyUrl = KeyFolder + '/0.atw'  #AutoWeb/0.atw
def InputData():  # InputData(密匙檔路徑2022)
    global KeyFolder
    global UserLanguage
    # 0Start2022 
    #KeyFolder = 密匙檔路徑2022

    _AutoWebLanguageSetting(talk8)
    print(LanguageText)

    # AutoImport
    #_AutoImportinputData('AutoWeb20210717.py')   #   (需安装Python依赖包的文件名./*.py)

    _AutoWebLanguageSetting(talk2+talk3+talk4+talk5+talk6+talk1+talk7+talk10)
    UserKey = getpass(prompt=LanguageText+AllTalk0)

    # 新用戶修改語言
    if UserKey == '0':
        #_AutoWebLanguageSetting(0)
        # ATW2022
        # 新言 = 目標語言
        UserLanguage = ATWLanguage._AutoWebChangeLanguage('zh-Hant') 
    else:
        if len(UserKey) < 8:
            _AutoWebLanguageSetting(talk11)
            print(LanguageText)
            InputData()

    # 文件夾位置
    #KeyFolder2 = input('\n請填寫您要建立的工作環境名稱(任何文字)(創文件夾)\n')
    #KeyFolder = KeyFolder2

    # 查 文件夾 在否       ./NOW
    _SetFolder(KeyFolder,'MakeFolder')    #   (文件夾名,動作)
    
    # 登入ATW
    _LoginATW('ATWKeyname-@=',UserKey)     #   (v1,ATW密匙),sel,_UnLockATWv1,_UnLockATWv2,_UnLockATWsel)

    # 執行本.py時才咁行
    # 其他py就可以引用InputData()
    if __name__=='__main__':
        # Goto
        if ThisPy == '自動搵客.py': # 客戶版ATW = 自動搵客.py
            _AutoWWebSales(UserKey)
        else:                       #   adminATW
            # Goto _index
            _index(UnLockData)


    # ATW2022
    return UnLockData, UserLanguage
    # Exp: to index
    # ATW2022._index(ATW2022.InputData())












#################################################################### _index 選擇功能
indexTalk7 = '\n   =========== AutoWeb index 歡迎您 ==========='
indexTalk0 = '\n   請選擇功能\n'
indexTalk1 = '\n   0 ====== Auto Setting\n   修改您的資料\n'
indexTalk2 = '\n   1 ====== Auto pip Import\n   自动安装所需的Python依赖包（pip install 包）\n'
indexTalk3 = '\n   2 ====== Auto WebPage template\n   自動下載mobanwang網頁模板(XXX維護中XXX)\n'
indexTalk4 = '\n   3 ====== Auto Sales\n   自動搵客，自動獲取工作相關的廣告資料\n'
indexTalk5 = '\n   4 ====== Auto chromedriver\n   自动下載最新 chromedriver\n'
indexTalk6 = '\n   5 ====== VIP KEY[ADMIN]\n   自动生成VIP驗證碼\n'
Loop_AutoWWebSales = 0
def _index(v1): 
    global Loop_AutoWWebSales
    while True:
        # 歡迎您

        _AutoWebLanguageSetting(indexTalk7)
        print (LanguageText)

        # Goto Fun
        try:
            _AutoWebLanguageSetting(indexTalk0+indexTalk1+indexTalk2+indexTalk3+indexTalk4+indexTalk5+indexTalk6)    
            Goto = int(input(Talk0+LanguageText+AllTalk0))
        except:
            _AutoWebLanguageSetting(talk9)
            print(LanguageText)
            continue

        if Goto == 0:
            while True:
                _AutoWebLanguageSetting ('\n   修改您的資料\n')
                print(Talk0+LanguageText)
                try:
                    _AutoWebLanguageSetting ('\n   請問您要修改?\n   0 === 語言\n   1 === 您的存檔\n\n')
                    sel_AutoWebSetting = int(input(Talk0+LanguageText+AllTalk0))
                except:
                    _AutoWebLanguageSetting(talk9)
                    print(LanguageText)
                    continue
                if sel_AutoWebSetting == 0:
                    _AutoWebLanguageSetting(0)
                if sel_AutoWebSetting == 1:
                    _AutoWebKeySetting('','',v1)
                else:
                    continue
                break

        if Goto == 1:
            _AutoWebLanguageSetting('\n   自动安装所需的Python依赖包\n')
            print (Talk0+LanguageText+AllTalk0)
            _AutoImportinputData()

        if Goto == 2:
            #自動下載 MoBanWang 網頁模板
            _AutoWebLanguageSetting ('\n   自動下載 MoBanWang 網頁模板\n')
            print (Talk0+LanguageText+AllTalk0)
            _AutoWebLanguageSetting ('\n   維護中。。。\n')
            print (Talk0+LanguageText+AllTalk0)
            continue

        if Goto == 3:
            # AutoWeb 自動搵客
            _AutoWebLanguageSetting ('\n   自動搵客\n')
            print (Talk0+LanguageText+AllTalk0)
            # 驗證登入
            #UserKey = getpass(prompt=talk2+talk1+talk7)

            while True:
                Loop_AutoWWebSales = 0
                try:
                    _AutoWebLanguageSetting('無限循環\n   0 === 無限循環\n   1 === 循環一次')
                    LoopSet = int(input(Talk0+LanguageText+AllTalk0))
                except:
                    _AutoWebLanguageSetting(talk9)
                    print (Talk0+LanguageText+AllTalk0)
                    continue

                if LoopSet == 0:
                    Loop_AutoWWebSales = 'LOOP'
                if LoopSet == 2:
                    print ('\n*** ADMIN 模式 ***\n')
                    Loop_AutoWWebSales = 'ADMIN'
                _AutoWWebSales(v1)
                break

        if Goto == 4:
            # AutoWeb 自动下載最新chromedriver OK
            #ATPYn = input('*****您好\n***請填寫下載 chromedriver 後存放的路徑，如:\n.\AutoWeb\n如沒填寫將使用您的工作環境文件夾',KeyFolder,'\n')
            
            #if chromedriverURL == '':
            #    chromedriverURL = KeyFolder
            chromedriverURL = KeyFolder
            _AutoWebLanguageSetting ('\  ===== 開始下載最新 chromedriver ===== \n')
            print (Talk0+LanguageText+AllTalk0)
            _InputChromeAutoUpData(chromedriverURL)

        if Goto == 5:
            print ('\  ===== 開始自动生成VIP驗證碼 ===== \n')
            VIPName = input('\n   請填寫VIP名稱\n')
            _VIPUser(VIPName,v1,'ADMIN')


        continue




_AutoWWebSettingTalk0 = '請填寫您要修改或增加的ATWKey，如:\n   ATWFacebookGroupsURL("-@="不用填寫)\n'
_AutoWWebSettingTalk1 = '不能修改\n'
_AutoWWebSettingTalk4 = '\n   0 ====== 退出\n'
_AutoWWebSettingTalk6 = '\nhttps://www.facebook.com/groups/2553682591549795,groups/1230482576964177,groups/flycan.webdesign,\n'

_AutoWWebSettingTalk7d = '未有用不能刪'
_AutoWWebSettingTalk8a = 'groups/\n'
_AutoWWebSettingTalk15b = ' " '
_AutoWWebSettingTalk15c = " ' \n"


















#################################################################### 修改您的資料 #
def _MakeTalk(): 
    global ATW_LS96


    _AutoWWebSettingTalk2 = '\n   請填寫新的值\n'


    _AutoWWebSettingTalk5 = '\n請填寫您的Facebook群組網址，如:\n'
    _AutoWWebSettingTalk7a = '\n   ***請用'
    _AutoWWebSettingTalk7b = '分開每一項'
    _AutoWWebSettingTalk7c = '未有用不能刪'

    _AutoWWebSettingTalk8 = '\n   *** 必需有 '

    _AutoWWebSettingTalk9 = '\n請填寫您的Facebook群組尋帖 1級關鍵字，如:\n'
    _AutoWWebSettingTalk10 = '\n徵求,發案,任務,誠徵,尋找,請問有,外快,looking for,需要,i need,we need,need a,required\n'

    _AutoWWebSettingTalk11 = '\n請填寫您的 Facebook群組尋帖 2級關鍵字，如:\n'
    _AutoWWebSettingTalk12 = '\n區塊鏈,Dapp,智能合約,erc721,ERC20,APP,直播,web,網站,網頁,website,web designer,Application,E-commerce,ecommerce\n'

    _AutoWWebSettingTalk13 = '\n請填寫您的 Facebook群組尋帖 負關鍵字(帖有將忽略)，如:\n'
    _AutoWWebSettingTalk14 = '\n徵才,我要接案,全職\n'

    _AutoWWebSettingTalk15a = '\n   XXX 不能有 '


    _AutoWWebSettingTalk16 = '\n請填寫 Facebook群組尋帖 的最後日期(- 月)'
    _AutoWWebSettingTalk17 = '(最少 1 個月) 。\n'

    #                                       0                       1                           2                           3                           4                           5                           6                               7                               8                           9                       10                              11                              12                      13                          14                   15 
    _AutoWebLanguageSetting(_AutoWWebSettingTalk5+'==='+_AutoWWebSettingTalk7a+'==='+_AutoWWebSettingTalk7b+'==='+_AutoWWebSettingTalk7c+'==='+_AutoWWebSettingTalk8+'==='+_AutoWWebSettingTalk15a+'==='+_AutoWWebSettingTalk9+'==='+_AutoWWebSettingTalk10+'==='+_AutoWWebSettingTalk11+'==='+_AutoWWebSettingTalk12+'==='+_AutoWWebSettingTalk13+'==='+_AutoWWebSettingTalk14+'==='+_AutoWWebSettingTalk2+'==='+_AutoWWebSettingTalk16+'==='+_AutoWWebSettingTalk17+'==='+talk9)
    _StrToList(LanguageText,'===')
    ATW_LS96=copy.deepcopy(TrueList)



#################################################################### 修改您的資料 #
def _AutoWebKeySetting(ATWKeyName,ATWKeyVlo,UserKey): 

    _MakeTalk()

    # 取 ALL Data
    _LoginATW('ALL',UserKey)
    AllYourData = UnLockData
    _StrToList(UnLockData,'\n')
    #AllYourDataList = TrueList
    AllYourDataList=copy.deepcopy(TrueList)

    # 加新Key
    if ATWKeyName != '':
        # list 轉字
        NewData = '\n'.join(str(e) for e in AllYourDataList)
        # 取所有舊內容
        #_LoginATW('ALL',UserKey)
        # 加新內容1/2
        Dt = str(NewData+ATWKeyName)
        # 取Key256
        _LoginATW('ATWKey256-@=',UserKey)
        # 加新內容2/2
        _SaveData(UnLockData,Dt,ATWKeyVlo,'0.atw')

    # SettingKey
    else:

        while True:
            list = ['ATWKeyname','ATWKey256','ATWUserSeleniumUserAgent','ATWFacebookAc','ATWUserFBName','ATWUserSeleniuWindowSiz']
            # 查看 ALL Data
            print ('All Your Data=\n\n'+str(AllYourDataList).replace("', '", "\n\n").replace("['", "").replace("']", ""))
            print (AllTalk0)

            # 填寫ATW NewKey
            _AutoWebLanguageSetting (_AutoWWebSettingTalk0+'\n'+str(list)+_AutoWWebSettingTalk1+_AutoWWebSettingTalk4+AllTalk0)
            AutoWWebSettingInput = input(Talk0+LanguageText+AllTalk0)

            # 不能修改
            if AutoWWebSettingInput in list:

                _AutoWebLanguageSetting (_AutoWWebSettingTalk1)
                print (Talk0+str(list)+LanguageText+AllTalk0)
                _AutoWebKeySetting('','',UserKey)

            # 0======退出_AutoWWebSetting
            if AutoWWebSettingInput == '0':
                InputData()




            # 填寫新的值 index
            if AutoWWebSettingInput == 'ATWFacebookGroupsURL':  # 修改fb群Url
                NewVlo = input(Talk0+ATW_LS96[0]+_AutoWWebSettingTalk6+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[4]+_AutoWWebSettingTalk8a+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)


            elif AutoWWebSettingInput == 'ATWFbPostkeyword1':      # 修改fb尋帖 1級關鍵字
                NewVlo = input(AllTalk0+ATW_LS96[6]+ATW_LS96[7]+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)


            elif AutoWWebSettingInput == 'ATWFbPostkeyword2':      # 修改fb尋帖 1級關鍵字
                NewVlo = input(AllTalk0+ATW_LS96[8]+ATW_LS96[9]+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)


            elif AutoWWebSettingInput == 'ATWFbPostNoKeyword':      # 修改fb尋帖 負關鍵字
                NewVlo = input(AllTalk0+ATW_LS96[10]+ATW_LS96[11]+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)
            


            elif AutoWWebSettingInput == 'ATWListTime':      # 修改fb尋帖 最後日期
                NewVlo = input(AllTalk0+ATW_LS96[13]+AllTalk0)
                # 刪除 NewVlo 不能出現的字付
                _AutoWebKeySettingDelTxt(AutoWWebSettingInput,NewVlo)
                NewVlo = NewVlo000





            # 不能空值
            if NewVlo == '':
                _AutoWebLanguageSetting ('\n*****沒有值 =====\n')
                print (Talk0+LanguageText+AllTalk0)
                continue
            #else:
            break

        # 刪除 NewVlo 不能出現的字付
        _AutoWebKeySettingDelTxt(AutoWWebSettingInput,NewVlo)
        NewVlo = NewVlo000



        # 刪除原項 如有
        i = 0
        while i < len(AllYourDataList):
            if AutoWWebSettingInput in AllYourDataList[i]:
                AllYourDataList.pop(i)
            i+=1

        # list 轉字
        NewData = '\n'.join(str(e) for e in AllYourDataList)
        # 加新內容1/2
        NewDataToSave = NewData+AutoWWebSettingInput+'-@='
        # 取Key256
        _LoginATW('ATWKey256-@=',UserKey)
        # 加新內容2/2
        _SaveData(UnLockData,NewDataToSave,NewVlo,'0.atw')

        _AutoWebLanguageSetting ('\n*****已記錄新值 =====\n')
        print (Talk0+LanguageText+AllTalk0)
        _AutoWebKeySetting('','',UserKey)



# UserUI ##########################################################################
################################################################################END














# 翻譯功能 ##########################################################################
def _AutoWebLanguageSetting(uk): 
    global UserLanguage
    global LanguageText
    #print ("*** _AutoWebLanguageSetting ***\n")

    if uk == 0:
        # 修改語言
        #print ('\n 修改語言 \n')


        while True: 
        # 取 UserLanguage
            _AutoWebLanguageSetting('您好 請直接填寫您語言之中的任何一個單詞，如: ')
            InputYourLanguage = input(Talk0+LanguageText+'语言,您好,Hello,こんにちは,สวัสดี...'+TalkEND)

            # 不能數字
            NoNb0 = []
            NoNb = [1,2,3,4,5,6,7,8,9,0]
            NoNb1 = []
            i = 0
            while i < len(InputYourLanguage):
                NoNb0.append(InputYourLanguage[i])
                i+=1
            NoNb1.clear()
            for nb in NoNb:
                for word in NoNb0:
                    word,nb = str(word),str(nb)
                    if word in nb:
                        NoNb1.append(word)
            if NoNb1:
                _AutoWebLanguageSetting('XXX 不能用數字 XXX\n')
                print (Talk0+LanguageText+AllTalk0)
                continue
            if InputYourLanguage == '':
                _AutoWebLanguageSetting('XXX 不能空值 XXX\n')
                print (Talk0+LanguageText+AllTalk0)
                continue
            break
        
        # 轉 UserLanguage
        try:
            # https://deep-translator.readthedocs.io/en/latest/usage.html#language-detection
            UserLanguage = single_detection(InputYourLanguage, api_key='1521de38ddf080ba292f64dfe40a0438')
            YourLanguage1 = '已經轉換您的語言   '+UserLanguage+'\n   0 === 保存\n   1 === 重新修改語言\n\n'
            _AutoWebLanguageSetting(YourLanguage1)

            # Goto
            InputYourLanguageGoto = input(Talk0+LanguageText+TalkEND)
            if InputYourLanguageGoto == '0':
                InputData()
            else:
                _AutoWebLanguageSetting(0)
        except:
            # 不支持
            print ('XXX This Language [',InputYourLanguage,'] cannot be used XXX\n change Language to [EN] ')
            UserLanguage = 'en'
            _AutoWebLanguageSetting(0) 
    else:
        #print ('=翻譯句子= \n[',uk,']\n--------------------------\n')
        # 翻譯句子
        if UserLanguage != 'zh-Hant':
            LanguageText = GoogleTranslator(source='auto', target=UserLanguage).translate(uk) 
        else:
            # 繁中不需
            LanguageText = uk















































































# 可選功能##########################################################################


###################################################################################
################################################################# 刪除所有中英符號
NoPunctuation = 0
def _DelPunctuation(txt): 
    global NoPunctuation

    DelEnPunctuation='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！，]+'
    txtB=re.sub(DelEnPunctuation,'',str(txt))

    punctuation_str = punctuation
    for i in punctuation:
        NoPunctuation = txtB.replace(i, '')











###################################################################################
################################################################# AutoWeb 生成文件夾
def _SetFolder(v1,sel):     #   (文件夾名,動作)
    #print ('_SetFolder\n'+ str(v1) +'\n')
    
    # MakeFolder = MakeFolder
    if sel == 'MakeFolder':
        # 查 文件夾 在否       ./NOW
        folder = os.path.exists(v1)
        if not folder:
            os.makedirs(v1)    # makedirs　文件夾不在创，在ＥＲＲＯＲ
            _AutoWebLanguageSetting("\n***!!成功创建文件夾!!!!!*****\n")
            print (Talk0,LanguageText,v1)











###################################################################################
################################################################### AutoWeb 加密解密
tttKey = 0
#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#密碼生成
def _ChgCodeAll(Key,ttt,nb):     #   (sha256Key,加密內容,動作)
    global tttKey
    #print (str(nb) +'ttt\n'+ ttt +'\n')

    # 加密
    if nb == 256:
        # Key 轉 不可解 sha256     https://blog.csdn.net/qq_38161040/article/details/103963756
        tttKey = hashlib.sha256(ttt.encode('utf-8')).hexdigest()
    
    if nb == 16:
        # binascii加密   可解  https://blog.csdn.net/weixin_42575020/article/details/107788550
        tttKey = binascii.b2a_hex(ttt.encode())

    if nb == 3:
        #刪PY廢字
        tttKey22 = str(ttt)
        tttKey33 = tttKey22[2:-1]

        #加密3 偽隨機打亂
        tkl = len(tttKey33)                 #   加密後內容字數
        tkl2 = math.ceil(tkl / 2)           #   加密後內容字數/2
        N = int(random.uniform(0, tkl2))    #   N = 0 ~ 加密後內容字數/2
        M = int(random.uniform(tkl2, tkl))  #   M = 加密後內容字數/2 ~ 加密後內容字數
        if (N % 2) == 0:
            sk1 = Key[:32]
            sk2 = Key[32:]
        else:
            sk2 = Key[:32]
            sk1 = Key[32:]
        # tttKey44 = 16Key + sha256Key1 + 16Key2 + sha256Key2 + 16Key3
        tttKey = tttKey33[:N] + sk1 + tttKey33[N:M] + sk2 + tttKey33[M:]
        '''
        print ('16加密後\n'+ str(tttKey33) +'\n')
        print ('sha256Key\n'+ str(sk1) +'\n')
        print ('sha256Key\n'+ str(sk2) +'\n')
        print ('tttKey1\n'+ str(tttKey33[:N]) +'\n')    
        print ('tttKey2\n'+ str(tttKey33[N:M]) +'\n')
        print ('tttKey3\n'+ str(tttKey33[M:]) +'\n')
        print ('tttKey44\n'+ str(tttKey44) +'\n')
        '''

    # 解密
    if nb == 30:    
        #解密3    偽隨機打亂
        sk2 = str(Key[:32])
        sk1 = str(Key[32:])
        tttKey = ttt.replace(sk1, '').replace(sk2, '')

    if nb == 160:    
        #binascii解密
        tttKey = binascii.a2b_hex(ttt).decode()

    #print (str(nb) ,'tttKey\n', tttKey ,'---\n')











###################################################################################
################################################## AutoWeb 自动安装所需的Python依赖包
# https://github.com/cuntou0906/pipUtils
# input路径名称
def _AutoImportinputData():   #   (需安装Python依赖包的文件名./*.py)

    # 找出現在目錄所有.py
    PYList = [] 
    ss = os.listdir(".")
    for item in ss: 
        if(item.endswith('.py')):
            PYList.append(item)
    i = 0
    while i < len(PYList):
        print('   ',i,'=====',PYList[i],'\n')
        i+=1

    while True:
        _AutoWebLanguageSetting('\n   請填寫您需安装Python依赖包的文件號\n   或直接填寫文件名和路徑，如 ./path.py\n')
        ImportPyUrl = input(Talk0+LanguageText+AllTalk0)
        # 不能空值
        if ImportPyUrl == '':
            continue
        # 查 ImportPyUrl 是否 int
        try:
            ImportPyUrl = PYList[int(ImportPyUrl)]
            break
        except:
            break

    if not os.path.isfile(ImportPyUrl):
        _AutoWebLanguageSetting('不存在，請從試***')
        print ('\n   *** ',ImportPyUrl,LanguageText,AllTalk0)
        InputData()

    _AutoWebLanguageSetting(' 安装依赖包\n')
    print (ImportPyUrl,LanguageText,AllTalk0)

    # UP自己時try XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    _AutoWebLanguageSetting('   請填寫Import的行(由,至)，如 5,15')
    lines = input(Talk0+LanguageText+AllTalk0)
    l1 = (lines.split(",")[0])
    l2 = (lines.split(",")[1])

    # Import的行(由,至)
    PackageName = _getpackage(ImportPyUrl,l1,l2)
    print(PackageName)

    PackageName = ['opencv-python' if i =='cv2' else i for i in PackageName]

    ###########


    PackageName = list(set(PackageName))   # 去除重复的包名
    _AutoWebLanguageSetting("所需安装的包：")
    print(Talk0,LanguageText,PackageName)
    _AutoWebLanguageSetting("总共需要安装數  ")
    print(Talk0,LanguageText,len(PackageName))

    ###########

    jingxiangstr = "https://pypi.tuna.tsinghua.edu.cn/simple/"  # 镜像源
    for index in range(len(PackageName)):

        comand = "pip install " + PackageName[index] +" -i "+jingxiangstr
        # 正在安装
        _AutoWebLanguageSetting("正在安装")
        print("------------------" + LanguageText + str(PackageName[index]) + " ----------------------")
        print(comand + "\n")
        os.system(comand)

    os.system("pip list")    # 显示所有的包

def _getpackage(path,lines1,lines2):
    # 以只读模式打开文件，如果打开失败有error输出
    index = 1
    PackageName = []
    try:
        f = open(path, 'r',encoding='UTF-8')
        while(1):
            if index>=int(lines1):
                if index<=int(lines2):
                    str = f.readline()
                    # print("当前第",index,"行：",str)
                    strsplit = str.split()    # 分割字符串
                    # try內配合pipUtils5.0.py轉換
                    try:
                        str2 = strsplit[1]
                        loc = str2.find(".")   # 找到 . 的位置
                        if loc==-1:
                            PackageName.append(str2)
                        else:
                            PackageName.append(str2[0:loc])
                    except:
                        print ('\n***************** =====\n')
                    pass
                else:
                    break
            else:
                str = f.readline()
            pass
            index = index + 1
    # 要用finally来关闭文件！
    finally:
        if f:
            f.close()
            pass
        pass
    return PackageName











###################################################################################
################################################## AutoWeb 自动下載最新 chromedriver
# https://medium.com/drunk-wis/python-selenium-chrome-browser-%E8%88%87-driver-%E6%83%B1%E4%BA%BA%E7%9A%84%E7%89%88%E6%9C%AC%E7%AE%A1%E7%90%86-cbaf1d1861ce

ii0 = 0
ChmExUrl0 = 0
# chrome_helper.py
CHROME_DRIVER_BASE_URL = "https://chromedriver.storage.googleapis.com"
#CHROME_DRIVER_FOLDER = ii0    # chromedriver 存放路徑
CHROME_DRIVER_MAPPING_FILE = r"{}\mapping.json".format(ii0)
CHROME_DRIVER_EXE = r"{}\chromedriver.exe".format(ii0)
CHROME_DRIVER_ZIP = r"{}\chromedriver_win32.zip".format(ii0)
def _InputChromeAutoUpData(chromedriverURL):    #   (保存chromedriver的路徑)
    global ii0
    global ChmExUrl0
    #print ('_SetFolder\n'+ str(v1) +'\n')

    # chromedriver 存放路徑
    #tt2 = '*****您好\n***請填寫下載 chromedriver 後存放的路徑，如:\n.\AutoWeb\n'
    #ii0 = input(tt2)
    ii0 = chromedriverURL
    
    # _SetFolder
    _SetFolder(ii0,'MakeFolder')   #   (文件夾名,動作)

    tt2 = '***請填寫您的 chrome.exe 路徑，如:'
    tt9 = '***您的chrome.exe不存在***'
    # 驗查 chrome.exe 位置
    ChmExUrl1 = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    ChmExUrl2 = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    if os.path.isfile(ChmExUrl1):
        #print ('ChmExUrl1\n'+ str(ChmExUrl1) +'\n')
        ChmExUrl0 = ChmExUrl1
    else:
        if os.path.isfile(ChmExUrl2):
            #print ('ChmExUrl2\n'+ str(ChmExUrl2) +'\n')
            ChmExUrl0 = ChmExUrl2
        else:
            # 都沒 = input loop 至有
            while True:
                _AutoWebLanguageSetting(tt9)
                print (Talk0+LanguageText+AllTalk0)
                _AutoWebLanguageSetting(tt2)
                ii1 = input(Talk0+LanguageText+ChmExUrl1+ChmExUrl2)
                try:
                    print ('\n'+ str(ii1) +'\n')
                    if os.path.isfile(ii1):
                        ChmExUrl0 = ii1
                except:
                    continue
                else:
                    break
    # Run
    check_browser_driver_available()

def get_chrome_driver_major_version():
    chrome_browser_path = ChmExUrl0     #chrome.exe 位置
    chrome_ver = get_file_version(chrome_browser_path)
    chrome_major_ver = chrome_ver.split(".")[0]
    return chrome_major_ver

def get_latest_driver_version(browser_ver):
    latest_api = "{}/LATEST_RELEASE_{}".format(
        CHROME_DRIVER_BASE_URL, browser_ver)
    resp = requests.get(latest_api)
    lastest_driver_version = resp.text.strip()
    return lastest_driver_version

def download_driver(driver_ver, dest_folder):
    download_api = "{}/{}/chromedriver_win32.zip".format(
        CHROME_DRIVER_BASE_URL, driver_ver)
    dest_path = os.path.join(dest_folder, os.path.basename(download_api))
    resp = requests.get(download_api, stream=True, timeout=300)

    if resp.status_code == 200:
        with open(dest_path, "wb") as f:
            f.write(resp.content)
        logging.info("Download driver completed")
    else:
        raise Exception("Download chrome driver failed")

def unzip_driver_to_target_path(src_file, dest_path):
    with zipfile.ZipFile(src_file, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
    logging.info("Unzip [{}] -> [{}]".format(src_file, dest_path))

def read_driver_mapping_file():
    driver_mapping_dict = {}
    if os.path.exists(CHROME_DRIVER_MAPPING_FILE):
        driver_mapping_dict = read_json(CHROME_DRIVER_MAPPING_FILE)
    return driver_mapping_dict

def check_browser_driver_available():
    chrome_major_ver = get_chrome_driver_major_version()
    mapping_dict = read_driver_mapping_file()
    driver_ver = get_latest_driver_version(chrome_major_ver)

    if chrome_major_ver not in mapping_dict:
        download_driver(driver_ver, ii0)
        unzip_driver_to_target_path(r'{}/chromedriver_win32.zip'.format(ii0), ii0)

        mapping_dict = {
            chrome_major_ver: {
                "driver_path": CHROME_DRIVER_EXE,
                "driver_version": driver_ver
            }
        }
        
        # 下載完 Del zip
        os.remove(r'{}/chromedriver_win32.zip'.format(ii0))
        _AutoWebLanguageSetting('已經下載到===文件夾中')
        _StrToList(LanguageText,'===')

        print ("\n***!!chromedriver",TrueList[0],ii0,TrueList[1],"!!!!!*****\n")

        mapping_dict.update(mapping_dict)
        #write_json(CHROME_DRIVER_MAPPING_FILE, mapping_dict)

# file_util.py
def get_file_version(file_path):
    logging.info('Get file version of [%s]', file_path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("{!r} is not found.".format(file_path))

    wincom_obj = wincom_client.Dispatch('Scripting.FileSystemObject')
    version = wincom_obj.GetFileVersion(file_path)
    logging.info('The file version of [%s] is %s', file_path, version)
    return version.strip()

def read_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data



# 可選功能##########################################################################
################################################################################END
















































































































'''

       /\          /\          /\
    /\//\\/\    /\//\\/\    /\//\\/\
 /\//\\\///\\/\//\\\///\\/\//\\\///\\/\
//\\\//\/\\///\\\//\/\\///\\\//\/\\///\\
\\//\/                            \/\\//
 \/                                  \/
 /\                                  /\
//\\         _AutoWWebSales         //\\
\\//                                \\//
 \/                                  \/
 /\                                  /\
//\\/\                            /\//\\
\\///\\/\//\\\///\\/\//\\\///\\/\//\\\//
 \/\\///\\\//\/\\///\\\//\/\\///\\\//\/
    \/\\//\/    \/\\//\/    \/\\//\/
       \/          \/          \/
'''



# _AutoWWebSales###################################################################
###################################################################################
def _AutoWWebSales(UserKey):
    
    # 香港政府一站通 搜尋結果 https://www.search.gov.hk/result?query=%E6%8B%9B%E6%A8%99&ui_lang=zh-hk&ui_charset=utf-8
    # 政府招標資料 搜尋憲報公告 https://www.gld.gov.hk/egazette/tc_chi/search_gazette/search.php?Years%5B%5D=2021&Date=&NoticeNo=&Title=%E6%8B%9B%E6%A8%99&type=mg&submit=%E6%90%9C%E5%B0%8B
    # 香港政府一站通 招标公告 https://pcms2.gld.gov.hk/iprod/#/sta00305
    # 政府發展局 https://www.devb.gov.hk/tc/construction_sector_matters/tender_notices/forecast_of_consultancies_and_tenders/tenders/
    # 政府物流服务署 HK https://www.gld.gov.hk/zh-cn/our-services/procurement/forecast-purchase/
    # 欢迎浏览电子采购计划 https://www.gov.hk/sc/theme/eprocurement/eppp/
    # 政府物流服务署的招标公告 https://www.gld.gov.hk/assets/gld/download-files/tender-notice/tender_notice_20210716_zh-cn.pdf
    # 招标公告, 计划意向书, 征求建议书 https://www.ogcio.gov.hk/sc/our_work/business/tender_eoi_rfp/

    # freelancer
    # https://hkese.net/jobs?query=app&refinementList%5Bfield_job_feature%5D%5B0%5D=Remote%20Work%20%E9%81%99%E8%B7%9D%20%2F%20%E5%9C%A8%E5%AE%B6%E5%B7%A5%E4%BD%9C&page=1
    # http://www.parttime.hk/jobs/SearchResults.aspx?q=%E7%A8%8B%E5%BC%8F%E9%96%8B%E7%99%BC&wt=S
    # https://www.freelancer.com/jobs/solidity/
    # https://www.zhipin.com/job_detail/54502c08e8f6c3581nR42t29E1dR.html
    # https://task.tw/


    # 檢查 ATWFacebookAc
    #while True: 
        #_LoginATW('ATWFacebookAc-@=',UserKey)
        #if UnLockData == '沒有NODATA內容':
            # _SaveData
            #print ('\n!!!!!沒有 ATWFacebookAc!!***\n')
        #    FBAc = input('\n請填寫您的Facebook帳號\n')
        #    _AutoWebKeySetting('ATWFacebookAc-@=',FBAc,UserKey)
        #    FBpw = input('\n請填寫您的Facebook密碼\n')
        #    _AutoWebKeySetting('ATWFacebookPw-@=',FBpw,UserKey)
        #    continue
        #break
    
    #_AutoWebLanguageSetting(_AutoWWebSettingTalk5+'==='+_AutoWWebSettingTalk7a+'==='+_AutoWWebSettingTalk7b+'==='+_AutoWWebSettingTalk7c+'==='+_AutoWWebSettingTalk8+'==='+_AutoWWebSettingTalk15a+'==='+_AutoWWebSettingTalk9+'==='+_AutoWWebSettingTalk10+'==='+_AutoWWebSettingTalk11+'==='+_AutoWWebSettingTalk12+'==='+_AutoWWebSettingTalk13+'==='+_AutoWWebSettingTalk14)
    #_StrToList(LanguageText,'===')
    #ATW_LS95=copy.deepcopy(TrueList)

    _MakeTalk()

    # 檢查 ATWFacebookGroupsURL
    while True: 
        _LoginATW('ATWFacebookGroupsURL-@=',UserKey)
        if UnLockData == '沒有NODATA內容':
            FBGrURLInput = input(Talk0+ATW_LS96[0]+_AutoWWebSettingTalk6+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[4]+_AutoWWebSettingTalk8a+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)
            _AutoWebKeySetting('ATWFacebookGroupsURL-@=',FBGrURLInput,UserKey)
            continue
        break

    # 檢查 ATWSendJobDataToFbInboxOwnId 100013505203886
    #while True: 
    #    _LoginATW('ATWSendJobDataToFbInboxOwnId-@=',UserKey)
    #    if UnLockData == '沒有NODATA內容':
    #        OwnIdInput = input('   請填寫要接收資料的 Email\n   收集到的資料將自動Email給您\n\n')
    #        _AutoWebKeySetting('ATWSendJobDataToFbInboxOwnId-@=',OwnIdInput,UserKey)
    #        continue
    #    break

    # 檢查 ATWFbPostkeyword1
    while True: 
        _LoginATW('ATWFbPostkeyword1-@=',UserKey)
        if UnLockData == '沒有NODATA內容':
            FbPostkeywordInput1 = input(AllTalk0+ATW_LS96[6]+ATW_LS96[7]+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)
            # 刪除 NewVlo 不能出現的字付
            _AutoWebKeySettingDelTxt('ATWFbPostkeyword1',FbPostkeywordInput1)
            FbPostkeywordInput1 = NewVlo000
            _AutoWebKeySetting('ATWFbPostkeyword1-@=',FbPostkeywordInput1,UserKey)
            continue
        break

    # 檢查 ATWFbPostkeyword2
    while True: 
        _LoginATW('ATWFbPostkeyword2-@=',UserKey)
        if UnLockData == '沒有NODATA內容':
            FbPostkeywordInput2 = input(AllTalk0+ATW_LS96[8]+ATW_LS96[9]+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)
            # 刪除 NewVlo 不能出現的字付
            _AutoWebKeySettingDelTxt('ATWFbPostkeyword2',FbPostkeywordInput2)
            FbPostkeywordInput2 = NewVlo000
            if FbPostkeywordInput2 != '':
                _AutoWebKeySetting('ATWFbPostkeyword2-@=',FbPostkeywordInput2,UserKey)
            continue
        break

    # 檢查 AFbPostNoKeywordInput
    while True: 
        _LoginATW('ATWFbPostNoKeyword-@=',UserKey)
        if UnLockData == '沒有NODATA內容':
            AFbPostNoKeywordInput = input(AllTalk0+ATW_LS96[10]+ATW_LS96[11]+ATW_LS96[1]+_AutoWWebSettingTalk7d+ATW_LS96[2]+ATW_LS96[5]+_AutoWWebSettingTalk15b+_AutoWWebSettingTalk15c+AllTalk0)
            # 刪除 NewVlo 不能出現的字付
            _AutoWebKeySettingDelTxt('ATWFbPostNoKeyword',AFbPostNoKeywordInput)
            AFbPostNoKeywordInput = NewVlo000
            if AFbPostNoKeywordInput != '':
                _AutoWebKeySetting('ATWFbPostNoKeyword-@=',AFbPostNoKeywordInput,UserKey)
            continue
        break
    

    # 檢查 ATWListTime
    while True: 
        _LoginATW('ATWListTime-@=',UserKey)
        if UnLockData == '沒有NODATA內容':
            AFbPostNoKeywordInput = input(AllTalk0+ATW_LS96[13]+AllTalk0)  #QQQQQQQQ
            # 刪除 NewVlo 不能出現的字付
            _AutoWebKeySettingDelTxt('ATWListTime',AFbPostNoKeywordInput)
            AFbPostNoKeywordInput = NewVlo000
            if AFbPostNoKeywordInput != '':
                _AutoWebKeySetting('ATWListTime-@=',AFbPostNoKeywordInput,UserKey)
            continue
        break
    


    # LOOP _AutoWWebSales
    while True: 

        # 付款用戶 chrome1  QQQQQQQQQQQQQQ 月
        _VIPUser(UserKey,UserKey,'USER')

        # 取FB群帖 chrome
        _FBGetGrPost(UserKey)
    
        if Loop_AutoWWebSales == 'LOOP':
            _AutoWebLanguageSetting('60秒後循環')
            print ('\n   *** ',LanguageText,' ***\n')
            time.sleep(60)
            continue
        else:
            _AutoWebLanguageSetting('升級 VIP 可無限自動循環')
            print ('\n   ***',LanguageText,'***\n')
            break


    print ('\n!!!!!_AutoWWebSalesEND!!***\n')





















# Facebook#########################################################################
##########################冇需要#########################################################
################################################################## AutoWeb _LoginFB 
def _LoginFB(UserKey):


    FB = 'Facebook'
    fb = "https://www.facebook.com/"

    while True: 

        # 檢查 ATWFacebookAc
        _LoginATW('ATWFacebookAc-@=',UserKey)

        if UnLockData == '沒有NODATA內容':
            # _SaveData
            #print ('\n!!!!!沒有 ATWFacebookAc!!***\n')
            FBAc = input('\n請填寫您的' + FB + '帳號\n')
            _AutoWebKeySetting('ATWFacebookAc-@=',FBAc,UserKey)

            FBpw = input('\n請填寫您的' + FB + '密碼\n')
            _AutoWebKeySetting('ATWFacebookPw-@=',FBpw,UserKey)
            continue
            
        break
    # 取
    FBAC = UnLockData
    _LoginATW('ATWFacebookPw-@=',UserKey)
    FBPW = UnLockData


    print ('\n!!!!!開始登入facebook!!***\n')

    #selenium chrome1 配置
    chrome1driverURL = KeyFolder
    _SteChrome(chrome1driverURL,'chrome1',UserKey)

    # 沒入email位回
    while True:      
        # 登入FB頁
        chrome1.get(fb)
        try:
            # 入email
            username002 = chrome1.find_element_by_xpath('//*[@id="m_login_email"]')
            # 入PS
            password002 = chrome1.find_element_by_xpath('//*[@id="m_login_password"]')
            # 點登入
            submit002 = chrome1.find_element_by_xpath('//*[@id="login_password_step_element"]/button')
        except: 
            try:
                # 入email 
                username002 = chrome1.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
                # 入PS
                password002 = chrome1.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
                # 點登入
                submit002 = chrome1.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
            except: 
                try:    # https://m.facebook.com/
                    # 入email                         
                    username002 = chrome1.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[4]/div[1]/div/div/input')
                    # 入PS
                    password002 = chrome1.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div/div/div[1]/div/input')
                    # 點登入
                    submit002 = chrome1.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[5]/div[1]/button')
                except: 
                    # 沒
                    print ('解碼錯誤***[找不到入email]***請聯絡開發者更新代碼\n')
                    chrome1.close()
                    InputData()
        break

    username002.send_keys(FBAC)                        
    #time.sleep(random.uniform(3, 11))

    password002.send_keys(FBPW)                        
    #time.sleep(random.uniform(3, 11))

    submit002.click()
    time.sleep(random.uniform(3, 11))

    # 編輯用 
    if Loop_AutoWWebSales == 'ADMIN':
        print ('\n*** ADMIN 編輯用 ***\n')
        os.system("pause")

    # 驗查登入否 
    chrome1.get(fb +'me/')
    currentURL = chrome1.current_url
    #print (str(currentURL) +'--currentURL\n')
    if currentURL == 'https://www.facebook.com/':
        print ('\n!!!沒有登入 請選其他帳號再試***\n')
        chrome1.close()
        InputData()

    # 轉言語 搵帖用中文
    while True:
        chrome1.get('https://mbasic.facebook.com/settings/language/')
        FBSettingsLanguageTw = chrome1.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/table[1]/tbody/tr/td/h3/a/span')
        # 如沒中文 轉
        if '中文' not in FBSettingsLanguageTw.text:
            FBSettingsLanguage = chrome1.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/table[1]/tbody/tr/td/h3/a/strong')
            FBSettingsLanguage.click()

            # 點 中文台灣
            # QQQQQQQQQQQQQQ 20210727 找不到 from
            print ('\n!!!!!請將語言轉為中文台灣再繼續!!***\n')
            os.system("pause")
            continue
        else:
            break
































###################################################################################
######################################################## AutoWeb _FBGetGrPost QQQQQQQQQQQQQQQ精簡QQQQQQQQQQQQQQQ
# 徵求,發案,任務,誠徵,尋找,請問有,外快,looking for,需要,i need,we need,need a,required,區塊鏈,Dapp,智能合約,erc721,ERC20,APP,直播,web,網站,網頁,website,web designer,Application,E-commerce,ecommerce,smart contract
# ATWFbPostkeyword1 = 1級關鍵字 = 徵求,發案,任務,誠徵,尋找,請問有,外快,looking for,需要,i need,we need,need a,required
# ATWFbPostkeyword2 = 2級關鍵字 = 區塊鏈,Dapp,智能合約,erc721,ERC20,APP,直播,web,網站,網頁,website,web designer,Application,E-commerce,ecommerce,smart contract
# ATWFbPostNoKeyword = 負關鍵字 = 徵才,我要接案,全職,組的字符集，因為這個原因，造,m Professional,Serving you,A degree (or equivalent) in Computer Science,hiring me,想問下各位 點解我<img src 插入既圖片可以在,工作職缺


# https://mbasic.facebook.com/hashtag/我要發案
# groups/359478437747556/,groups/flycan.webdesign/,groups/1335691586521825/,groups/1865822177019795/,groups/engeogeek/,groups/100528646656732/,groups/722896854461813/,groups/643006822972631/,groups/2553682591549795,groups/1230482576964177,groups/1418868921741092/,groups/web888/
FBMbasic = 'https://mbasic.facebook.com/'
def _FBGetGrPost(UserKey):

    # 檢查 
    _LoginATW('ATWFacebookGroupsURL-@=',UserKey)
    _StrToList(UnLockData,',')
    FBGrURL=copy.deepcopy(TrueList)
    _LoginATW('ATWFbPostkeyword1-@=',UserKey)
    _StrToList(UnLockData,',')
    ATWFbPostkeyword1=copy.deepcopy(TrueList)




    # 202108021704 OK
    _LoginATW('ATWListTime-@=',UserKey)
    _StrToList(UnLockData,',')
    ListTime=copy.deepcopy(TrueList)   

    # ListTime 比較 今年
    nowtime1 = nowtime.format("YYYY")   # 今日年
    ListTime1 = ListTime[-1][0:4]       # ATWListTime 取最後一個 頭4字
    #print ('ListTime1='+str(ListTime1))

    if nowtime1 != ListTime1:       # QQQQ 未試
    # ListTime年 != 今日年  = 超一年fb帖有完整年月，可直用
        #print ('Lis1tTime 可直用')
        ListTimeALL = []
        i = 0
        while i < len(ListTime): 
            _AutoWebLanguageSetting(ListTime[i])
            ListTimeALL.append(str(LanguageText))   # 轉英入
            ListTimeALL.append(str(ListTime[i]))    # 入  中
            i+=1
        #print ('ListTimeALL='+str(ListTimeALL))    # ListTimeALL == all lan ListTime

    else:
    # ListTime年 == 今日年  = 一年內fb帖 只有月 轉 純月
        #print ('ListT2ime 轉純月')

        ListTimeA=copy.deepcopy(ListTime[0:12])    # 上年  1 ~ 12
        ListTimeB=copy.deepcopy(ListTime[12:])   # 今年1月至ListTime
        ListTimeALL = []

        i = 0
        while i < len(ListTimeB):
            #fr2ff3f = str(ListTimeB[i][5:])
            #print ('fr2ff3f='+str(fr2ff3f))
            ListTimeALL.append(str(ListTimeB[i][5:]))
            i+=1
        # 純月 add  ListTimeALL

        i = 0
        while i < len(ListTimeA):
            ListTimeALL.append(str(ListTimeA[i]))
            i+=1
        # 上年 完整 add ListTimeALL

        i = 0
        ListTimeD = []
        while i < len(ListTimeALL):
            _AutoWebLanguageSetting(ListTimeALL[i])
            ListTimeD.append(str(LanguageText))
            i+=1
        i = 0
        while i < len(ListTimeD):
            ListTimeALL.append(str(ListTimeD[i]))
            i+=1
        # all 轉 en add ListTimeALL

        #print ('ListTimeALL # 沒轉en會看到重複='+str(ListTimeALL))
        #os.system("pause")
        # 202108021704 OK









    # Loop FBGrURL 到每一群
    FbGrCount = 0                #    FbGrCount            = 每一群     計算器
    while FbGrCount < len(FBGrURL):

        #selenium chrome 配置
        chromedriverURL = KeyFolder
        _SteChrome(chromedriverURL,'chrome',UserKey)


        URL = FBMbasic+'groups/'+str(FBGrURL[FbGrCount]).split('groups/')[-1]
        chrome.get(URL)

        FbPostGetMoreSel = 0     #    FbPostGetMoreSel     = 點更多     選擇器

        # 取群名
        FbGrName  = '/html/body/div/div/div[2]/div/div[1]/header/table/tbody/tr/td[1]/a/table/tbody/tr/td[2]/h1/div'
        try:
            Txt0 = chrome.find_element_by_xpath(FbGrName)
        except:
            _AutoWebLanguageSetting ('找不到 群名，已被封請1小時後再試\n')
            print (LanguageText)
            os.system("pause")

        FbGrName0 = Txt0.text

        print ('\n\n\n'+AllTalk0+'\n')
        _AutoWebLanguageSetting('開始取第===號群，')
        _StrToList(LanguageText,'===')
        ATW_LS1=copy.deepcopy(TrueList)
        print (ATW_LS1[0]+str(FbGrCount)+ATW_LS1[1]+'\n'+ str(FbGrName0)+'\n'+ str(URL)+'\n')

        # 私人群
        FBCode8 = '/html/body/div/div/div[2]/div/div[1]/header/table/tbody/tr/td[1]/a/table/tbody/tr/td[2]/p'
        element = WebDriverWait(chrome, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,FBCode8)),'解碼錯誤***[找不到 私人群]***')
        PublicPrivate = chrome.find_element_by_xpath(FBCode8)

        list = ['私人群組','private']
        if PublicPrivate.text in list:
            FbPostGetMoreSel = 1
            FbGrCount +=1
            chrome.close()
            continue

        #print ('nFbPostCount'+str(FbPostCount)+'\n')
        # Loop FbPost 取每一帖

        # 編輯用 
        if Loop_AutoWWebSales == 'ADMIN':
            print ('\n*** ADMIN 編輯用 ***\n')
            os.system("pause")

        FbPostCount = 1          #    FbPostCount          = 每一帖     計算器
        while FbPostCount < 9:

            _AutoWebLanguageSetting('必須等待===秒再開始，盡量減低被封機率。===查看更多帖子===解碼錯誤===找不到 帖內文點更多===號帖沒有內文')
            _StrToList(LanguageText,'===')
            ATW_LS2=copy.deepcopy(TrueList)

            # 等待  
            SleepForFB = random.uniform(3, 15)
            SleepForFB = round(SleepForFB, 2)
            print (ATW_LS2[0]+str(SleepForFB)+ATW_LS2[1]+TalkEND)
            time.sleep(SleepForFB)

            # 取整帖    article class="bh bi bj"    202107241822
            FBCode0  = '/html/body/div/div/div[2]/div/div[1]/div[*]/section/article['+str(FbPostCount)+']'
            # 取帖內文
            FBCode1  = FBCode0+'/div/div/div'
            FBCode1b  = FBCode0+'/div/div[*]/div'
            # 取帖時
            FBCode2  = FBCode0+'/footer/div[1]/abbr'
            # 取帖主
            FBCode3a = FBCode0+'/div/header/table/tbody/tr/td[2]/header/h3/strong'
            FBCode3b = FBCode0+'/div/header/table/tbody/tr/td[2]/header/h3/span/strong[1]'
            # 取帖主ID
            FBCode4a = FBCode0+'/div/header/table/tbody/tr/td[2]/header/h3/strong/a'
            FBCode4b = FBCode0+'/div/header/table/tbody/tr/td[2]/header/h3/span/strong[1]/a'

            # 查看更多帖子 
            if FbPostGetMoreSel == 0: 
                if FbPostCount == 8: 
                    print ('--------',ATW_LS2[2],'--------\n')
                    try:
                        FBCode5 = '/html/body/div/div/div[2]/div/div[1]/div[*]/div/a'
                        FbPostClickMore = chrome.find_element_by_xpath(FBCode5)
                        FbPostClickMore.click()
                        FbPostCount = 0

                        # 編輯用
                        if Loop_AutoWWebSales == 'ADMIN':
                            print ('\n*** ADMIN 編輯用 ***\n')
                            print ('\n***人手找關鍵字***\n')
                            os.system("pause")
                        continue

                    except:
                        FbPostGetMoreSel = 1
                        FbPostCount = 0
                        continue

            # 取帖內文  
            _AutoWebLanguageSetting('開始取第===號帖')
            _StrToList(LanguageText,'===')
            print ('開始取第'+str(FbGrCount)+ATW_LS1[1]+str(FbPostCount)+'號帖-----*\n')
            try:
                Txt1 = chrome.find_element_by_xpath(FBCode1)
                TxtOk = Txt1.text
            except:
                try:
                    Txt1 = chrome.find_element_by_xpath(FBCode1b)
                    TxtOk = Txt1.text
                except:
                    print ('----------------\n')
                    FbPostCount+=1
                    continue

            # 帖內文點更多 
            if '更多' in Txt1.text :
                # 202107242226
                FBCode6 =  '/html/body/div/div/div[2]/div/div[1]/div[*]/section/article['+str(FbPostCount)+']/div/div[*]/div[1]/div[4]/div/span/a'
                FBCode6b = '/html/body/div/div/div[2]/div/div[1]/div[*]/section/article['+str(FbPostCount)+']/div/div[*]/div/span/a'
                try:
                    FbPostTxtClickMore = chrome.find_element_by_xpath(FBCode6).get_attribute("href")
                except: 
                    try:
                        FbPostTxtClickMore = chrome.find_element_by_xpath(FBCode6b).get_attribute("href")
                    except: 
                        print (ATW_LS2[3],'***[',ATW_LS2[4],']***\n')
                        if Loop_AutoWWebSales == 'ADMIN':
                            print ('\n*** ADMIN 編輯用 ***\n')
                            print('***未 20210728***')
                            os.system("pause")
                        FbPostCount+=1
                        continue

                #selenium chrome 配置
                chromedriverURL = KeyFolder
                _SteChrome(chromedriverURL,'chrome2',UserKey)
                chrome2.get(FbPostTxtClickMore)

                # 帖內文
                FBCode7 = '/html/body/div/div/div[2]/div/div[*]/div[1]/div/div/div[*]/div'
                #element = WebDriverWait(chrome, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,FBCode7)),'解碼錯誤***[找不到 帖內文]***')
                try:
                    Txt1 = chrome2.find_element_by_xpath(FBCode7)
                    TxtOk = Txt1.text
                except:
                    TxtOk = ''
                chrome2.close()

            # 不要沒有內文帖
            if TxtOk == '':
                #print (str(FbPostCount)+ATW_LS2[5]+'-----NO=xxx(-_-) \n')
                FbPostCount+=1
                continue

            # 帖內文 轉 List
            _StrToList(TxtOk,'\n')
            TxtOkList=copy.deepcopy(TrueList)

            # 取帖主 
            try:
                Txt3 = chrome.find_element_by_xpath(FBCode3a)
                Txt4 = chrome.find_element_by_xpath(FBCode4a).get_attribute("href")
            except: 
                try:
                    Txt3 = chrome.find_element_by_xpath(FBCode3b)
                    Txt4 = chrome.find_element_by_xpath(FBCode4b).get_attribute("href")
                except: 
                    print ('解碼錯誤***[找AAAAAAAAA不到 帖主]***')  # QQQQQQQQQ
                    _AutoWebLanguageSetting('解碼錯誤***[找不到 帖主]***請5分鐘後重試。如多次錯誤，請聯絡開發者更新代碼')
                    print (LanguageText,TalkEND)

            # 取帖主ID
            _StrToList(Txt4,'%')
            GetFbPoOwnID = 0
            while GetFbPoOwnID < len(TrueList):
                if '3Acontent_owner_id_new.' in TrueList[GetFbPoOwnID]:    
                    Txt4 = str(TrueList[GetFbPoOwnID]).replace('3Acontent_owner_id_new.', '')
                GetFbPoOwnID+=1


            ################################################################
            # 如時間岩 ************************************************ 條件1
            # 取帖時

            element = WebDriverWait(chrome, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,FBCode2)),'解碼錯誤***[找不到 帖時]***')
            Txt2 = chrome.find_element_by_xpath(FBCode2)

            # 202108021801 OK
            _AutoWebLanguageSetting('號帖日期 = [===]本帖不儲存===如本頁其他帖也都過期，將不再查看更多帖子')
            _StrToList(LanguageText,'===')
            ATW_LS94=copy.deepcopy(TrueList)

            
            timeNotOk = []
            for tm in ListTimeALL:
                if tm in Txt2.text:
                    timeNotOk.append(tm)

            if timeNotOk : 
                print (str(FbPostCount)+ATW_LS94[0]+str(timeNotOk[0])+ATW_LS94[1]+'-----NO Time x--- -_- \n'+ATW_LS94[2])
                FbPostGetMoreSel = 1
                FbPostCount += 1
                #os.system("pause")
                continue
            #else:
            #    print (str(FbPostCount)+ATW_LS94[0]+str(Txt2.text)+']-----OK Time=o__( \n') 
            #os.system("pause")

            ################################################################
            # 如有 負關鍵字 不記 ************************************** 條件2

            # 取 負關鍵字 
            _LoginATW('ATWFbPostNoKeyword-@=',UserKey)
            if UnLockData != '沒有NODATA內容':
                _StrToList(UnLockData,',')
                ATWFbPostNoKeyword=copy.deepcopy(TrueList)

                # 取整帖
                ATWFbPostNoKeywordTxt1 = chrome.find_element_by_xpath(FBCode0)
                _StrToList(ATWFbPostNoKeywordTxt1.text,'\n')
                ATWFbPostNoKeywordList=copy.deepcopy(TrueList)

                # ATWFbPostNoKeyword 比較 TxtOkList
                ATWFbPostNoKeywordHave = []
                ATWFbPostNoKeywordHave.clear()
                for kw in ATWFbPostNoKeywordList:
                    for word in ATWFbPostNoKeyword:
                        if word in kw:
                            ATWFbPostNoKeywordHave.append(word)

                if ATWFbPostNoKeywordHave : 
                    _AutoWebLanguageSetting('負關鍵字')
                    print (LanguageText+'==\n'+str(ATWFbPostNoKeywordHave)+'-----NO NoKey ox-- (-_-) \n') 
                    FbPostCount += 1
                    continue
            
            #print (str(FbPostCount)+ATW_LS94[0]+str(Txt2.text)+']-----OK2=oo_(^ \n') 
            # 如有 ************************************************ 加條件

            ################################################################
            # 如有 1級關鍵字 ****************************************** 條件3
            # ATWFbPostkeyword1 比較 TxtOkList
            FbPostkeywordHave1 = []
            FbPostkeywordHave1.clear()
            for kw in TxtOkList:
                for word in ATWFbPostkeyword1:
                    if word in kw:
                        FbPostkeywordHave1.append(word)
            # 刪空值 
            while '' in FbPostkeywordHave1:
                FbPostkeywordHave1.remove('')

            _AutoWebLanguageSetting('號帖沒有 1級關鍵字===號帖有 1級關鍵字')
            _StrToList(LanguageText,'===')
            if not FbPostkeywordHave1 :  
                # 直接下帖
                print (str(FbPostCount)+TrueList[0]+'-----NO 1Key oox- (T_T) \n')
            else:
                #print (str(FbPostCount)+TrueList[1]+'-----OK 1Key=ooo(^_ \n')
                #print (str(FbPostkeywordHave1)+'\n')


                ################################################################
                # 2級關鍵字 *********************************************** 條件4

                



                # 取 2級關鍵字
                _LoginATW('ATWFbPostkeyword2-@=',UserKey)

                # 轉 URL


                if UnLockData == '沒有NODATA內容':
                    FbPostGetMoreSel = 0    # 查看更多帖子
                    #print ('沒有2級關鍵字，您可到 _AutoWWebSetting 加入-----*\n')
                    # 保存工作資料(群名,群Url,帖時,帖主ID,帖主,關鍵字,帖文,帖號,sel)
                    _SaveJob(FbGrName0,URL,Txt2.text,Txt4,Txt3.text,FbPostkeywordHave1,TxtOk,FbPostCount,UserKey,'FbPost')
                    # 附合條件1+2帖 ************************************************ 附合條件1+2帖
                else:
                    # 如有 ************************************************ 加條件

                    FbPostGetMoreSel = 0    # 查看更多帖子

                    _StrToList(UnLockData,',')
                    ATWFbPostkeyword2=copy.deepcopy(TrueList)

                    # ATWFbPostkeyword2 比較 TxtOkList
                    FbPostkeywordHave2 = []
                    FbPostkeywordHave2.clear()
                    for kw in TxtOkList:
                        for word in ATWFbPostkeyword2:
                            if word in kw:
                                FbPostkeywordHave2.append(word)
                    # 刪空值 
                    while '' in FbPostkeywordHave2:
                        FbPostkeywordHave2.remove('')

                    _AutoWebLanguageSetting('號帖沒有 2級關鍵字===號帖有 2級關鍵字')
                    _StrToList(LanguageText,'===')

                    if not FbPostkeywordHave2 :
                        print (str(FbPostCount)+TrueList[0]+'-----NO 2Key ooox (T^T) \n')
                    else:
                        print (str(FbPostCount)+TrueList[1]+'-----OK ALL oooo (^_^) \n')
                        print (str(FbPostkeywordHave2)+'\n')

                        # 2級關鍵字 入 FbPostkeywordHave1
                        i = 0
                        while i < len(FbPostkeywordHave2):
                            FbPostkeywordHave1.append(FbPostkeywordHave2[i])
                            i+=1

                        # 保存工作資料(群名,群Url,帖時,帖主ID,帖主,關鍵字,帖文,帖號,sel)
                        _SaveJob(FbGrName0,URL,Txt2.text,Txt4,Txt3.text,FbPostkeywordHave1,TxtOk,FbPostCount,UserKey,'FbPost')
                        # 附合條件1+2+3帖 ************************************************ 附合條件1+2+3帖


            FbPostCount+=1
        # Loop FbPost END if FbPostGetMoreSel == 1
        _AutoWebLanguageSetting('已取完第===號群帖。')
        _StrToList(LanguageText,'===')
        print (TrueList[0]+str(FbGrCount)+TrueList[1]+'\n')
        chrome.close()
        FbGrCount+=1
    # Loop FBGrURL 到每一群 END
    _AutoWebLanguageSetting('已取完所有群帖。===下一步')
    _StrToList(LanguageText,'===')
    print (TrueList[0]+AllTalk0)
    print ('\n***',TrueList[1],'***\n')


















































JobFolderDataFn = 0
FbPostAllData = 0
####################################################### AutoWeb selenium chrome set
def _SaveJob(V1,V2,V3,V4,V5,V6,V7,v8,UserKey,sel): 
    global JobFolderDataFn
    global FbPostAllData
    if sel == 'FbPost':

        # _FBGetGrPost (群名,群Url,帖時,帖主ID,帖主,關鍵字,帖文,sel)
        
        #刪除所有中英符號
        #_DelPunctuation(str(V6))    # 關鍵字
        #FbPostkeyword0 = NoPunctuation.replace(' ', '').replace('：', '').replace('＃', '').replace('、', '')
        
        _DelPunctuation(str(V7))    # 帖文
        FbPostTxt = NoPunctuation.replace(' ', '').replace('：', '').replace('＃', '').replace('、', '').replace('\\', '')

        #帖時轉日期
        FbPostToDayList = ['剛','小','今','鐘','hrs']
        FbPostToDay = []
        for kw in FbPostToDayList:
            for word in str(V3):
                if kw in word:
                    FbPostToDay.append(word)
        if FbPostToDay :
            #   '剛剛','小時','今日'   =   今日
            ft = today.strftime("%m月%d日")
            FbPostTime = str(ft).replace('0', '')
        else:
            #   '昨天'   =   今日 - 1
            if '昨天' in str(V3): 
                Day = today - datetime.timedelta(1)
                otherStyleTime = Day.strftime("%m月%d日")
                FbPostTime = str(otherStyleTime).replace('0', '')
            else:
                #   使用帖原日期(" "之前的值)
                _StrToList(V3,'日')
                eqw = TrueList[0]
                FbPostTime = eqw+'日'

        # 帖主ID 帖主名
        if V4 != 'None': 
            FbPostOwnInbox = str('https://mbasic.facebook.com/messages/thread/'+str(V4))
            FbPostOwnName = str(V5)


        # save # save # save # save # save # save # save # save # save 
        # 查創 job文件夾
        JobFolder = KeyFolder+"/job/"
        _SetFolder(JobFolder,'MakeFolder')


        # JobFolder =_atw/job/帖時_帖主ID_帖主名_關鍵字_帖文
        #JobFolderData = FbPostTime+"_"+FbPostOwnInbox+"_"+FbPostOwnName+"_"+FbPostkeyword0+"_"+FbPostTxt

        # JobFolder =_atw/job/ 帖時_帖主名_帖文
        _AutoWebLanguageSetting(FbPostOwnName+'==='+FbPostTxt)
        _StrToList(LanguageText,'===')

        JobDataKey = (TrueList[0]+"_"+TrueList[1])[0:80]    # 限字數免超檔名數限
        JobFolderData = FbPostTime+"_"+JobDataKey
        JobFolderDataFn = JobFolder+'NEW'+JobFolderData+'/' # _狀態

        # 查 相同資料
        JobDataKeyHave = 0
        for root, dirs, files in os.walk(JobFolder):
            i = 0
            while i < len(dirs):
                if JobDataKey in dirs[i]:
                    _AutoWebLanguageSetting('相同資料已存在，不記錄')
                    print('\n*** ',LanguageText,' ***\n')
                    JobDataKeyHave = 1
                    # 重PO特別 QQQQ
                i+=1

        if JobDataKeyHave == 0:
            # 创 單個job文件夾
            _SetFolder(JobFolderDataFn,'MakeFolder')

            # 截圖
            FBCode0  = '/html/body/div/div/div[2]/div/div[1]/div[*]/section/article['+str(v8)+']'
            element = WebDriverWait(chrome, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,FBCode0)),'解碼錯誤***[找不到 截圖]***')
            SaveScreenshot = chrome.find_element_by_xpath(FBCode0)
            #_SeleniumHighlight(SaveScreenshot, 3, "blue", 5)

            FBJobScreenshot = JobFolderDataFn+FbPostTime+".png"
            SaveScreenshot.screenshot(FBJobScreenshot)

            # 寫入job文件
            _AutoWebLanguageSetting('帖主名稱===帖文===發帖日期===群名===關鍵字===帖主===記錄時間===翻譯')
            _StrToList(LanguageText,'===')
            

            JobFolderDataTn = JobFolderDataFn+JobFolderData+'.txt'
            _AutoWebLanguageSetting(V7)
            FbPostAllData = (
                
                '\n\n'+TrueList[0]+' = '+FbPostOwnName+
                '\n---\n'+
                '\n'+TrueList[1]+' = \n'+V7+
                '\n-\n'+
                '\n'+TrueList[7]+' = \n'+LanguageText+
                '\n---\n'+
                '\n'+TrueList[2]+' = '+FbPostTime+
                '\n----------\n'+
                '\n'+TrueList[3]+' = '+V1+
                '\nUrl = '+V2+
                '\n'+TrueList[4]+' = '+str(V6)+
                '\n----------\n'+



                '\n'+TrueList[5]+'Inbox = '+FbPostOwnInbox+
                '\n'+TrueList[6]+' = '+today.strftime("%y-%m-%d %H:%M:%S")+
                '\n'+AllTalk0+'\n\n\n'
                )

            _SaveData('999',FbPostAllData,JobFolderDataTn,'JOB')

            # 發自動搵客資料ToYou QQQQQ
            # _SendJobDataToFbInbox(UserKey)







###################################################################################
# _SendJobDataToFbInbox############################################# 發自動搵客資料ToYou QQQQQQ
def _SendJobDataToFbInbox(UserKey):

    # 檢查 ATWSendJobDataToFbInboxOwnId
    while True: 
        _LoginATW('ATWSendJobDataToFbInboxOwnId-@=',UserKey)
        if UnLockData == '沒有NODATA內容':
            OwnIdInput = input('   請填寫要接收資料的FacebookID\n   收集到的資料將自動Inbox給您\n\n')
            _AutoWebKeySetting('ATWSendJobDataToFbInboxOwnId-@=',OwnIdInput,UserKey)
            continue
        break

    FBInboxOwnId = UnLockData

    # Login FB
    #_LoginFB(UserKey)

    chrome1.get('https://mbasic.facebook.com/messages/thread/'+FBInboxOwnId)

    # 新增相片
    #FBCode_SendJobDataToFbInbox0  = '//*[@id="composer_form"]/span/input[2]'
    #chrome1.find_element_by_xpath(FBCode_SendJobDataToFbInbox0).click()

    # 寫信息
    chrome1.find_element_by_xpath('//*[@id="composerInput"]').send_keys(FbPostAllData,JobFolderDataFn)  

    # send
    chrome1.find_element_by_xpath('//*[@id="composer_form"]/table/tbody/tr/td[2]/input').click() 

    # 登出fb
    #chrome1.close()





























###################################################################################
####################################################### AutoWeb selenium chrome set
def _SteChrome(chromedriverURL,ChromeSel,UserKey):     #   (保存chromedriver的路徑)
    global chrome
    global chrome1
    global chrome2


    #selenium chrome 配置
    options = Options()
    if ChromeSel == 'chrome1':
        options.add_argument('--headless')  # 配置无界面

    options.add_argument("--incognito")  # 配置隐私模式 https://blog.csdn.net/weixin_35757704/article/details/112975153
    options.add_argument("--disable-notifications")

    # 取消log
    options.use_chromium = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # 檢查 ATWUserSeleniumUserAgent
    while True: 
        _LoginATW('ATWUserSeleniumUserAgent-@=',UserKey)
        if UnLockData == '沒有NODATA內容':
            # random UserAgent
            #https://stackoverflow.com/questions/49565042/way-to-change-google-chrome-user-agent-in-selenium/49565254#49565254
            ua = UserAgent()
            userAgent = ua.random
            _AutoWebKeySetting('ATWUserSeleniumUserAgent-@=',userAgent,UserKey)
            continue
        break
    
    #print ('\n!!!!!userAgent!!***\n' + str(UnLockData) +'\n')


    #random window_siz
    #        K                    k    k
    W = [280,540,375,414,375,320,411,411,360]
    H = [653,720,812,736,667,568,823,731,640]

    # chromedriver有否
    while True:
        try:
            chromedriverURL0 = chromedriverURL + '/chromedriver'

            if ChromeSel == 'chrome':
                chrome = webdriver.Chrome(chromedriverURL0, chrome_options=options)
                ua = UserAgent()
                userAgent = ua.random
                options.add_argument(f'user-agent={userAgent}')
                N = int(random.uniform(0, 8))
                chrome.set_window_size(W[N],H[N])

            if ChromeSel == 'chrome1':
                chrome1 = webdriver.Chrome(chromedriverURL0, chrome_options=options)
                options.add_argument(f'user-agent={UnLockData}')
                

            if ChromeSel == 'chrome2':
                chrome2 = webdriver.Chrome(chromedriverURL0, chrome_options=options)
                ua = UserAgent()
                userAgent = ua.random
                options.add_argument(f'user-agent={userAgent}')
                N = int(random.uniform(0, 8))
                chrome2.set_window_size(W[N],H[N])

            break
        except:
            # 自动下載最新chromedrive
            _InputChromeAutoUpData(chromedriverURL)    #   (保存chromedriver的路徑)
            continue
    







################################################################ _SeleniumHighlight
# https://stackoverflow.com/questions/52207164/python-selenium-highlight-element-doesnt-do-anything
#   _SeleniumHighlight(Txt1, 3, "blue", 5)
def _SeleniumHighlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    chrome = element._parent
    def apply_style(s):
        chrome.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)


















































'''

       /\          /\          /\
    /\//\\/\    /\//\\/\    /\//\\/\
 /\//\\\///\\/\//\\\///\\/\//\\\///\\/\
//\\\//\/\\///\\\//\/\\///\\\//\/\\///\\
\\//\/                            \/\\//
 \/                                  \/
 /\                                  /\
//\\            內部功能             //\\
\\//                                \\//
 \/                                  \/
 /\                                  /\
//\\/\                            /\//\\
\\///\\/\//\\\///\\/\//\\\///\\/\//\\\//
 \/\\///\\\//\/\\///\\\//\/\\///\\\//\/
    \/\\//\/    \/\\//\/    \/\\//\/
       \/          \/          \/
'''


# QQQQQQQQQQQQQQQQQQQ 月auto
###################################################################################
################################################################# AutoWeb 付款用戶 
def _VIPUser(VIPName,UserKey,sel):     #   (名)
    global Loop_AutoWWebSales

    # Key 轉 sha256 ATW加密KEY
    Key2 = VIPName + 'ATW2021VIPUser'
    _ChgCodeAll(999,Key2,256) 
    VIPUserKey256 = tttKey

    if sel == 'ADMIN':
        print ('\  ===== ADMIN ===== \n')
        
        RdData = 'AutoWeb--自動收入程式' + VIPUserKey256 + '食左飯未' + today.strftime("%y年%m月%d日 %H:%M:%S")
        #16加密
        _ChgCodeAll(999,RdData,16)       #   (999,保存的內容,動作)

        #刪PY廢字
        tttKey22 = str(tttKey)
        tttKey33 = tttKey22[2:-1]
        VIPUserKeyCode = str(tttKey33)+str(VIPUserKey256)+str(tttKey33)

    #selenium chrome1 配置
    chrome1driverURL = KeyFolder
    _SteChrome(chrome1driverURL,'chrome1',UserKey)
    
    # VIP官方DATA
    chrome1.get('https://raw.githubusercontent.com/mokaki/AutoWeb/master/VIP.data')
    GetData = chrome1.find_element_by_xpath('/html/body/pre').text
    chrome1.close()

    if VIPUserKey256 in GetData:
        Loop_AutoWWebSales = 'LOOP'
        print ('\n   !!!!! VIPUser !!!!! \n' )
    else:
        Loop_AutoWWebSales = '1'
        _AutoWebLanguageSetting('升級 VIP 可無限自動循環')
        print ('\n   ***',LanguageText,'***\n')

    if sel == 'ADMIN':
        print (str(VIPUserKeyCode))
        print (str(VIPUserKey256))
        print ('https://raw.githubusercontent.com/mokaki/AutoWeb/master/VIP.data')
        #print (str(Loop_AutoWWebSales) +'--Loop_AutoWWebSales\n')

        # save QQQQQ
        os.system("pause")

    #print ('\n!!!!!_VIPUser END==!\n' )








######################################################### 刪除 NewVlo 不能出現的字付 #
### qqqqq FB??
def _AutoWebKeySettingDelTxt(ATWKey,v1): 
    global NewVlo000

    # 修改fb尋帖 最後日期
    if ATWKey == 'ATWListTime': 
        while True:
            try:
                #   錯重多一次 QQQ
                v1 = int(input(AllTalk0+ATW_LS96[13]+AllTalk0))
            except:
                print(ATW_LS96[15])
                continue
            break

        while True:
            if v1 < 1:
                print(ATW_LS96[14])
                print('3333')
                v1 = int(input(AllTalk0+ATW_LS96[13]+AllTalk0))
                continue
            NewVlo000 = str(v1)
            break

        # ListTime0 = - 後日期
        
        ListTime0 = nowtime.shift(months=-int(NewVlo000))

        # 生成年用以比較
        nowtime1 = nowtime.format("YYYY年MM月")
        ListTime1 = ListTime0.format("YYYY年MM月")

        # 生成全年所有之前月 帖有不存 QQQQ
        ListTime2 = ListTime0.format("年MM")
        ListTime2 = str(ListTime2).replace('年0', '').replace('年', '')
        ListTime3 = ListTime0.format("YYYY")
        # ListTime2 = int(月) ListTime = int(年)

        ListTimeMList = []

        i = 1
        ListTime4 = int(ListTime3) - 1
        while i < 13:
            ListTimeMList.append(str(ListTime4)+'年'+str(i)+'月')
            i+=1

        i = 1
        ListTime5 = int(ListTime2) + 1
        while i < ListTime5:
            ListTimeMList.append(str(ListTime3)+'年'+str(i)+'月')
            i+=1
        # ListTimeMList[0] = YYYY年MM月 上年至今年最後帖日

        NewVlo000 = str(ListTimeMList).replace('[', '').replace(']', '').replace("'", "").replace(" ", "")
        #print (str(NewVlo000)+'-----NewVlo000 \n')

    # 刪除 NewVlo 不能出現的字付
    if ATWKey != 'ATWListTime': 
        while True: 
            if '"' in v1 : # "
                v1 = v1.replace('"', '')
            if "'" in v1 : # '
                v1 = v1.replace("'", '')
            if ',,' in v1 : # ,,
                v1 = v1.replace(',,', ',')
                continue
            if v1[-1] == ',' : # 尾,
                v1 = v1[0:-2]
                continue
            NewVlo000 = str(v1)
            break












###################################################################################
################################################################ AutoWeb 文字轉list
TrueList = []
def _StrToList(txt,cut):                 #   (文字,分割符號)
    global TrueList
    txt,cut = str(txt),str(cut)
    TrueList.clear()                     #                  清空列表
    StrNotList = txt.split(cut)          #   str扮list指定 \n 分隔符號
    i = 0                                #         i = StrNotList計算器
    while i < len(StrNotList):           #   當 計算器 少於 data  總長
        TrueList.append(StrNotList[i])   #   將 data[a] 加入 TrueList
        i+=1



###################################################################################
################################################################# AutoWeb 生成文字檔
def _SaveData(Key256,v1,v2,sel):     #   (Key256,'所,有,前,值,新值名,',v2,sel)

    if sel == 'JOB':
        #保存文件                #   '帖時_帖主ID_帖主名_關鍵字_帖文'
        with open(v2, 'a', encoding="utf-8") as kf:
            kf.write(v1)
        kf.close()
        #print ('\n!!!!!已保存!!***\n'+str(v2))
        _AutoWebLanguageSetting('已保存內容')
        print ('\n   ***'+LanguageText+'***\n' + str(v1))
    else:

        #保存ATW密文檔
        #保存的內容                            單數 = 名 雙數 = 容 
        D1 = str(v1 + v2 + '\n')         #        \n 分格
        Dt = str(D1)

        #16加密
        _ChgCodeAll(999,Dt,16)       #   (999,保存的內容,動作)

        #加密3 偽隨機打亂
        _ChgCodeAll(Key256,tttKey,3)     #   (sha256Key,16內容,動作)

        #新文件名
        if sel == 'NEW':
            KU1 = (KeyUrl.split("/")[0]) #   'AutoWeb'
            KU2 = (KeyUrl.split("/")[1]) #   '0.atw'
            DF2 = KU1 + '/' + time.strftime('%Y%m%d%H%M%S') + KU2
        if sel == '0.atw':
            DF2 = KeyUrl


        #print ('保存文件\n'+ str(tttKey) +'\n')
        #保存文件                #   'AutoWeb/time0.atw'
        with open(DF2, 'w', encoding="utf-8") as kf:
            kf.write(tttKey)
        kf.close()

        #print ('\n!!!!!已保存 '+str(DF2)+' !!***\n')
        #print ('\n!!!!!內容!!***\n' + str(Dt) + '\n!!***\n')

        if sel == 'NEW':
            #檢查ATW密文檔
            while True:
                if not os.path.isfile(KeyUrl):
                    _AutoWebLanguageSetting('請先將===密文名修改為===再繼續')
                    _StrToList(LanguageText,'===')
                    print ('\n   ***',TrueList[0],'ATW',TrueList[1],'0.atw',TrueList[2],'***\n')
                    os.system("pause")
                    continue
                break



###################################################################################
############################################################ AutoWeb 檢查ATW密文在否
def _LoginATW(ATWKeyName,UserKey):     #   ('ATWKeyname-@=',UserKey) ('fbac,',UserKey) ('fbpw,',UserKey)
    #print ('Key\n'+ str(Key) +'\n')

    # Key 轉 sha256 ATW加密KEY
    Key2 = UserKey + '.'
    _ChgCodeAll(999,Key2,256)       #   (999,UserKey+ATWKey,動作)
    UserKey256 = tttKey

    #檢查ATW密文在否，如不在，先記錄再登入
    if not os.path.isfile(KeyUrl):       #    _atw/0.atw不在
        #   開新AC 去記錄
        _SaveData(tttKey,ATWKeyName,UserKey,'NEW')    #   (Key256,'ATWKeyname-@=',UserKey,sel)

        #   記Key256 去記錄2
        _LoginATW('ALL',UserKey)
        Dt = str(UnLockData+'ATWKey256-@=')
        #print ('保存文件\n'+ str('\n'+Dt+UserKey256+'\n') +'\n')
        _SaveData(UserKey256,Dt,UserKey256,'0.atw')    #   (Key256,'ATWKeyname-@=',UserKey,sel)
        _LoginATW('ATWKeyname-@=',UserKey)

    _UnLockATW(UserKey256,ATWKeyName)  #   (Key256,要取的ATWKeyName) _UnLockATWv1,_UnLockATWv2,_UnLockATWsel)



###################################################################################
################################################################ AutoWeb 解碼ATW密文
UnLockData = 0
def _UnLockATW(sha256Key,ATWKeyName):     #   (Key256,ATWKeyName) v1,v1,v2,sel)
    global UnLockData
    
    # 重置 UnLockData
    UnLockData = '沒有NODATA內容'

    # 打開文件 解碼
    for i in open(KeyUrl, 'r', encoding='UTF-8'):
        d1 = i

    # 解密30 偽隨機打亂
    _ChgCodeAll(sha256Key,d1,30)       #   (sha256Key,ATW密文,動作)

    #驗證內容碼
    try:
        # 解密160 binascii
        _ChgCodeAll(999,tttKey,160)       #   (999,160密文,動作)
    except:
        # 解密錯誤
        print ('\n ***************** \n')
        _AutoWebLanguageSetting('密匙錯誤===請先將您的ATW密文修改為===方可登入')
        _StrToList(LanguageText,'===')

        print ('\n   ***[',TrueList[0],']***\n')
        print ('\n   ***',TrueList[1],' 0.atw ***\n')
        _AutoWebLanguageSetting(talk5+talk6)
        print ('\n'+LanguageText+'\n')
        print ('\n ***************** \n')
        # 重新開始
        InputData()

    # 取得內容
    if ATWKeyName == 'ALL':
        # 顯示所有內容
        UnLockData = tttKey

    else:
        # 顯示指定內容

        # 文件內容入list
        _StrToList(tttKey,'\n')
        #print ('\n'+ str(TrueList))
        # TrueList[0] = ATWKeyname-@=...

        # list中找指定str行
        i = 0
        while i < len(TrueList):
            #  ATWKeyName = ATWKey***-@=
            if ATWKeyName in TrueList[i]:    
                # 記錄及刪除 ATWKeyName
                UnLockData = str(TrueList[i]).replace(ATWKeyName, '')
            i+=1
        #print (ATWKeyName + '-\n' + str(UnLockData) + '\n')



###################################################################################
########################################################################## 退出程式
def _OUT():
    print ("---------------------------")
    _AutoWebLanguageSetting('按鍵退出程式')
    print(LanguageText)
    os.system("pause")
    os._exit()



# 內部功能##########################################################################
################################################################################END




























































































# *****************************本app選擇
# hisPy = 
# adminATW = ATW.py ~ 
# 客戶版ATW = 自動搵客.py ~ _AutoWWebSales(UserKey) + Loop_AutoWWebSales = 'LOOP'

# Auto chromedriverNO 必須帶chromedriver
# Auto pip Import NO
ThisPy = '女'   # 自動搵客.py
# 執行本.py
if __name__=='__main__':
    InputData()
    #os.system("pause")







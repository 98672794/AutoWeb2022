

'''
winpy3

0Start
runThe.py
ATW202202061852
mokaki
https://98672794.github.io/



**********
README()



請選擇功能 
    0Start._index()

開始執行同層的py檔 
    0Start._RunThePY()



**********
檢查使用者 UserInputData ---------
    |           |         |     |   
    |           |         |     |
ifUser         hv_atw    not
auto run  ---- user ---- makeAcc  admin---AdminSet
        |       |   
        |    _index()     
        |       |
        |-ifUser--autoRun
        |-hv_atw----index
        |-not-----makeAcc
        |-user set auto run 
        |
        |- _SetFolder _GetFolder _MakeJobFolder
        |
        -Er-_Error(e)





**********
User coed /
_atw -  |0.atw 
        |--.py
        |--.html
        |--.job
        |--...








'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os 

from getpass import getpass # 填寫密匙時將不會顯示

import random
import math

import time
import hashlib  # 不可解 sha256 
import binascii # binascii加密   可解


















密匙檔路徑 = '_atw' #202202051729

#######################################################################
##################################################### Start = 開始 分頁0
def UserInputDatart():

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
        NowJobFolder = _MakeJobFolder(密匙檔路徑)
        # NowJobFolder = 文件夾 全路徑




        print('qqqqqqqqqqqq=')
        # 登入ATW
        _LoginATW('ATWKeyname-@=',UserKey,NowJobFolder)     
        #   (v1,ATW密匙),sel,_UnLockATWv1,_UnLockATWv2,_UnLockATWsel)

        #########if YouAcTo == 'NewAc':

        print('qqqqqqqqqqqq=')
        os.system("pause")

        # Goto _index
        #__index(UnLockData)


        ##############新言


    except Exception as e:
        _Error(e)
        os.system("pause")
        pass













##################################################
############### 請選擇功能 0Start._index()
def _index():
    #print ('開始執行_Start')

    # 說明
    Talk = [
        '\n   =========== AutoWeb index 歡迎您 ===========',
        '\n   請選擇功能\n',
        '\n   0 ====== RunThePY\n   開始執行同層的其他py檔\n',
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
            print (' / END',_RunThePY(),'.py')
            print ('********** /Sel 0 *************') 





        ################################## /Sel END
        continue    # All sel 回 Goto Fun loop 







































































# 可選功能 ###########################################################################
###################################################################################


##################################################
##################################################
##################################################
##################################################
############### 開始執行同層的py檔 0Start._RunThePY()
def _RunThePY():

    # 預設run
    BasePY = 'ATWError'

    # 說明
    Talk = [
        ' Start._RunThePY()  ',
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
##################################################
##################################################
##################################################
############### /開始執行同層的py檔 0Start._RunThePY()








##################################################
##################################################
##################################################
##################################################
############### AutoWeb 文字轉list



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


##################################################
##################################################
##################################################
##################################################
############### /AutoWeb 文字轉list










##################################################
##################################################
##################################################
##################################################
############### ATWFolder

'''
        '_SetFolder(v1,sel) =\n        生成文件夾',
        '_GetFolder() =\n        獲取檔案路徑和當前工作目錄',
        '_MakeJobFolder(FolderName) =\n        在當前文件夾创工作目錄',
        ' ==== 恭賀新禧 ==== ',
'''



###################################################################################
################################################################ AutoWeb 生成文件夾
def _SetFolder(v1,sel):     #   (文件夾名,動作)
    #print ('_SetFolder\n'+ str(v1) +'\n')
    
    # MakeFolder = MakeFolder
    if sel == 'MakeFolder':
        # 查 文件夾 在否       ./NOW
        folder = os.path.exists(v1)
        if not folder:
            os.makedirs(v1)    # makedirs　文件夾不在创，在ＥＲＲＯＲ
            print ("\n*** 成功创建文件夾 ",v1," ***\n")

            #_AutoWebLanguageSetting("\n***!!成功创建文件夾!!!!!*****\n")
            #print (Talk0,LanguageText,v1)


###################################################################################
######################################################### 獲取檔案路徑和當前工作目錄
# https://www.delftstack.com/zh-tw/howto/python/python-get-path/

def _GetFolder():
    # print ('_GetFolder')
    NowFolder = (os.path.dirname(os.path.abspath(__file__)))

    #print ('_GetFolder,',NowFolder)
    return NowFolder



###################################################################################
############################################################# 在當前文件夾创工作目錄
def _MakeJobFolder(FolderName): 
    # 要創的文件夾名 = FolderName

    # 獲取當前工作目錄
    NowFolder = _GetFolder()

    # 文件夾 全名
    NowJobFolder = NowFolder + '\\' + FolderName

    # 创文件夾 if 冇
    _SetFolder(NowJobFolder,'MakeFolder')

    return NowJobFolder



##################################################
##################################################
##################################################
##################################################
############### /ATWFolder











# /可選功能 ###########################################################################
###################################################################################























































##################################################
##################################################
##################################################
##################################################
############### ATW_LoginATW


###################################################################################
############################################################ AutoWeb 檢查ATW密文在否
def _LoginATW(ATWKeyName,UserKey):     #   ('ATWKeyname-@=',UserKey) ('fbac,',UserKey) ('fbpw,',UserKey)
    #print ('Key\n'+ str(Key) +'\n')

    # Key 轉 sha256 ATW加密KEY
    Key2 = UserKey + '.'
    _ChgCodeAll(999,Key2,256)       #   (999,UserKey+ATWKey,動作)
    UserKey256 = tttKey

    #檢查ATW密文在否，如不在，先記錄再登入
    if not os.path.isfile(密匙檔路徑):       #     AutoWeb/0.atw不在
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
################################################################ AutoWeb 解碼ATW密文
# UnLockData = 0
def _UnLockATW(sha256Key,ATWKeyName):     #   (Key256,ATWKeyName) v1,v1,v2,sel)
    # global UnLockData

    Talk = [
        '密匙錯誤',
        '請先將您的ATW密文修改為  0.atw ',
        '方可登入',

        '您必須在可信的地方另外備份，以防意外丟失',
        '因ATW密匙、ATW密文一旦丟失將永不能復原',
        'n其所有資產也將永遠消失'
    ]
    
    # 重置 UnLockData
    UnLockData = '沒有NODATA內容'

    # 打開文件 解碼
    for i in open(密匙檔路徑, 'r', encoding='UTF-8'):
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
        for txt in Talk:
            print (txt)
        print ('\n ***************** \n')
        # 重新開始
        UserInputDatart()

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
    return UnLockData






###################################################################################
################################################################# AutoWeb 生成文字檔
def _SaveData(Key256,v1,v2,sel):     #   (Key256,'所,有,前,值,新值名,',v2,sel)

    if sel == 'JOB':
        #保存文件                #   '帖時_帖主ID_帖主名_關鍵字_帖文'
        with open(v2, 'a', encoding="utf-8") as kf:
            kf.write(v1)
        kf.close()
        #print ('\n!!!!!已保存!!***\n'+str(v2))
        
        print ('\n   *** 已保存內容 ***\n' + str(v1))
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
            KU1 = (密匙檔路徑.split("/")[0]) #   'AutoWeb'
            KU2 = (密匙檔路徑.split("/")[1]) #   '0.atw'
            DF2 = KU1 + '/' + time.strftime('%Y%m%d%H%M%S') + KU2
        if sel == '0.atw':
            DF2 = 密匙檔路徑


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
                if not os.path.isfile(密匙檔路徑):
                    print ('\n   *** 請先將密文檔名修改為 0.atw 再繼續 ***\n')
                    os.system("pause")
                    continue
                break





##################################################
##################################################
##################################################
##################################################
############### /ATW_LoginATW




































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
    UserInputDatart()





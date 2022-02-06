




'''
winpy3

AutoWeb 檢查ATW密文在否
ATW_LoginATW
ATW202202042022
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-

import hashlib  # sha256
import binascii # binascii加密可解
import math #
import random
import time

import ATWREADME
import ATWTxtAndList



###################################################################################
############################################################# AutoWeb 檢查ATW密文在否
def README(): 

    ThisREADME = [
        '*** ATW_LoginATW.README ***', # PYfileName
        'AutoWeb 檢查ATW密文在否 =\n         _LoginATW(ATWKeyName,UserKey)',
        'AutoWeb 加密解密 =\n         _ChgCodeAll(Key,ttt,nb)',
        'AutoWeb 生成文字檔 =\n         _SaveData(Key256,v1,v2,sel,JobFolder2)',
        
        
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202051218',
        'https://98672794.github.io/'
    ]

    ATWREADME._READYourME(ThisREADME)










###################################################################################
############################################################ AutoWeb 檢查ATW密文在否
def _LoginATW(ATWKeyName,UserKey,JobFolder):     #   ('ATWKeyname-@=',UserKey) ('fbac,',UserKey) ('fbpw,',UserKey)
    #print ('Key\n'+ str(Key) +'\n')

    # Key 轉 sha256 ATW加密KEY
    Key2 = UserKey + '.'# Key
    UserKey256 = _ChgCodeAll(999,Key2,256)       #   (999,UserKey+ATWKey,動作)
    

    #檢查ATW密文在否，如不在，先記錄再登入
    if not ATWREADME.os.path.isfile(JobFolder):       #     AutoWeb/0.atw不在
        
        #   開新AC 去記錄
        _SaveData(UserKey256,ATWKeyName,UserKey,'NEW',JobFolder)    #   (Key256,'ATWKeyname-@=',UserKey,sel)

        #   記Key256 去記錄2
        _LoginATW('ALL',UserKey,JobFolder)
        Dt = str(UnLockData+'ATWKey256-@=')
        #print ('保存文件\n'+ str('\n'+Dt+UserKey256+'\n') +'\n')
        _SaveData(UserKey256,Dt,UserKey256,'0.atw',JobFolder)    #   (Key256,'ATWKeyname-@=',UserKey,sel)
        _LoginATW('ATWKeyname-@=',UserKey,JobFolder)

    _UnLockATW(UserKey256,ATWKeyName,JobFolder)  #   (Key256,要取的ATWKeyName,JobFolder) _UnLockATWv1,_UnLockATWv2,_UnLockATWsel)











































###################################################################################
################################################################### AutoWeb 加密解密
#tttKey = 0
#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#_ChgCodeAll#密碼生成
def _ChgCodeAll(Key,ttt,nb):     #   (sha256Key,加密內容,動作)
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
    return tttKey






















###################################################################################
################################################################ AutoWeb 解碼ATW密文
#UnLockData = 0
def _UnLockATW(sha256Key,ATWKeyName,JobFolder3):     #   (Key256,ATWKeyName) v1,v1,v2,sel)
    global UnLockData
    
    # 重置 UnLockData
    UnLockData = '沒有NODATA內容'

    # 打開文件 解碼
    for i in open(JobFolder3, 'r', encoding='UTF-8'):
        d1 = i

    # 解密30 偽隨機打亂
    _ChgCodeAll(sha256Key,d1,30)       #   (sha256Key,ATW密文,動作)

    #驗證內容碼
    try:
        # 解密160 binascii
        tttKey5 = _ChgCodeAll(999,tttKey,160)       #   (999,160密文,動作)
    except:
        # 解密錯誤
        print ('\n ***************** \n')
        ATWTxtAndList._StrToList('密匙錯誤===請先將您的ATW密文修改為===方可登入','===')

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
        ATWTxtAndList._StrToList(tttKey,'\n')
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

    #return UnLockData






















































###################################################################################
################################################################# AutoWeb 生成文字檔
def _SaveData(Key256,v1,v2,sel,JobFolder2):     #   (Key256,'所,有,前,值,新值名,',v2,sel,JobFolder2)

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
        tttKey2 = _ChgCodeAll(999,Dt,16)       #   (999,保存的內容,動作)

        #加密3 偽隨機打亂
        tttKey3 = _ChgCodeAll(Key256,tttKey2,3)     #   (sha256Key,16內容,動作)

        #新文件名
        if sel == 'NEW':
            KU1 = (JobFolder2.split("/")[0]) #   'AutoWeb'
            KU2 = (JobFolder2.split("/")[1]) #   '0.atw'
            DF2 = KU1 + '/' + time.strftime('%Y%m%d%H%M%S') + KU2
        if sel == '0.atw':
            DF2 = JobFolder2


        #print ('保存文件\n'+ str(tttKey) +'\n')
        #保存文件                #   'AutoWeb/time0.atw'
        with open(DF2, 'w', encoding="utf-8") as kf:
            kf.write(tttKey3)
        kf.close()

        #print ('\n!!!!!已保存 '+str(DF2)+' !!***\n')
        #print ('\n!!!!!內容!!***\n' + str(Dt) + '\n!!***\n')

        if sel == 'NEW':
            #檢查ATW密文檔
            while True:
                if not ATWREADME.os.path.isfile(JobFolder2):

                    TrueList = ATWTxtAndList._StrToList('請先將===密文名修改為===再繼續','===')
                    print ('\n   ***',TrueList[0],'ATW',TrueList[1],'0.atw',TrueList[2],'***\n')
                    ATWREADME.os.system("pause")
                    continue
                break




















































if __name__ == "__main__":
    README()
    
    



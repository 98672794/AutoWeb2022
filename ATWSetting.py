#!/usr/bin/env python

# -*- coding: UTF-8 -*-




###################################################################################
############################################################# ATWSetting 說明
def README(): 
    ThisREADME = '''
win py3
            _\|/_
            (o o)
    +----oOO-{_}-OOo--------------------------+
    |                                         |
    |                                         |
    |        202202130852                     |
    |        ATWSetting.py                    |
    |        修改您的資料                      |
    |         ------------------------        |
    |         ------------------------        |
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
0000

'''
    print(ThisREADME)

















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
                InputData()   # QQQQQQQQQQQQ 




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































if __name__ == "__main__":
    README()
    
    

















'''
自動覆客_OK 202111272338

時K時唔K
loop很煩        if Loop1 % 10 == 0:
睇錯 314         # 睇錯 202111272338  See_UserAutoReWs客自Loop See_LoopForGetUser我等客Loop


---------------------------------------


ATW  自動覆客202109252002OK OK

**************************

開始私測 202109252002OK

暫可3開
試user loop

******************************
自動覆客.py

自動覆
wts ig fb

我是主機
用網頁set
我登佢登
我auto



202109211446

用:

a =9867
ai=5525 all
a(ai(AdminTxt,key))
ai=run





######################################################


txt


importfrom


BassData        QQ


Fun
    1                   AdminLoginWTS                      admin login whatsapp     202109122207

    2                   _LoopForGetUser                                等客Loop     202109122207    Q

    2A        User ReplyKeyList Ws   =  User自動覆客機器人 系列
        2.A.1           _UserLogin                客戶用ReplyKeyList wts AI動作
            2.A.1.1     _GetUserTel                                    取手機號     202109122207
            2.A.1.2     _UL_Gt_QR                               開 User ws 截圖     202109122207
            2.A.1.3     _UL_Sn_QR                             SEND QR User 登入     202109120449

        2B              _ALL_Reply                        客戶wts我 AI回覆     202109122207

    共用動作 系列
    3                   _InputWsTxt          續句寫入 wts 對話 \n = SHIFT ENTER     202109130420
    4                   _OutTehTalk                                    退出對話     202109130420


    return 系列
    5                   _UserReplyKeyListMake                    分析 User 指令     202109120449
    6                   _MakeAdminTxt                           Make Admin 指令     202109010117


自動覆客機器人   ReplyKeyList


User    ReplyKeyList    9867


Ran



OutCode





######################################################

'''















































import sys

# 202111232107 OK
#sys.path.append('C:\\Users\\mokaki\\Desktop\\搵工易')
sys.path.append('..\\搵工易')
import ATW
import ATWFileList
import ATWReadFile
import ATWGetListKeyTxt
import ATWSteChrome
import ATWFolder

import ATWTime  # 202111272338


from pickle import FALSE
import time
import os
from types import CodeType


import threading






































JobCont='自動覆客_OK'  # 当前路径当前路径当前路径当前路径
KeyFolder = '_atw'
UrlName='https://web.whatsapp.com/'






AdminSetBtn=0#True
def RunThisPY():  
    # admin
    if AdminSetBtn == 0:
    #    Test()
    #else:
        # 正常
        AdminLoginWTS()
    ATW._OUT









def Test():    
    print('*** Test *** ')

    uuu='https://stackoverflow.com/questions/52342854/share-image-on-whatsapp-using-selenium-java'
    eqe='//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[1]/div'


    ATWSteChrome._SteChrome(KeyFolder,'chrome')
    ATWSteChrome.chrome.get(UrlName)
    ttt = ATWSteChrome.chrome.find_element_by_xpath(eqe).text
    print('chrome,',ttt)

    ATW._OUT

    ATWSteChrome._SteChrome(KeyFolder,'chrome1')
    ATWSteChrome.chrome1.get(uuu)
    ttt3 = ATWSteChrome.chrome1.find_element_by_xpath(eqe).text
    print('chrome,',ttt3)


    ATWSteChrome._SteChrome(KeyFolder,'chrome2')
    ATWSteChrome.chrome2.get(uuu)
    tt54t = ATWSteChrome.chrome2.find_element_by_xpath(eqe).text
    print('chrome,',tt54t)









#   1   Admin Login wts 202109122207
def AdminLoginWTS():    

    print('*** 1AdminLoginWTS *** ')

    # 获取当前路径
    project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))

    #### 在當前文件夾创工作目錄 if not ###
    # # C:\\Users\\mokaki\\Desktop\\搵工易
    ATWFolder._MakeJobFolder("..\\"+JobCont+"\\"+KeyFolder+"\\Uqr")

    #selenium chrome 配置
    ATWSteChrome._SteChrome(KeyFolder,'chrome')

    # admin login whatsapp
    ATWSteChrome.chrome.get(UrlName)

    # 點個人檔案    c1
    CheckPoint1 = "chrome.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[1]/div/img').click()"
    #   您的名字    c2 c3 
    CheckPoint20 = "chrome"
                    #//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]
    CheckPoint21 = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]'  
    Talk1 = '請admin 登入whatsapp 852 5525 8378'
    Talk2 = '歡迎您'

    # 去login.py
    ATWSteChrome._LoopAndCheck(CheckPoint1,CheckPoint20,CheckPoint21,'0','c5',Talk1,Talk2,'t3','t4','t5','WAR1')
    # F5
    ATWSteChrome.chrome.refresh()

    if __name__=='__main__':


        # 睇錯 202111272338 
        while True:
            try:
                # 回等客Loop
                _LoopForGetUser()
            except Exception as e:
                _Error(e)
                continue
        





























See_LoopForGetUser我等客Loop = 'No data!!!See_LoopForGetUser我等客Loop'
#   2 等客Loop 202109122207     
def _LoopForGetUser():
    global AdminTxtOK
    global See_LoopForGetUser我等客Loop

    print('*** 2_LoopForGetUser *** ')

    # 生成 admin指令 #############
    ATAllOK=_MakeAdminTxt()
    AdminTxtOK=[]
    i = 0
    try:
        while i < len(ATAllOK):

            # i = 客戶說:
            AdminTxtOK.append(ATAllOK[i]) 

            # ii = AI回覆:
            ii = i+1
            # 轉換行
            UsTxtList00 = str(ATAllOK[ii]).replace("@@","\n")
            # 轉 @+@ @@ ',' .,.
            UsTxtList00 = str(UsTxtList00).replace("@+@","@@").replace("','",".,.")
            AdminTxtOK.append(UsTxtList00)

            i+=2
    except:
        pass


    Loop1 = 1   # 等客來loop數
    while True:
        #print('333')

        #   先取User內容  '.,.' #############
        UserReplyKeyList='//span[contains(text(),".,.")]'
        try:
            DialogueList = ATWSteChrome.chrome.find_element_by_xpath(UserReplyKeyList).text.lower()
            if DialogueList:
                #print('aa3a=',UserReplyKeyList)

                #   分析 User 指令
                ReUsTxt = _UserReplyKeyListMake(DialogueList)

                #print('    *** goto User Login000 *** ')
                #os.system("pause")

                # 202111232107 qqq
                try:
                    #   goto User Login
                    _UserLogin(UserReplyKeyList,ReUsTxt)
                except Exception as e:
                    # F5
                    ATWSteChrome.chrome.refresh()
                    _Error(e)
                    continue
        except:
            pass


        # 再取 admin指令 i=客戶說 ii=AI回覆 #############
        i = 0
        while i < len(AdminTxtOK):

            ii = i+1    # AI回覆
            #   任何新對話中有 客戶說 = 開始自回 不能有' '
            aaa = AdminTxtOK[i].replace(' ','')

            # 找 小草 Key
            aaa = aaa.lower()
            ReplyDataKeyRKL = '//span[contains(text(),"'+aaa+'")]'
            try:
                DialogueList = ATWSteChrome.chrome.find_element_by_xpath(ReplyDataKeyRKL).text.lower()

                if DialogueList:
                    if not '.,.' in DialogueList:
                        #print('a1aa=',aaa)
                        UKey = ReplyDataKeyRKL  # 點位置
                        UKey0 = AdminTxtOK[ii]     # AI回覆
                        #   goto AI回覆
                        #print('    *** goto AI回覆1 *** ')
                        #os.system("pause")
                        _ALL_Reply(UKey,UKey0,'chrome')
            except:
                # 找 大草 Key
                aaa2 = aaa.upper()
                ReplyDataKeyRKL = '//span[contains(text(),"'+aaa2+'")]'
                #print('aaa=',aaa)
                try:
                    DialogueList = ATWSteChrome.chrome.find_element_by_xpath(ReplyDataKeyRKL).text.lower()
                    
                    if DialogueList:
                        if not '.,.' in DialogueList:
                            #print('aa2a=',aaa)
                            UKey = ReplyDataKeyRKL  # 點位置
                            UKey0 = AdminTxtOK[ii]     # AI回覆
                            #   goto AI回覆
                            #print('    *** goto AI222回覆 *** ')
                            #os.system("pause")
                            _ALL_Reply(UKey,UKey0,'chrome')
                except:
                    pass
            i+=2

        # loop很煩 10位先出
        if Loop1 % 100 == 0:
            # 沒有任何人 sn 任何指令比我
            print('   已到帳 *** ',Loop1,' 億 *** 港元')
        
        # 睇錯用 202111272338
        See_LoopForGetUser我等客Loop = '   已到帳 *** ',Loop1,' 億 *** 港元'

        Loop1+=1    # 等客來loop數+1


        # ADMIN SET ### 
        if AdminSetBtn == True:
            if Loop1>5:
                print('`````````````````````等客Loop ADMIN SET````````````````````````````')
                os.system("pause")

        continue























# 2A        User ReplyKeyList Ws  =  User自動覆客機器人 系列 #####################################################################
####################################################################################






# 客戶登錄ws仔  202111272338 

# User Chrome 配置 計
UserChromeCont=1

# 2.A.1    客戶登錄ws仔
def _UserLogin(UKey,Txt):

    global UserChromeCont

    print('*** 2.A.1    客戶登錄ws仔 *** ')

    #   點入User對話
    #效 = ATWSteChrome._Loop數停('chrome',UKey,'click','0')
    #_Error回_LoopForGetUser(效)

    while True:
        Error數 = 0
        try:
            ATWSteChrome.chrome.find_element_by_xpath(UKey).click()
            break
        except:
            Error數+=1
            if Error數 == 10:
                # 回等客Loop
                _LoopForGetUser()
            #print('點入User對話')
            time.sleep(2)
            continue


    # 「自動刪除訊息」功能已開啟    
    das='//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/div/div/div/div[2]/div'
    try:
        ATWSteChrome.chrome.find_element_by_xpath(das).click()
    except:
        pass

    # 指令OK 
    if Txt[1]:

        if Txt[0] == ' ':
            print('xxx 指令錯誤')
            # 如何使用自動覆客機器人" 
            _InputWsTxt(AdminTxtOK[3],1,1,'chrome')
            #   退出對話
            _OutTehTalk('chrome')

        #   取手機號
        UserTel = _GetUserTel()
        # 查是群 202111272338
        if UserTel == '不可以在群組執行ws仔\n請用個人帳號再試':
            _InputWsTxt(UserTel,1,0,'chrome')
            _OutTehTalk('chrome')
            _Error回_LoopForGetUser('沒')

        #print('UserTel:',UserTel)
        #os.system("pause")

        # 轉換所有對話 User確定
        UserTxtB =[]
        i = 0
        try:
            while i < len(Txt):
                Us='客戶說: '+str(Txt[i])+'\n'
                UserTxtB.append(Us)
                ii = i+1
                As = 'AI回覆: \n'+str(Txt[ii])+'\n'
                UserTxtB.append(As)
                UserTxtB.append('\n----\n')
                i+=2
        except:
            pass

        # 登入提示
        txt = '請於10秒內，用B設備掃QR，受權機器人登入。'
        txt2 = '請驗證指令，如錯誤，登出已連結裝置，重試'

        # 刪廢字 轉句
        UserTxtB[-1] = txt2

        # 一句一行
        _InputWsTxt(txt,1,0,'chrome')

        # Chrome1,2,3,4...
        ThisUserChromeCont = 'chrome'+str(UserChromeCont)
        #print('ThisUserChromeCont,',ThisUserChromeCont)

        # 開 User ws UserTel=QR.img
        UserWsQR=_UL_Gt_QR(UserTel,ThisUserChromeCont)

        # send QR圖 QQ 不能動
        _UL_Sn_QR(UserWsQR,txt)

        # 等 User Login 15秒冇loop  
        txt=_UL_Lg(ThisUserChromeCont)

        UserChromeCont+=1   # QQ

        if txt == '登入成功':
            # 一句一行
            _InputWsTxt(txt,1,0,'chrome')
            _OutTehTalk('chrome')

            # 2Fun同時執行 多线程   ####################
            _TwoFunRun(Txt,UserTxtB,UserTel,ThisUserChromeCont)

        if txt == '登入超時':
            # 登入超時,如何使用自動覆客機器人" 
            das = txt+'\n\n'+AdminTxtOK[3]
            _InputWsTxt(das,1,1,'chrome')
            #   退出對話
            _OutTehTalk('chrome')

    # 指令錯誤
    else:
        print('xxx 指令錯誤')
        # 如何使用自動覆客機器人" 
        _InputWsTxt(AdminTxtOK[3],1,1,'chrome')
        #   退出對話
        _OutTehTalk('chrome')

    # 回LOOP ###










def _TwoFunRun(Txt,UserTxtB,UserTel,ThisUserChromeCont):
            # 2Fun同時執行 多线程 ************************************************
    
            # QQ t+UserChromeCont ************************************************
            t1 = threading.Thread(target=_UserAutoReWs,args=(Txt,UserTxtB,UserTel,ThisUserChromeCont,))
    
            t1.start()











See_UserAutoReWs客自Loop = 'No data!!!See_UserAutoReWs客自Loop'
def _UserAutoReWs(User_Txt,UserTxtB,UserTel,chromeSel593):
    global See_UserAutoReWs客自Loop

    print('\n   *** _UserAutoReWs')

    #  回 Admin 登入成功

    # eval 轉 chrome
    BB1=eval((str('ATWSteChrome.')+str(chromeSel593)))

    BB1.set_window_size(200,200)

    # get 入對話
    OK='https://web.whatsapp.com/send?phone=85255258378'
    BB1.get(OK)
    time.sleep(2)

    # list 續句寫入
    _InputWsTxt(UserTxtB,0,0,chromeSel593) 

    #User Data
    ReData=chromeSel593+','+UserTel+'\n'+UserTxtB[-1]

    # 補尾句
    _InputWsTxt(ReData,1,0,chromeSel593)

    #   退出對話
    _OutTehTalk(chromeSel593)

    # User 等客來loop數
    Loop1 = 1   
    while True:

        # 取 User指令 i=User客戶說 ii=User回覆 #############
        i = 0
        while i < len(User_Txt):

            ii = i+1    # AI回覆
            #   任何新對話中有 客戶說 = 開始自回 不能有' '
            aaa = User_Txt[i].replace(' ','')

            # 找 小草 Key
            aaa = aaa.lower()
            ReplyDataKeyRKL = '//span[contains(text(),"'+aaa+'")]'
            try:
                DialogueList = BB1.find_element_by_xpath(ReplyDataKeyRKL).text.lower()

                if DialogueList:
                    #print('a1aa=',aaa)
                    U2Key = ReplyDataKeyRKL  # 點位置
                    U2Key0 = User_Txt[ii]     # AI回覆
                    #   goto AI回覆
                    #print('    *** goto AI回覆1 *** ')
                    #os.system("pause")
                    _ALL_Reply(U2Key,U2Key0,chromeSel593)
                #break
            except:
                # 找 大草 Key
                aaa2 = aaa.upper()
                ReplyDataKeyRKL = '//span[contains(text(),"'+aaa2+'")]'
                #print('aaa=',aaa)
                try:
                    DialogueList = BB1.find_element_by_xpath(ReplyDataKeyRKL).text.lower()
                    
                    if DialogueList:
                        #print('aa2a=',aaa)
                        UKey = ReplyDataKeyRKL  # 點位置
                        UKey0 = User_Txt[ii]     # AI回覆
                        #   goto AI回覆
                        #print('    *** goto AI222回覆 *** ')
                        #os.system("pause")
                        _ALL_Reply(UKey,UKey0,chromeSel593)
                    #break
                except:
                    pass
            i+=2

        # User Loop 計數

        if Loop1 % 100 == 0:
            # 沒有任何人 sn 任何指令比我
            print('   ````````````````````` ',chromeSel593,UserTel,Loop1,' 次`````````````````````')

        # 睇錯用 202111272338
        See_UserAutoReWs客自Loop = '   ````````````````````` ',chromeSel593,UserTel,Loop1,' 次`````````````````````'
        Loop1+=1    # 等客來loop數+1

        #  如 User 登出 關 chrome
        try:
            # 如找到刷碼頁的位
            UserIfOut = BB1.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div').text
        except:
            try:
                UserIfOut = BB1.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div').text
            except:
                pass
        try:
            if UserIfOut:
                print('`````````````````````',chromeSel593,UserTel,Loop1,' User 登出 ````````````````````````````')
                See_UserAutoReWs客自Loop = '`````````````````````',chromeSel593,UserTel,Loop1,' User 登出 ````````````````````````````'
                BB1.close()
                break
        except:
            # ADMIN SET ### 
            if AdminSetBtn == True:
                if Loop1>5:
                    print('`````````````````````',chromeSel593,UserTel,Loop1,'_UserAutoReWs ADMIN SET````````````````````````````')
                    os.system("pause")
            continue


































# 2.A.1.4     _UL_Lg                                    等 User Login
def _UL_Lg(chromeSel646):
    print('*** 2.A.1.4     _UL_Lg                                    等 User Login   *** ')

    BB1=eval((str('ATWSteChrome.')+str(chromeSel646)))

    #   點個人檔案
    cont=0
    while True:
        try:
            BB1.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[1]/div/img').click()
                                                        
            break
        except:
            print('等 User Login :',cont)
            time.sleep(1)
            
            cont+=1
            if cont == 15:
                break
            
            continue

    if cont < 15:
        txt = '登入成功'
        # F5
        BB1.refresh()
    else:
        txt = '登入超時'
        # close
        BB1.close()

    return txt

















#   2.A.1.0    SEND QR User 登入    202109120449
def _UL_Sn_QR(img,txt):

    print('*** _UL_Sn_QR *** ')

    # send img

    # 202109211559  常手轉 QQQ
    d202111242300 = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div'

    a=d202111242300
    b='/span/div[1]/div/ul/li[1]/button/span'


    while True:
        try:
            # 點附件功能
            ATWSteChrome.chrome.find_element_by_xpath(a).click()
            break
        except:
            print('點附件功能')
            time.sleep(2)
            continue

    while True:
        try:
            # 點開sn圖功能
            zz=a+b
            ATWSteChrome.chrome.find_element_by_xpath(zz).click()
            break
        except:
            print('點sn圖')
            time.sleep(2)
            continue

    # 關附窗.exe
    # https://www.cnblogs.com/chongyou/p/7065462.html
    #os.startfile("C:\\Users\\mokaki\\Desktop\\job2021\\"+JobCont+"\\"+KeyFolder+"\\CloseFW.exe")
        
    # 获取当前路径
    project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
    os.startfile(project_path+"\\"+JobCont+"\\"+KeyFolder+"\\CloseFW.exe")
    print('關附窗')

    while True:
        try:
            # 要sn的圖
            ATWSteChrome.chrome.find_element_by_tag_name('input').send_keys(img)  
            break
        except:
            print('sn圖')
            time.sleep(2)
            continue

    while True:
        try:
            # 填圖片文字
            for part in txt.split('\n'):
                ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(part)
                ATWSteChrome.ActionChains(ATWSteChrome.chrome).key_down(ATWSteChrome.Keys.SHIFT).key_down(ATWSteChrome.Keys.ENTER).key_up(ATWSteChrome.Keys.SHIFT).key_up(ATWSteChrome.Keys.ENTER).perform()

            # 點sn鍵
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys('\n')
            break
        except:
            time.sleep(2)
            continue

    # 202109221204 允許使用鏡頭 
    while True:
        try:
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/span[2]/div[1]/div/div/div/div/div/div/div[4]/div/div/div').click()
            break
        except:
            print('允許使用鏡頭 202109221204')
            break
    print('允許使用鏡頭END')





















































# 動作+return 系列 #####################################################################









#   2.A.1.1     _GetUserTel                                    取手機號     202109122207
def _GetUserTel():

    print('--- UserTel ')

    #   點名開info
    while True:
        try:
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span').click()
            break
        except:
            #print('點名開info')
            time.sleep(2)
            continue


    # 查是群 = '刪除對話' = ok 202111272338 
    try:
        查是群 = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[7]/div[1]/div[2]/div/span').get_attribute("textContent")
    except:
        查是群 = 'NO_NO'

    #print('查是群,',查是群) #封鎖我司(華麗
    #os.system("pause")

    if 查是群 == '退出群組':
        UserTel = '不可以在群組執行ws仔\n請用個人帳號再試'
    else:   # 查是群 == '刪除對話'

        #   取手機號
        while True:
            try:
                UserTel = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[*]/div[3]/div/div/span/span').get_attribute("textContent")
                break
            except:
                #print('取手機號')
                time.sleep(2)
                continue

        #   關info
        while True:
            try:
                ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button').click()
                break
            except:
                #print('關info')
                time.sleep(2)
                continue

    return UserTel








# 2.A.1.2     _UL_Gt_QR                               開 User ws 截圖     202109122207
def _UL_Gt_QR(UserTel,chromeSel):    

    UserTel = UserTel.replace(' ','')
    print('--- QRImg ')

    #selenium chrome 配置
    ATWSteChrome._SteChrome(KeyFolder,chromeSel)

    # eval 轉 chrome
    BB1=eval((str('ATWSteChrome.')+str(chromeSel)))

    BB1.set_window_size(414,900)

    # User login whatsapp
    BB1.get(UrlName)

    # 获取当前路径
    project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))

    # 隱式 等QR位置
    element = ATWSteChrome.WebDriverWait(BB1, 10, 0.5).until(ATWSteChrome.EC.presence_of_element_located((ATWSteChrome.By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas')),'解碼錯誤***[找不到 QR位置]***')


    # 截圖 Save 全畫面
    QRImg = project_path+"\\"+JobCont+"\\"+KeyFolder+"\\Uqr\\"+UserTel+".png"
    BB1.save_screenshot(QRImg)

    return QRImg





















# 共用動作 系列 #####################################################################




# 创建锁    好像有效
LockThis = threading.Lock()
#   2B              _ALL_Reply                        客戶wts我 AI回覆     202109122207
def _ALL_Reply(UKey,UKey0,chromeSel994):
    print('*** 2B _ALL_Reply *** ',chromeSel994)
    #  鎖定
    LockThis.acquire()

    #print('000 ')
    # eval 轉 chrome
    #BB1=eval((str('ATWSteChrome.')+str(chromeSel994)))
    #print('111 ')

    #   點入User對話
    #效 = ATWSteChrome._Loop數停(chromeSel994,UKey,'click','0')
    #_Error回_LoopForGetUser(效)

    #print('222 ')
    Error數 = 0
    while True:
        try:
            BB1=eval((str('ATWSteChrome.')+str(chromeSel994)))
            BB1.find_element_by_xpath(UKey).click()
            break
        except:
            Error數+=1
            print('Error數_ALL_Reply=',Error數)
            if Error數 == 3:
                # 回等客Loop
                _LoopForGetUser()

            #print('點入User對話')
            time.sleep(2)
            continue




    # 「自動刪除訊息」功能已開啟    QQQQQQQQ
    das='//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/div/div/div/div[2]/div'
    try:
        BB1.find_element_by_xpath(das).click()
    except:
        pass


    # 一句句寫入AI回覆
    _InputWsTxt(UKey0,1,1,chromeSel994)

    print(UKey0)

    #   退出對話
    _OutTehTalk(chromeSel994)


    # 释放
    LockThis.release()










# 3     續句寫入 wts 對話 \n = SHIFT ENTER  202109252108


def _InputWsTxt(txt,sel,sel2,chromeSel957):

    print('!!! _InputWsTxt *** ')

    #  選 chrome
    BB1=eval((str('ATWSteChrome.')+str(chromeSel957)))

    #  202111102306
    a0fd='//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
    a0d='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'

    # 等load完 202109252108 暫OK
    while True:
        try:
            aa=eval('BB1.find_element_by_xpath(a0d)')
            BB1.find_element_by_xpath(a0d)
            break
        except:
            print('更新ws send 位 = a0d')
            time.sleep(2)
            continue

    # send list
    if sel == 0:    
        # 一字一行
        i = 0
        while i < len(txt):
            for part in txt[i].split('\n'):
                aa.send_keys(part)
                #BB1.find_element_by_xpath(a0d).send_keys(part)
                ATWSteChrome.ActionChains(BB1).key_down(ATWSteChrome.Keys.SHIFT).key_down(ATWSteChrome.Keys.ENTER).key_up(ATWSteChrome.Keys.SHIFT).key_up(ATWSteChrome.Keys.ENTER).perform()
            print(txt[i])
            i+=1

    # send txt
    if sel == 1: 
        # 一句一行
        for part in txt.split('\n'):
            aa.send_keys(part)
            #BB1.find_element_by_xpath(a0d).send_keys(part)
            ATWSteChrome.ActionChains(BB1).key_down(ATWSteChrome.Keys.SHIFT).key_down(ATWSteChrome.Keys.ENTER).key_up(ATWSteChrome.Keys.SHIFT).key_up(ATWSteChrome.Keys.ENTER).perform()

    # 點sn鍵
    aa.send_keys('\n')
    #BB1.find_element_by_xpath(a0d).send_keys('\n')

    if sel2 == 1: 
        # 補尾句 防止 找到舊對話
        aa.send_keys('Thank you\n')







#   4 退出對話 202109130420
def _OutTehTalk(chromeSel1005):
    print('!!! _OutTehTalk ')

    #  選 chrome
    BB1=eval(('ATWSteChrome.'+chromeSel1005))

    # 點最後說話,離開輸入框
    time.sleep(2)
    #print('點最後說話,離開輸入框')
    LT= BB1.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[last()]')
    #print('LT',LT)
    BB1.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span').click()
    # F5
    BB1.refresh()


































# return 系列 #####################################################################






#   5   分析 User 指令      202109120449
def _UserReplyKeyListMake(txt):

    print('--- ReUsTxt ')


    ATW._StrToList(txt,'.,.')
    UsTxtList=ATW.TrueList[:]

    # 製作回覆內容
    ReUsTxt = []
    try:
        # 指令 錯誤 內容不足
        if not UsTxtList[1]:
            ReUsTxt = ['***指令 錯誤 內容不足 請從試 ***\n']
    except:
        print('\n   *** 指令 OK ***\n')

    # 記錄 ReUsTxt = ReplyKeyList
    i = 0
    try:
        while i < len(UsTxtList):

            # i = 客戶說:
            ReUsTxt.append(UsTxtList[i]) 

            # ii = AI回覆:
            ii = i+1
            # 轉換行
            UsTxtList00 = str(UsTxtList[ii]).replace("@@","\n")
            # 轉 @+@ @@ ',' .,.
            UsTxtList00 = str(UsTxtList00).replace("@+@","@@").replace("','",".,.")
            ReUsTxt.append(UsTxtList00)

            i+=2
    except:
        pass

    return ReUsTxt














#   6   Make Admin 指令 202109010117
def _MakeAdminTxt():

    print('--- ATAll ')
    


    AT1 = "ai.,. ',' ws仔 :@@Auto reply whatsapp 自動覆客機器人@@"                                                                                            
    AT2 = "    歡迎您@@"                                                                                            
    AT3 = "    @@"                                                                                            
    AT4 = "    您好!我係聊天機器人ws仔 ',' @@"                                                                                            
    AT5 = "    使您解放雙手! 毋須再條條回覆whatsapp訊息!@@"                                                                                            
    AT6 = "    只需簡單設定,我即刻可以幫您自動回覆信息!@@"                                                                                            
    AT7 = "    如果你說出神秘指令，我 ',' 可能會送禮物給您哦!@@"                                                                                            
    AT8 = "    @@"                                                                                            
    AT9 = "    ai = 歡迎@@"                                                                                            
    AT10 = "    @@"                                                                                            
    AT11 = "    a0 = 如何使用自動覆客機器人@@"                                                                                            
    AT12 = "    @@"                                                                                            
    AT13 = "    a1 = 私隱安全@@"                                                                                            
    AT14 = "    @@"                                                                                            
    AT15 = "    API = 配合whatsapp API 製作您的網上引流工具@@"                                                                                            
    AT16 = ".,."                                                                                            


    AT20 = "A0.,. ',' ws仔 :@@如何使用自動覆客機器人:@@"                                                                                            
    AT21 = "    @@"                                                                                            
    AT22 = "    1 您需要有 2 部可使用whatsapp的設備@@"                                                                                            
    AT23 = "    @@"                                                                                            
    AT24 = "    2 A設備發送 指令 啟動ws仔自動覆客機器人@@"                                                                                            
    AT25 = "    @@"                                                                                            
    AT26 = "    3 ws仔回覆受權QR Code@@"                                                                                            
    AT27 = "    @@"                                                                                            
    AT28 = "    4 B設備掃QR，受權ws仔登入您B設備的whatsapp@@"                                                                                            
    AT29 = "    @@"                                                                                            
    AT30 = "    5 通知您的客戶並使用它@@"                                                                                            
    AT31 = "    @@"                                                                                            
    AT32 = "    6 關閉機器人請在 whatsapp > 已連結裝置 > 登出@@"                                                                                            
    AT33 = "    @@"                                                                                            
    AT36 = "    *機器人不會記錄您任何資料，每次使用您必須從新提交指令@@"                                                                                            
    AT37 = "    *必須在一句對話內完成一組完整的指令"                                                                                            
    AT38 = "    @@"                                                                                            
    AT39 = "    *用','分開每項"                                                                                            
    AT40 = "    @@"                                                                                            
    AT41 = "    *用 @+@ 代替換行@@" 
    AT43 = "    指令範本:@@@@"   
    AT47 = "查詢','您好@+@請選','@@"
    AT48 = "query','Hello@+@Please select','@@"
    AT49 = "クエリ','こんにちは@+@選択してください',' @@"                                                                                            
    AT50 = "쿼리','안녕하세요@+@선택해주세요','@@"                                                                                            
    AT51 = "查询','你好@+@请选择','@@"    
    AT73 = ".,."     



    AT77 = "a1.,. ',' ws仔 :@@私隱安全:@@"                                                                                            
    AT78 = "@@"                                                                                            
    AT79 = "    您所有經過機器人的數據都已加密，@@"                                                                                            
    AT80 = "    除了您和信息接收者，@@"                                                                                            
    AT81 = "    任何人都無法解密查看原文。@@"                                                                                            
    AT82 = "@@"                                                                                            
    AT83 = "    您必須定期登出所有已連結裝置@@"                                                                                            
    AT84 = "    @@"                                                                                            
    AT85 = "    whatsapp > 設定 > 已連結裝置 > 登出@@"                                                                                            
    AT86 = "    @@"                                                                                            
    AT87 = "    這樣可保證機器人只有您需要時才可存取您的數據@@"                                                                                            
    AT88 = ".,."                                                                                            



    AT89 = "a2.,. ',' ws仔 :@@常見問題:@@"   
    AT90 = "@@"
    AT91 = "    如何一件登出所有已連結裝置?@@"    
    AT92 = "    whatsapp > 設定 > 已連結裝置 > 多裝置測試 > 加入測試 > 退出測試@@"
    AT93 = "    @@"
    AT94 = "    B設備掃QR，後不能啟動ws仔?@@"  
    AT95 = "    whatsapp > 設定 > 已連結裝置 > 多裝置測試 > 退出測試@@"
    AT96 = "    @@"
    AT97 = "    ws仔錯誤回覆信息?@@"  
    AT98 = "    聯絡人名稱和指令文字相同，請轉換指令或修改聯絡人名稱@@@@"

    AT99 = "    ws仔沒有回覆指令?@@"  
    AT100 = "    指令文字必須大小階相同@@"
    AT101 = "    每小時最小打開A設備的Whatsapp一次，已確保連線@@"
    AT102 = ".,."  


    AT143 = "API.,. ',' ws仔 :@@我可以配合whatsapp API 製作您的網上引流工具@@"                                                                                            
    AT144 = "whatsapp API@@"                                                                                            
    AT145 = "    https://wa.me/younb?text=ReplyKey@@"                                                                                            
    AT146 = "    @@"                                                                                            
    AT147 = "    https://wa.me/85298672794?text=我想制作網頁@@"                                                                                            
    AT148 = "    https://wa.me/85255258378?text=ai@@"                                                                                            
    AT149 = ".,."                                                                                            

    AT150 = "0aki.,.10秒後自爆.,."  


    # ReplyKeyList 轉換1
    # Admin ReplyKeyList 先=str
    ATNb = 1
    ATAllT=''

    while ATNb < 151:
        try:
            ATAllT = ATAllT + (eval(str('AT')+str(ATNb)))
        except:
            pass
        ATNb+=1


    # ReplyKeyList 轉換2
    # _Str To List .,.
    ATAll=[]
    ATW._StrToList(ATAllT,".,.")
    ATAll=ATW.TrueList[:]

    return ATAll







































'''     自動覆客機器人  ReplyKeyList


ai.,.Auto reply whatsapp 自動覆客機器人@@
    歡迎您@@
@@
    您好!我係聊天機器人ws仔 ',' @@
    使您解放雙手! 毋須再條條回覆whatsapp訊息!@@
    只需簡單設定,我即刻可以幫您自動回覆信息!@@
    如果你說出神秘指令，我 ',' 可能會送禮物給您哦!@@
@@
    ai = 歡迎@@
@@
    a0 = 如何使用自動覆客機器人@@
@@
    a1 = 私隱安全@@
@@
    API = 配合whatsapp API 製作您的網上引流工具@@
.,.



a0.,.如何使用自動覆客機器人:@@
@@
    1 您需要有 2 部可使用whatsapp的設備@@
@@
    2 A設備發送 指令 啟動ws仔自動覆客機器人@@
@@
    3 ws仔回覆受權QR Code@@
@@
    4 B設備掃QR，受權ws仔登入您B設備的whatsapp@@
@@
    5 通知您的客戶並使用它@@
@@
    6 關閉機器人請在 whatsapp > 已連結裝置 > 登出@@
@@
指令範本:@@
@@
    機器人不會記錄您任何資料，每次使用您必須從新提交指令@@
    必須在一句對話內完成一組完整的指令@@
@@
    用','分開每項
    @@
    用 @+@ 代替換行@@
@@
    1:@@
    ReplyKey','ReplyTxt','ReplyKey','ReplyTxt',' ...@@
    @@
    2:@@
    客給您的信息1','機器人動回覆的內容','@@
    客給您的信息2','機器人動回覆的內容2','@@
    ...@@
    @@
    3:@@
    ai','Auto reply whatsapp 自動覆客機器人@+@
    @@
    歡迎您@+@
    @@
    ...
    @@
    @+@
    @@
    ...@@
    @@
    ','
    @@
    a0','如何使用自動覆客機器人:@+@
    @@
    @+@
    @@
    1 您需要有...@+@
    @@
    ...
    @@
    @@
.,.



a1.,.私隱安全:@@
@@
    您所有經過機器人的數據都已加密，@@
    除了您和信息接收者，@@
    任何人都無法解密查看原文。@@
@@
    您必須定期登出所有已連結裝置@@
    @@
    whatsapp > 設定 > 已連結裝置 > 登出@@
    @@
    這樣可保證機器人只有您需要時才可存取您的數據@@
.,.



API.,.ws仔可以配合whatsapp API 製作您的網上引流工具@@
whatsapp API@@
    https://wa.me/younb?text=ReplyKey@@
    @@
    https://wa.me/85298672794?text=我想制作網頁@@
    https://wa.me/85255258378?text=ai@@
.,.

0aki.,.10秒後自爆





'''


















''' User ReplyKeyList 9867



it.,.Hello@@
   We are IT team from Hong Kong@@
@@
   Professional development：@@
   Blockchain, dapp, smart contract, erc721, ERC20, website, ios/android/wechat application, e-commerce@@
@@
   What are the details of you project?@@
   Your budget?@@
   Hope to finish time?@@
@@
   I am Mr. Mok@@
@@ 
   about us@@
   https://abta.work@@
.,.


科技券.,.科技券計劃旨在資助本地中小型企業使用科技服務和方案，以提高生產力或升級轉型。@@
該計劃於2019年2月27日被納入為創新及科技基金下一個恆常的資助計劃。@@
@@
申請資格：@@
• 1. 根據《商業登記條例》(第310章)在香港登記；@@
• 2. 在本港有實質業務運作 ，而該業務在提交申請時須與申請項目相關 。@@
@@
資助金額：@@
• 科技券計劃會以 3:1 的配對模式，向每間合資格企業最多可獲批6個項目最高 60 萬港元資助。@@
• 企業須以現金投入不少於核准項目總成本四分之一的資金。待項目審批完成後，政府會向申請企業發放核准資助。@@
• 每個項目一般應在12個月內完成。@@
資助範圍：@@
• 科技顧問服務@@
• 購買、租用或訂購訂製或現成的設備/硬件、軟件及科技服務或方案@@
• 包括訂購形式的科技服務或方案,例 如雲端服務、AI客戶服務@@
@@
• 預約安排及輪候管理系統@@
• 擴增實境技術系統@@
• 大數據及雲端分析方案@@
• 建築資訊模型系統@@
• 診所管理系統@@
• 網絡安全方案@@
• 文件管理及流動存取系統@@
• 電子庫存管理系統@@
• 電子採購管理系統@@
• 企業資源規劃方案@@
• 客戶關係管理系統@@
• 客戶及會員分析管理系統@@
• 人力資源管理系統@@
• 車隊管理系統@@
• 定位服務@@
• 物流管理系統@@
• 銷售點管理系統@@
• 快速回應管理系統@@
• 實時生產追蹤系統@@
• 協助企業符合生產標準的方案@@
@@
所需文件：@@
• 商業登記證副本、商業登記署表格 1(a) 或公司註冊處 (表格NAR1) 副本@@
• 實質業務運作證明文件@@
• 申請人身分證明文件副本@@
• 科技顧問的商業登記證副本@@
• 報價單副本@@
@@
科技券計劃申請指南：@@
https://www.itf.gov.hk/filemanager/tc/content_38/TVP-guide-c_202009.pdf
@@
.,.


tvp.,.The Technology Voucher Programme aims to subsidize local SMEs to use technology services and solutions to increase productivity or upgrade and transform.  @@
The plan was included as the next permanent funding plan of the Innovation and Technology Fund on February 27, 2019.  @@
@@
Petition form:@@
• 1. Registered in Hong Kong under the "Business Registration Ordinance" (Chapter 310); @@
• 2. There is a substantial business operation in Hong Kong, and the business must be related to the application project when submitting the application.  @@
@@
Funding:@@
• TVP will use a 3:1 matching model to grant each eligible company up to 6 projects with a maximum of 600,000 Hong Kong dollars in funding.  @@
• The enterprise must invest no less than one-fourth of the total cost of the approved project in cash.  After the approval of the project is completed, the government will issue approved grants to the applicant enterprises.  @@
• Each project should generally be completed within 12 months.  @@
Scope of funding: @@
• Technology Consultancy Service@@
• Purchase, rent or order customized or ready-made equipment/hardware, software and technology services or solutions@@
• Including subscription-based technology services or solutions, such as cloud services@@
@@
• Appointment arrangement and waiting management system@@
• Augmented Reality Technology System@@
• Big data and cloud analysis solution@@
• Building Information Modeling System@@
• Clinic Management System@@
• Network Security Solution@@
• Document Management and Mobile Access System@@
• Electronic inventory management system@@
• Electronic Procurement Management System@@
• Enterprise Resource Planning Scheme@@
• Customer Relationship Management System@@
• Customer and member analysis management system@@
• Human Resource Management System@@
• Fleet Management System@@
• positioning service@@
• Logistics Management System@@
• Point of Sale Management System@@
• Quick response management system@@
• Real-time production tracking system @@
• Assist the company to meet the production standards of the program@@
@@
needed file:@@
• Copy of Business Registration Certificate, Business Registration Office Form 1(a) or Company Registry (Form NAR1) Copy@@
• Substantive business operation certification documents@@
• A copy of the applicant’s identity document@@
• A copy of the business registration certificate of the technology consultant@@
• Copy of Quotation @@
Technology Voucher Programme Application Guide: @@
https://www.itf.gov.hk/filemanager/tc/content_38/TVP-guide-c_202009.pdf
@@
.,.


'''















































######################################################################################################
###################################################################################### 发生异常
def _Error(e):

    #### 在當前文件夾创_Error目錄 if not
    # # C:\\Users\\mokaki\\Desktop\\搵工易
    Error目錄名 = "..\\"+JobCont+"\\"+KeyFolder+"\\_Error"
    ATWFolder._MakeJobFolder(Error目錄名)

    現在時間 = ATWTime.NowIsTime()

    #print('-----')
    #print(e)
    #print(See_LoopForGetUser我等客Loop)
    #print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    #print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数
    #print('-----')
    E_Data = [
        '\n_Error=',e,
        '\n-----',
        '\n发生异常所在的文件=',(e.__traceback__.tb_frame.f_globals["__file__"]),
        '\n发生异常所在的行数=',(e.__traceback__.tb_lineno),
        '\n我等客Loop=',See_LoopForGetUser我等客Loop,
        '\n客自Loop=',See_UserAutoReWs客自Loop,
        '\n時間=',現在時間
    ]

    # Error目錄名轉字
    Error目錄名 == Error目錄名.replace('\\','/')
    # 创Error文件 一次一檔 
    创Error文件 = Error目錄名+ '/'+ 現在時間 + '.txt'
    ATWFolder._MakeJobFolder(创Error文件)   # qqqqqqqqqqqqqqqqqqqqqqqq

    for dd in E_Data:
        print(dd)
    print('-----')








def _Error回_LoopForGetUser(t):
    if t == '沒':
        # 回等客Loop
        ATWSteChrome.chrome.refresh()
        _LoopForGetUser()






























































# 執行本.py
if __name__=='__main__':
    RunThisPY()





















































































































































































































































































































































































































































































































































































































































def 不名_UserAutoReWs(User_Txt,UserTxtB,UserTel,chromeSel593):

    print('\n   *** _UserAutoReWs')

    #  回 Admin 登入成功

    # eval 轉 chrome
    BB1=eval((str('ATWSteChrome.')+str(chromeSel593)))

    # get 入對話
    OK='https://web.whatsapp.com/send?phone=85255258378'
    BB1.get(OK)
    time.sleep(2)

    # list 續句寫入
    _InputWsTxt(UserTxtB,0,0,chromeSel593) 
    # 補尾句
    _InputWsTxt(UserTxtB[-1],1,0,chromeSel593)
    #   退出對話
    _OutTehTalk(chromeSel593)



    # User 等客來loop數
    Loop1 = 1   
    while True:

        # 取 User指令 i=User客戶說 ii=User回覆 #############
        i = 0
        while i < len(User_Txt):

            ii = i+1    # AI回覆
            #   任何新對話中有 客戶說 = 開始自回 不能有' '
            aaa = User_Txt[i].replace(' ','')

            # 找 小草 Key
            aaa = aaa.lower()
            ReplyDataKeyRKL = '//span[contains(text(),"'+aaa+'")]'
            try:
                DialogueList = BB1.find_element_by_xpath(ReplyDataKeyRKL).text.lower()

                if DialogueList:
                    #print('a1aa=',aaa)
                    U2Key = ReplyDataKeyRKL  # 點位置
                    U2Key0 = User_Txt[ii]     # AI回覆
                    #   goto AI回覆
                    #print('    *** goto AI回覆1 *** ')
                    #os.system("pause")
                    _ALL_Reply(U2Key,U2Key0,chromeSel593)
                #break
            except:
                # 找 大草 Key
                aaa2 = aaa.upper()
                ReplyDataKeyRKL = '//span[contains(text(),"'+aaa2+'")]'
                #print('aaa=',aaa)
                try:
                    DialogueList = BB1.find_element_by_xpath(ReplyDataKeyRKL).text.lower()
                    
                    if DialogueList:
                        #print('aa2a=',aaa)
                        UKey = ReplyDataKeyRKL  # 點位置
                        UKey0 = User_Txt[ii]     # AI回覆
                        #   goto AI回覆
                        #print('    *** goto AI222回覆 *** ')
                        #os.system("pause")
                        _ALL_Reply(UKey,UKey0,chromeSel593)
                    #break
                except:
                    pass
            i+=2

        # User Loop 計數
        print('   ````````````````````` ',chromeSel593,UserTel,Loop1,' 次`````````````````````')
        Loop1+=1    # 等客來loop數+1

        #  如 User 登出 關 chrome
        try:
            # 如找到刷碼頁的位
            UserIfOut = BB1.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div').text
        except:
            try:
                UserIfOut = BB1.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div').text
            except:
                pass
        try:
            if UserIfOut:
                print('`````````````````````',chromeSel593,UserTel,Loop1,' User 登出 ````````````````````````````')
                BB1.close()
                break
        except:
            # ADMIN SET ### 
            if AdminSetBtn == True:
                if Loop1>5:
                    print('`````````````````````',chromeSel593,UserTel,Loop1,'_UserAutoReWs ADMIN SET````````````````````````````')
                    os.system("pause")
            continue




























AdminKey='ttt'
AdminTel='ttt'

# 客戶wts我 指定內容 開始 客戶login自動覆wts
def _UserAddMe():

    #   等客來
    _AutomaticReplyWTS()

    #   分析 指令
    _SeeReplyKeyList(DialogueList,UKey0)

    #   點2入User對話
    while True:
        try:
            ATWSteChrome.chrome.find_element_by_xpath(UKey).click()
            break
        except:
            #print('點入User對話')
            time.sleep(2)
            continue

    #   點名開info
    while True:
        try:
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span').click()
            break
        except:
            #print('點名開info')
            time.sleep(2)
            continue

    #   取手機號
    while True:
        try:
            UserTel = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[*]/div[3]/div/div/span/span').get_attribute("textContent")
            break
        except:
            #print('取手機號')
            time.sleep(2)
            continue

    #   關info
    while True:
        try:
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button').click()
            break
        except:
            #print('關info')
            time.sleep(2)
            continue



    # 點對話框
    #ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(" ")
    #os.system("pause")



    # Admin User 分流 tel岩
    if UserTel == AdminTel:
        _AdminSet()
    else:
        _UserSet()
    #   20210831
    '''
    if UKey0 == AdminKey:
        if UserTel == '+852 9867 2794':
            _AdminSet()
        else:
            print('\n   *** 有人扮admin ***\n')
            print('User手機號=\n   *** ',UserTel,' ***\n')
            # send 警告到 admin
            #_UserAddMe()
    if UKey0 == '.,.':
        _UserSet()
    else:
        print('\n   *** UKey0NO ***\n')
    '''


























#   等客來

def _AutomaticReplyWTS():
    global DialogueList
    global UKey
    global UKey0

    Loop100F5 = 0   # 等客來loop數

    UKey  = '0'     # 點位置
    UKey0 = '0'     # AI回覆
    DialogueList = '0'     # AI回覆


    while True:

        # 使用 指令 auto re ###真ATR
        if RKL_OK == True:
            # 取 指令 i=客戶說 ii=AI回覆
            i = 0
            try:
                while i < len(ReUsTxt):
                    ii = i+1    # AI回覆
                    #   任何新對話中有 客戶說 = 開始自回 不能有' '
                    aaa = ReUsTxt[i].replace(' ','')

                    # 找 小草 Key
                    ReplyDataKeyRKL = '//span[contains(text(),"'+aaa+'")]'
                    #print('ReplyDataKeyRKL=',ReplyDataKeyRKL)
                    try:
                        DialogueList = ATWSteChrome.chrome.find_element_by_xpath(ReplyDataKeyRKL).text.lower()

                        if DialogueList:
                            UKey = ReplyDataKeyRKL  # 點位置
                            UKey0 = ReUsTxt[ii]     # AI回覆
                            #   goto AI回覆
                            _AutoReWsByReplyKeyList(UKey,UKey0)
                    except:
                        # 找 大草 Key
                        aaa2 = aaa.upper()
                        ReplyDataKeyRKL = '//span[contains(text(),"'+aaa2+'")]'
                        try:
                            DialogueList = ATWSteChrome.chrome.find_element_by_xpath(ReplyDataKeyRKL).text.lower()
                            
                            if DialogueList:
                                UKey = ReplyDataKeyRKL  # 點位置
                                UKey0 = ReUsTxt[ii]     # AI回覆
                                #   goto AI回覆
                                _AutoReWsByReplyKeyList(UKey,UKey0)
                        except:
                            pass

                    finally:    # t e 都行 = +2
                        i+=2
            except:
                pass
                #print('指令 reply END')

        # 沒有 admin的 指令 
        else:
            print('請admin開啟機器人功能')
            print('a =9867')
            print('ai=5525All')
            print('a(ai(AdminTxt,key))')
            print('ai=run')
            time.sleep(2)



        # 使用 [adminKey,UserKey] auto re
        #print('set 指令')
        #   adminKey1
        ReplyData = [AdminKey,'.,.']#[AdminKey,'.,.']


    
        #   https://wa.me/85255258378?text=我想制作網頁
        #   用字找  https://stackoverflow.com/questions/42046939/whatsapp-web-automation-with-selenium-not-working

        #   任何對話中有 ReplyData字 = 開始自回
        ReplyDataKeyA = '//span[contains(text(),"'+ReplyData[0]+'")]'
        ReplyDataKeyU = '//span[contains(text(),"'+ReplyData[1]+'")]'
        #print('ReplyDataKeyRKL=',ReplyDataKeyA)
        #print('ReplyDataKeyU=',ReplyDataKeyU)

        #   先取A內容 'AdminKey'
        try:
            DialogueList = ATWSteChrome.chrome.find_element_by_xpath(ReplyDataKeyA).text
            if DialogueList:
                UKey = ReplyDataKeyA
                UKey0 = ReplyData[1]#ReplyData[0]
                break   #   去分析 
        except:
            #   取User內容  '.,.'
            try:
                DialogueList = ATWSteChrome.chrome.find_element_by_xpath(ReplyDataKeyU).text
                if DialogueList:
                    UKey = ReplyDataKeyU
                    UKey0 = ReplyData[1]
                    break   #   去分析 
            except:
                # 沒有任何人 sn 任何指令比我
                #time.sleep(2)


                # https://zhuanlan.zhihu.com/p/158300209
                # 递归 溢出 解決 用 continue
                print('   已到帳 *** ',Loop100F5,' 億 *** 港元')
                Loop100F5+=1    # 等客來loop數+1
                continue



































#   分析 指令
def _SeeReplyKeyList(DialogueList,ReplyKey0):
    global ReUsTxt

    ATW._StrToList(DialogueList,ReplyKey0)
    UsTxtList=ATW.TrueList[:]


    # UsTxtList OK
    #  ReplyKey.,.ReplyTxt.,.ReplyKey.,.ReplyTxt.,.
    #tnb=0
    #for t in UsTxtList:
    #    print(tnb,'=',t)
    #    print('------=')
    #    tnb+=1
    #os.system("pause")

    ReUsTxt = []

    # Admin User 分流 tel岩
    #if UserTel == AdminTel:
    #    _AdminSet()
    #else:
    #    _UserSet()
        
    # 製作回覆內容
    try:
        # 指令 錯誤 內容不足
        if not UsTxtList[1]:
            print('\n   *** 指令 錯誤 內容不足 ***\n    ReplyKey.,.ReplyTxt.,.ReplyKey.,.ReplyTxt.,.')
            ReUsTxt = ['***指令 錯誤 內容不足 請從試 ***\n    ReplyKey.,.ReplyTxt.,.ReplyKey.,.ReplyTxt.,.']
    except:
        print('\n   *** 指令 OK ***\n')

    # 記錄 ReUsTxt = ReplyKeyList
    i = 0
    try:
        while i < len(UsTxtList):

            # i = 客戶說:
            ReUsTxt.append(UsTxtList[i]) 

            # ii = AI回覆:
            ii = i+1
            # 轉換行
            UsTxtList00 = str(UsTxtList[ii]).replace("@@","\n")
            # 轉 @+@ @@ ',' .,.
            UsTxtList00 = str(UsTxtList00).replace("@+@","@@").replace("','",".,.")
            ReUsTxt.append(UsTxtList00)

            i+=2
    except:
        pass























# _Admin Setting
def _AdminSet():
    global ReUsTxtB

    print('\n   *** ADMIN *** \n')

    # 轉換所有對話
    ReUsTxtB =[]
    i = 0
    try:
        while i < len(ReUsTxt):

            Us='客戶說: '+str(ReUsTxt[i])+'\n'
            ReUsTxtB.append(Us)

            ii = i+1
            As = 'AI回覆: \n'+str(ReUsTxt[ii])+'\n'
            ReUsTxtB.append(As)

            ReUsTxtB.append('\n----\n')
            i+=2
    except:
        pass
    # 刪廢字 轉句
    ReUsTxtB[-1] = '請仔細確認 指令 \n如沒問題，請用B設備掃QR，受權機器人登入。'

    # 續句寫入確認 指令 
    _InputWsTxt(ReUsTxtB,0,0)


    _AdminSet2()


























# Admin對話中 等新回
def _AdminSet2():
    global RKL_OK

    print('\n   *** _AdminSet2 *** \n')

    #   取我最後說話
    AdminOwen = ATWSteChrome.chrome.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[last()]')

    while True:
        #   取最後說話
        while True:
            try:
                AdminOwen0 = ATWSteChrome.chrome.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[last()]')
                break
            except:
                #print('等admin簽名1')
                time.sleep(2)
                continue
        
        #   最後說話 = 我 = continue
        if AdminOwen0 == AdminOwen:
            print('等admin簽名')
            time.sleep(2)
            continue
        else:
            break

    #   最後說話 = 客
    while True:
        try:
            AdminOwen0B = ATWSteChrome.chrome.find_elements_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[last()]')
            break
        except:
            #   等admin簽名
            #print('adm完in簽名')
            time.sleep(2)
            continue
    
    # admin 簽名
    if AdminKey in AdminOwen0B[-1].text:
        print('OK')
        # ws顯
        ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys('OK\n')
        RKL_OK = True
    else:
        # ws顯
        ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys('成功\n')
        print('簽名成功')

    #   退出對話
    _OutTehTalk()

    #   等客來
    _UserAddMe()


































# send圖比客戶 受權登入 UsTxtList
def _UserSet():


    print('\n   *** _UserSet *** \n')


    # 指令 錯誤
    try:
        if not ReUsTxt[1]:
            print(ReUsTxt)


            # 續句寫入 指令錯誤
            i = 0
            while i < len(ReUsTxt):
                for part in ReUsTxt[i].split('\n'):
                    ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(part)
                    ATWSteChrome.ActionChains(ATWSteChrome.chrome).key_down(ATWSteChrome.Keys.SHIFT).key_down(ATWSteChrome.Keys.ENTER).key_up(ATWSteChrome.Keys.SHIFT).key_up(ATWSteChrome.Keys.ENTER).perform()
                print(ReUsTxt[i])
                i+=1


            #   等客來
            _UserAddMe()



    except:
        print('\n   *** 指令 OK ***\n')




    
    os.system("pause")



    # 圖
    zz1 = 'C:/Users/mokaki/Desktop/job2021/template/abta/ATW/about.jpg'

    while True:
        try:
            # 點附件功能OOOOOOOOOOOOOOOOOO
            ggg = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span'
            ATWSteChrome.chrome.find_element_by_xpath(ggg).click()
            break
        except:
            print('點附件功能')
            time.sleep(2)
            continue

    while True:
        try:
            # 點開sn圖功能
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/span').click()
            break
        except:
            print('點開sn圖功能')
            time.sleep(2)
            continue

    # 關附窗.exe
    # https://www.cnblogs.com/chongyou/p/7065462.html
    # os.startfile("C:\\Users\\mokaki\\Desktop\\job2021\\ATW20210806\\_0atw\\CloseFW.exe")
    os.startfile("_0atw\\CloseFW.exe")
    print('關附窗')
    
    while True:
        try:
            # 要sn的圖
            ATWSteChrome.chrome.find_element_by_tag_name('input').send_keys(zz1)  
            break
        except:
            print('sn圖內的input')
            time.sleep(2)
            continue



    while True:
        try:
            # 填圖片文字
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(ReUsTxt) 
            # 視窗最大
            #ATWSteChrome.chrome.set_window_size(1000,1000)
            ATWSteChrome.chrome.maximize_window()
            # 點sn鍵
            ATWSteChrome.chrome.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[2]/div[2]').click()  
            break
        except:
            print('填圖片文字 視窗最大 點sn鍵')
            time.sleep(2)
            continue








































# 客戶wts我 AI回覆
def _AutoReWsByReplyKeyList(UKey,UKey0):

    #   點0入User對話
    while True:
        try:
            ATWSteChrome.chrome.find_element_by_xpath(UKey).click()
            break
        except:
            #print('點入User對話')
            time.sleep(2)
            continue


    # 一句句寫入AI回覆
    _InputWsTxt(UKey0,1,1)
    print(UKey0)

    #   退出對話
    _OutTehTalk()

    # 回等客
    _UserAddMe()



























































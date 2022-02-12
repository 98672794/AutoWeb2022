




















'''

搵工易 
202111032248
Start()
    _LoginFB()
    _GetJob()
        careerjet
            _GetJobWs
            _TxtToFpPage

#####

ATW 自動搵工程式 202110230036

Start()
    k 创文件夾
    k admin login whatsapp

_MakeReJob()
    取工
    PO FB ig
    傾老闆
    記工

_AutoReJob()
    LOOP
    回客po URL


'''






























from copy import Error
import re
import time
import random
import ATW
import ATWFileList
import ATWReadFile
import ATWGetListKeyTxt
import ATWSteChrome
import ATWFolder
import 自動覆客_IN_點入對話OK








































WhatsappUrl='https://web.whatsapp.com/'

AdminWs = '85255258378'
UserStartTxt = 'ATW202111 Start'

JobCont0='202109251335'






























#######################################################################
##################################################### Start = 開始 分頁0
def Start():
    global NowJobFolder
    global ToDayJobData

    #### 在當前文件夾创工作目錄 if not ####
    NowJobFolder = ATWFolder._MakeJobFolder('_atw')
    ToDayJobData = ATWFolder._MakeJobFolder('_atw\\GetJob')

    #### 登入whatsapp ####
    #                                             selenium chrome 配置
    ATWSteChrome._SteChrome(NowJobFolder,'chrome')
    #                                             admin login whatsapp
    ATWSteChrome.chrome.get(WhatsappUrl)
    #                                                     登入whatsapp
    ATWSteChrome._LoginWhatsapp('chrome','請先登入您的whatsapp','WAR1')
    #                                                               F5
    ATWSteChrome.chrome.refresh()


    #### 回 Admin 登入成功 ####
    #                                                   eval 轉 chrome
    BB1=eval((str('ATWSteChrome.')+str('chrome')))
    #                                     get 入對話  回 Admin 登入成功
    OK='https://web.whatsapp.com/send?phone=' + AdminWs
    BB1.get(OK)
    time.sleep(2)
    #                                                    list 續句寫入
    自動覆客_IN_點入對話OK._InputWsTxt(UserStartTxt,1,0,'chrome') 
    #                                                         退出對話
    自動覆客_IN_點入對話OK._OutTehTalk('chrome')

    if __name__=='__main__':
        #### 分頁1  Login Facebook  ####
        _LoginFB()

        #### 分頁2  自動收集工作程式  ####
        _GetJob()



















































######################################################################################################
########################################################################################## 自動搵工程式  
def _AutoReJob():
    global AdminTxtOK
    print('*** _AutoReJob *** ')

    #### 自動搵老闆程式 ####
    ATAllOK=_MakeReJob()

    AdminTxtOK=[]
    i = 0
    try:
        while i < len(ATAllOK):
            # i = 客戶說:
            AdminTxtOK.append(ATAllOK[i]) 
            # ii = AI回覆:
            ii = i+1
            # 轉換行    \+n
            UsTxtList00 = str(ATAllOK[ii]).replace("@@","\n")
            # 轉 @+@ @@ ',' .,.
            UsTxtList00 = str(UsTxtList00).replace("@+@","@@").replace("','",".,.")
            AdminTxtOK.append(UsTxtList00)
            i+=2
    except:
        pass

    Loop1 = 1   # 等客來loop數
    while True:
        print('333')

        # 回覆Job i=客戶說 ii=AI回覆 #############
        i = 0
        while i < len(AdminTxtOK):

            ii = i+1    # AI回覆
            #   任何新對話中有 客戶說 = 開始自回 不能有' '
            aaa = AdminTxtOK[i].replace(' ','')

            # 找 小草 Key
            aaa = aaa.lower()
            UserSay = '//span[contains(text(),"'+aaa+'")]'
            try:
                DialogueList = ATWSteChrome.chrome.find_element_by_xpath(UserSay).text.lower()

                if DialogueList:
                    if not '.,.' in DialogueList:
                        #print('a1aa=',aaa)
                        UKey = UserSay  # 點位置
                        UKey0 = AdminTxtOK[ii]     # AI回覆
                        #   goto AI回覆
                        #print('    *** goto AI回覆1 *** ')
                        #os.system("pause")
                        自動覆客_IN_點入對話OK._ALL_Reply(UKey,UKey0,'chrome')
            except:
                # 找 大草 Key
                aaa2 = aaa.upper()
                UserSay = '//span[contains(text(),"'+aaa2+'")]'
                #print('aaa=',aaa)
                try:
                    DialogueList = ATWSteChrome.chrome.find_element_by_xpath(UserSay).text.lower()
                    
                    if DialogueList:
                        if not '.,.' in DialogueList:
                            #print('aa2a=',aaa)
                            UKey = UserSay  # 點位置
                            UKey0 = AdminTxtOK[ii]     # AI回覆
                            #   goto AI回覆
                            #print('    *** goto AI222回覆 *** ')
                            #os.system("pause")
                            自動覆客_IN_點入對話OK._ALL_Reply(UKey,UKey0,'chrome')
                except:
                    pass
            i+=2

        # 沒有任何人 sn 任何指令比我
        print('   已到帳 *** ',Loop1,' 億 *** 港元')
        Loop1+=1    # 等客來loop數+1

        # ADMIN SET ### 
        if AdminSetBtn == 1:
            if Loop1>5:
                print('`````````````````````等客Loop ',Loop1,' ADMIN SET````````````````````````````')
                ATWFolder.os.system("pause")

        continue





















































######################################################################################################
###################################################################################### 自動收集工作程式  

'''
# NONON　https://www.google.com/search?q=%E5%8D%B3%E6%97%A5%E5%87%BA%E7%B3%A7&rlz=1C1ONGR_zh-HKHK956HK956&oq=%E5%8D%B3%E6%97%A5%E5%87%BA%E7%B3%A7&ibp=htl;jobs#htivrt=jobs&fpstate=tldetail&htichips=date_posted:week&htischips=date_posted;week&htidocid=p42n3ArvO76cS6IZAAAAAA%3D%3D

# https://www.careerjet.com.hk/search/gongzuo?s=%E5%8D%B3%E6%97%A5%E5%87%BA%E7%B3%A7&l=&radius=10&sort=relevance
# http://www.parttime.hk/%E7%8F%BE%E9%87%91%E5%87%BA%E7%B3%A7-jobs.aspx
# https://hkslash.com/zh/jobs/payment-methods/cash
# https://hkese.net/jobs?query=%E5%8D%B3%E6%97%A5%E5%87%BA%E7%B3%A7
# https://hk.indeed.com/%E6%95%A3%E5%B7%A5-jobs?vjk=67093a36f6033828

# https://mbasic.facebook.com/groups/198752280551178/
# https://mbasic.facebook.com/groups/1467646116897139/
# https://mbasic.facebook.com/groups/1590237851239877/
# https://mbasic.facebook.com/groups/797158416971511/
# https://mbasic.facebook.com/groups/1919154411681857/
# https://mbasic.facebook.com/groups/349905682009054/
# https://mbasic.facebook.com/groups/152343532277096/
# https://mbasic.facebook.com/groups/682095421872616/
# https://mbasic.facebook.com/groups/1787357104866653/
# https://mbasic.facebook.com/groups/hkcasualworker/
# https://mbasic.facebook.com/groups/199581878690345/
# https://mbasic.facebook.com/groups/2237867326301250/
# https://mbasic.facebook.com/groups/354260575016524/
# https://mbasic.facebook.com/groups/637094026468957/
# https://mbasic.facebook.com/groups/2129257833974089/
# https://mbasic.facebook.com/groups/hongkong28506666/
# https://mbasic.facebook.com/groups/396509674530531/
# https://mbasic.facebook.com/groups/1631258640481767/
# https://mbasic.facebook.com/groups/259848104382901/
https://mbasic.facebook.com/groups/643362102478011/
https://mbasic.facebook.com/groups/1277678625908584/
https://mbasic.facebook.com/groups/879708388771941/
https://mbasic.facebook.com/groups/1458262450968835/

# https://www.openrice.com/zh/hongkong/jobs/function/%E6%B8%85%E6%BD%94-%E6%B4%97%E7%A2%97

'''
def _GetJob():#(NowJobFolder):
    print('*** _GetJob *** ')

    #NowJobFolder = ATWFolder._MakeJobFolder('_atw') # QQQQQQQQQ
    #ATWSteChrome._SteChrome(NowJobFolder,'chrome') # QQQQQQQQQ
    #ATWSteChrome.chrome.execute_script('window.open()') # QQQQQQQQQ
    #ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[1]) # QQQQQQQQQ

    # 分頁2 打開 取 careerjet job
    ATWSteChrome.chrome.execute_script('window.open()')
    ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[2])
    ATWSteChrome.chrome.get('https://www.careerjet.com.hk/search/gongzuo?s=%E7%8F%BE%E9%87%91%E5%87%BA%E7%B3%A7&l=%E9%A6%99%E6%B8%AF&radius=10&sort=relevance')

    #### https://www.careerjet.com.hk
    NoTitOut = 0
    i = 1
    while i < 24:
        Job1Html = ['//*[@id="search-content"]/ul[2]/li[',']/article/header/h2/a']
        GJJ = Job1Html[0] + str(i) + Job1Html[1]

        #print('開始找 careerjet [',i,']號工作')
        try:
            # 取 job 名Url 新頁開
            JobName = ATWSteChrome.chrome.find_element_by_xpath(GJJ).text
            JobUrl = ATWSteChrome.chrome.find_element_by_xpath(GJJ).get_attribute("href")

            # 分頁3 打開 取 careerjet job 名Url
            ATWSteChrome.chrome.execute_script('window.open()')
            ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[3])
            ATWSteChrome.chrome.get(JobUrl)


            tex2ts = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="job"]/div/section[1]').text



            # Txt To list
            content_list = ATWReadFile.TxtToList(tex2ts,"\n")
            # Get Job Ws
            JobWs = _GetJobWs(content_list)
            # Get key tit  找關鍵字
            TitKet = 找關鍵字(content_list)

            #print('=All關鍵字Tit,',TitKet)
            #print('=JobWs,',JobWs)
            #ATWFolder.os.system("pause")

            # 页关闭
            ATWSteChrome.chrome.close()




            # 傾老闆 # 傾老闆 # 傾老闆 # 傾老闆 # 傾老闆 # 傾老闆 
            _傾老闆(JobWs,JobName,JobUrl)



            # Send Txt To fpPage
            # 回分頁1
            ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[1])
            _TxtToFpPage(JobWs,JobName,content_list,TitKet)



        except Exception as e:
            _Error(e)
            # 2次 out
            NoTitOut += 1
            if NoTitOut == 4:
                print('找不到 careerjet[',i,']號工作 == 退出')
                break
            print('找不到 careerjet[',i,']號工作')
            ATWFolder.os.system("pause")
            pass

        # 页关闭
        ATWSteChrome.chrome.close()
        # 回分頁2
        ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[2])
        #print('回分頁2')

        i += 1 

    print('careerjet END')

    ATAllOK = 'ATAllOK'

    return ATAllOK























































#     AT143 = "API.,. ',' ws仔 :@@我可以配合whatsapp API 製作您的網上引流工具@@" 
def _MakeReJob():
    print('*** _MakeReJob *** ')

    # 創 GetJob 文件夾 if not
    ffs5 = '_atw\\GetJob'
    ffs5B = ATWFolder._MakeJobFolder(ffs5)

    # 檢查 GetJob 檔案是否存在  全路徑
    ffs5C = ffs5B + '\\chromedriver0.txt'
    JobFile = ATWFileList.IfHaveFile(ffs5C) 
    if JobFile == 0:
        print('*** GetJob 檔案不存在 *** ')
    if JobFile == 1:
        print('*** GetJob 檔案存在 *** ')
    
    _GetJob(NowJobFolder)


















































# K ##################################################################################################
####################################################################################### Login Facebook
def _LoginFB():
    print ('\n!!!!! 登入facebook! ***\n')

    #FB = 'Facebook'
    fb = "https://www.facebook.com/"

    # 取 FB AC PW
    data = NowJobFolder + '\\facebookData.txt'
    FBData =  ATWReadFile.ATWReadFile(data,'NewData','FTL')
    FBAC = FBData[0].replace("\n","")
    FBPW = FBData[1]

    # 分頁1
    ATWSteChrome.chrome.execute_script('window.open()')
    ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[1])

    # 沒入email位回
    while True:      
        # 登入FB頁
        ATWSteChrome.chrome.get(fb)
        try:
            # 入email
            username002 = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="m_login_email"]')
            # 入PS
            password002 = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="m_login_password"]')
            # 點登入
            submit002 = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="login_password_step_element"]/button')
        except: 
            try:
                # 入email 
                username002 = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
                # 入PS
                password002 = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input')
                # 點登入
                submit002 = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
            except: 
                try:    # https://m.facebook.com/
                    # 入email                         
                    username002 = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[4]/div[1]/div/div/input')
                    # 入PS
                    password002 = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div/div/div[1]/div/input')
                    # 點登入
                    submit002 = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/form/div[5]/div[1]/button')
                except: 
                    # 沒
                    print ('解碼錯誤***[找不到入email]***請聯絡開發者更新代碼\n')
                    ATWSteChrome.chrome.close()
                    ATW._OUT()
        break

    # 填 AC PW
    username002.send_keys(FBAC)                        
    password002.send_keys(FBPW)                        
    # 點
    submit002.click()
    time.sleep(random.uniform(3, 11))

    # ADMIN SET ### 
    #if AdminSetBtn == 1:
    #    print ('\n*** ADMIN 編輯用 ***\n')
    #    ATWFolder.os.system("pause")

    # 驗查登入否 
    ATWSteChrome.chrome.get(fb +'me/')
    currentURL = ATWSteChrome.chrome.current_url
    #print (str(currentURL) +'--currentURL\n')
    if currentURL == 'https://www.facebook.com/':
        print ('\n!!!沒有登入 請選其他帳號再試***\n')
        ATWSteChrome.chrome.close()
        ATW._OUT()
    else:
        print ('*** 成功登入facebook ***')

        # 轉言語 搵帖用中文
        while True:
            ATWSteChrome.chrome.get('https://mbasic.facebook.com/settings/language/')
            FBSettingsLanguageTw = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/table[1]/tbody/tr/td/h3/a/span')
            # 如沒中文 轉
            if '中文' not in FBSettingsLanguageTw.text:
                FBSettingsLanguage = ATWSteChrome.chrome.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/table[1]/tbody/tr/td/h3/a/strong')
                FBSettingsLanguage.click()

                # 點 中文台灣
                # QQQQQQQQQQQQQQ 20210727 找不到 from
                print ('\n!!!!!請將語言轉為中文台灣再繼續!!***\n')
                ATWFolder.os.system("pause")
                continue
            else:
                break









































######################################################################################################
###################################################################################### _Txt To Fp Page  
def _TxtToFpPage(JobWs,JobName,content_list,TitKet):
    print('_TxtToFpPage')



    # 香港搵工易 專頁 發布
    ATWSteChrome.chrome.get('https://mbasic.facebook.com/composer/mbasic/?c_src=page_self&referrer=pages_feed&target=1789512794640018')

    # po文all
    TxtAll = ''
    ds = 0
    while ds < len(content_list):
        TxtAll = str(TxtAll + content_list[ds] + '\n' )
        ds+=1


    #J_data = JobName + '\n' + JobWs + '\n' + TxtAll + '\n' + TitKet + '\n' 
    try:
        ATWSteChrome.chrome.find_element_by_name("xc_message").send_keys(JobName + '\n') 

        ATWSteChrome.chrome.find_element_by_name("xc_message").send_keys(JobWs + '\n') 

        ATWSteChrome.chrome.find_element_by_name("xc_message").send_keys(TxtAll + '\n') 

        ATWSteChrome.chrome.find_element_by_name("xc_message").send_keys(TitKet + '\n') 

        ATWSteChrome.chrome.find_element_by_name("view_post").click()

    except Exception as e:
        _Error(e)
        pass





































#  #################################################################################
#################################################################################### 傾老闆 
def _傾老闆(WS,jobname,url):

            # 202111070157 # QQQQQQQQQQQ
            print('=傾老闆')




# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ
# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ# GetJ

#  #################################################################################
#################################################################################### Get key tit 找關鍵字

def 找關鍵字(CareerJetcomHK文):

    地區 = [
        # 地區
        '香港','中西區','東區','南區','灣仔','九龍','觀塘','深水埗','黃大仙',
        '油尖旺','新界','離島','葵青','北區','西貢','沙田','大埔','荃灣','屯門','元朗',
        '赤鱲角','尖沙咀 ','旺角','銅鑼灣','流浮山','堅尼地城','將軍澳','葵涌'
        ]

    行業 = [
        # 行業
        '保安員','貨倉','樓面','倉務','侍應','派傳單',
        '單剪','髮型師','包裝','樓面','廚','司機','跟車','什工'
        ]

    薪金 = [
        # 薪金
        '日薪','$','現金出糧'
        ]


    #   All關鍵字
    All關鍵字Tit = '\n#'
    # 地區
    地區關鍵字 = []
    for C文每行 in CareerJetcomHK文:
        for 地區行 in 地區:
            if 地區行 in C文每行:
                地區關鍵字.append(C文每行)
    All關鍵字Tit = All關鍵字Tit + 地區關鍵字[0] + '\n#'

    # 行業
    行業關鍵字 = []
    for C文每行 in CareerJetcomHK文:
        for 行業行 in 行業:
            if 行業行 in C文每行:
                行業關鍵字.append(C文每行)
    All關鍵字Tit = All關鍵字Tit + 行業關鍵字[0] + '\n#'

    # 薪金
    薪金關鍵字 = []
    for C文每行 in CareerJetcomHK文:
        for 薪金行 in 薪金:
            if 薪金行 in C文每行:
                薪金關鍵字.append(C文每行)
    All關鍵字Tit = All關鍵字Tit + 薪金關鍵字[0] + '\n'




    #print(All關鍵字Tit)
    return All關鍵字Tit




# 202111052211# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ
# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ
# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ# QQQQQQQQQQQ








# 202111022300 #################################################################################
###################################################################################### 取純數字ws
def _GetJobWs(手):
    print('------_GetJobWs-----')

    # ws錨
    GwsN = ['whatsapp','https://wa.me/'] # QQQQQ 2ws同
    #GwsN = 'whatsapp'
    #ffd = 'https://wa.me/'
    #ShopWts=[]

    #   找ws字
    for wst in 手:
        if GwsN[0] in wst.lower() or GwsN[1] in wst.lower():
            #   客公司ws
            #ShopWts.append(wst)  
            ShopWts = wst

    #   轉純數字
    ShopWtsBBB = ''
    for x in ShopWts:
        try:
            int(x)
            ShopWtsBBB = str(ShopWtsBBB + x)
        except:
            pass

    #print(ShopWtsBBB)
    return ShopWtsBBB
































######################################################################################################
###################################################################################### 发生异常
def _Error(e):
    print(e)
    print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数


























































AdminSetBtn=1
#########################
############### 執行本.py
if __name__=='__main__':
    Start()
    #_GetJob()





























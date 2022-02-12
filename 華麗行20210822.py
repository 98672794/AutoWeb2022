














'''

華麗行 202108191503
華麗行.py


華麗行
openrice 請人
ws  我們是
'''













from re import T
import time
import os
import sys
from types import CodeType

from selenium.webdriver.support import wait
import ATW
import ATWFileList
import ATWReadFile
import ATWGetListKeyTxt
#import ATWInWebServer
import ATWSteChrome
import ATWUrlToBitly














KeyFolder = 'AutoWeb'

Bitlyid = 'yobif97000@6ekk.com'
Bitlyps = 'fgj54ignjk' 
# 華麗報價單 2021 08
WLHQT = 'https://docs.google.com/spreadsheets/d/1ncvND-Igdh459ProCtSdeXKuxBKFU6D-Z6E8mrfiXuo/?'























#   Admin Login wts
def AdminLoginWTS():    

    urlName='https://web.whatsapp.com/'
    #selenium chrome 配置
    ATWSteChrome._SteChrome(KeyFolder,'chrome')

    # P1 admin login whatsapp
    ATWSteChrome.chrome.get(urlName)


    # 頁2 打開 openrice 請人
    ATWSteChrome.chrome.execute_script('window.open()')
    ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[1])
    #   關歡迎用    第一次有歡 二冇
    ATWSteChrome.chrome.get('https://www.openrice.com/zh/hongkong/jobs/function/廚師')


    # 頁3 打開 Bitly
    ATWSteChrome.chrome.execute_script('window.open()')
    ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[2])
    ATWSteChrome.chrome.get('https://app.bitly.com/')

    # 回ws
    ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[0])
    # 點個人檔案    c1
    CheckPoint1 = "chrome.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[1]/div/img').click()"
    #   您的名字    c2 c3 
    CheckPoint20 = "chrome"


    #   QQQQQQQQQQQQQQQ 
    #ATWSteChrome.chrome.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/header/div[1]/div/img').click()
    try:
        #   個人
        CheckPoint21 = ATWSteChrome.chrome.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]' )
    except:
        #   商戶
        CheckPoint21 = ATWSteChrome.chrome.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]' )
    #   QQQQQQQQQQQQQQQ 取不到 admin名
    #print('CheckPoint21',CheckPoint21)
    #os.system("pause")
    #   QQQQQQQQQQQQQQQ 


    Talk1 = '請admin 登入whatsapp'
    Talk2 = '歡迎您'

    # 去login.py
    ATWSteChrome._LoopAndCheck(CheckPoint1,CheckPoint20,CheckPoint21,'0','c5',Talk1,Talk2,'t3','t4','t5','WAR1')
    # F5
    ATWSteChrome.chrome.refresh()

    # openrice 請人
    _OpenriceJob()













































































#   openrice 請人
def _OpenriceJob(): 

    # 頁2 打開 openrice 請人
    #ATWSteChrome.chrome.execute_script('window.open()')
    ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[1])

    #   關歡迎用    第一次有歡 二冇
    #ATWSteChrome.chrome.get('https://www.openrice.com/zh/hongkong/jobs/function/廚師')
    #time.sleep(2)

    # 行業
    # https://www.openrice.com/zh/hongkong/jobs/function/行業
    JobList = ['廚師','侍應','餐廳經理-餐廳主任-餐廳部長','店務員','清潔-洗碗','水吧-調酒師','收銀員','客戶服務員','食品製作','咖啡師','傳菜員','技術員-工程師','前堂客務-禮賓部','客務','預約-訂房部','房務員-管家部','其他餐飲服務部','物流-交通-運輸','市場營銷-公共關係','銷售','財務-會計','資訊科技','管理-酒店管理','採購','一般-其他']
    # ws錨
    GwsN = 'whatsapp'
    ShopWts=[]


    # 到每行業 url
    for JobClass in JobList:
        ThisJobClass = 'https://www.openrice.com/zh/hongkong/jobs/function/'+JobClass
        ATWSteChrome.chrome.get(ThisJobClass)

        #   每頁 一頁=15
        startAtCont = 15
        while True:

            #   每個工作    左列表 2~16
            i = 3
            while i < 17:                

                # all內容
                HeWs = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="layout"]/main/div/div[3]/div[3]/div[1]/article/div[2]').text
                #  轉list
                ATW._StrToList(HeWs,'\n')
                Txt_List=ATW.TrueList[:]

                #   客公司名
                ShopName = Txt_List[1]

                ShopWts.clear()
                #   找ws字
                for wst in Txt_List:
                    if GwsN in wst.lower():
                        #   客公司ws
                        ShopWts.append(wst)                       

                # 有ws去sn
                if ShopWts:
                    #print('ShopName=',ShopName)
                    # 修正取得的ws內容 ###########################################
                    _ChangeTxt(ShopName,ShopWts)
                    ############################################################
                else:
                    print('whatsapp=沒有')

                #   下個工作
                print('第',str(i),'個工作')
                try:
                    NextJob = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="layout"]/main/div/div[3]/div[2]/div['+str(i)+']/div/div[1]/div[1]/a')
                    NextJob.click()
                except:
                    pass

                time.sleep(2)
                i+=1
                #   回每個工作

            #   下15個 找3頁夠暫時
            while startAtCont < 60:
                ThisJobClassNextPage = ThisJobClass+'?startAt='+str(startAtCont)
                ATWSteChrome.chrome.get(ThisJobClassNextPage)
                startAtCont+=15

                try:    # 查本page有沒內容
                    SeeIfHave = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="layout"]/main/div/div[3]/div[3]/div[1]/article/div[2]')
                    if SeeIfHave:
                        break
                except:
                    startAtCont==60
                    break

            #   回每頁
            if startAtCont < 60:
                continue
            else:
                break

        #   下類工作           
        print('已取完所有',JobClass,'類工作')
        #os.system("pause")

    print('已取所有行業 完')
    os.system("pause")























































#   修正取得的ws內容
def _ChangeTxt(SN,SW):    

    nbs = ''    #   客公司ws 純數字
    Nb = ['1','2','3','4','5','6','7','8','9','0',',']
    Nb2 = ['1','2','3','4','5','6','7','8','9','0']

    OKsn = False
    print('修正取得的ws內容')
    try: 
        # 多個ws
        if SW[1]:
            print('多1SW',SW)
    except:
        # 單個ws
        print('單1SW',SW)

    # 合併 all SN
    for wts00 in SW:
        SW1 = SW1+','+wts00+','
        SW= str(SW1).replace('/',',').replace('w',',').replace('W',',')

    #Q  沒用QQQQQQQQQQQQQQQQ
    #for wts0 in SW:
    #    for Nbm2 in Nb2:
    #        if wts0 !=Nbm2:
    #            wts0 = ','
    print('SW0=',SW)

    # 每字轉 取純數字
    for wts in SW:
        for Nbm in Nb:
            if wts in Nbm:
                nbs = str(nbs+wts)

    #   如取得的是數字
    print('nbs1=',nbs)
    for Nbm in Nb2:
        if Nbm in nbs:
            OKsn = True

    TelNb = ['4','5','6','7','8','9']
    if OKsn == True:
        #  所有有ws的句 轉後 用8位
        if ',' in nbs:
            ATW._StrToList(nbs,',')
            for txt in ATW.TrueList:
                if len(txt) == 8:
                    for txt2 in TelNb:
                        if txt[0] == txt2:
                            TrueWs = txt
        else:
            TrueWs = nbs

        # Whatsapp Sane 
        _WLHSendWts(SN,TrueWs)

    #QQQQQQQQQQ
    #豚豚
    #嚐‧高美集團有限公司





















































































snT1 = 'https://web.whatsapp.com/send?phone=852'
snT2 = '您好\n我們是 華麗行\n專營咖啡、紅茶，糧油醬料及冷凍食品\n現付上本月報價單\n'
snT3 = '\n如需試貨訂貨\n敬請聯絡洽詢 莫生\n謝謝'

#   Whatsapp Sane WLH QT
def _WLHSendWts(TrueShopName,TrueShopwhatsapp):    

    #   回ws
    ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[0])

    time.sleep(2)

    #   入號找舊對話
    ATWSteChrome.chrome.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').send_keys(ATWSteChrome.Keys.CONTROL, 'a')
    ATWSteChrome.chrome.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]').send_keys(TrueShopwhatsapp)
    time.sleep(2)

    #   找舊對話
    try:
        OutTalk = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]').text
    except:
        #print('未sn')

        # 頁3 打開 Bitly
        WLHQT0 = WLHQT+TrueShopwhatsapp
        ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[2])
        BitlyTag = '華麗To'+TrueShopName+time.strftime('%Y年%m月%d日')
        ATWUrlToBitly._UrlToBitly(Bitlyid,Bitlyps,BitlyTag,WLHQT0)

        # 回頁1 sn ws
        ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[0])
        snThis = snT1+TrueShopwhatsapp

        print('ShopName=',TrueShopName)
        print('Shopws=',TrueShopwhatsapp)
        print('您的短網址 =',ATWUrlToBitly.uuu)
        print('snThis',snThis)
        ATWSteChrome.chrome.get(snThis)
        time.sleep(2)

        # 續句寫入確認 ReplyKeyList 
        while True:
            try:
                gggg = ATWSteChrome.chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
                break
            except:
                time.sleep(1)
                continue

        snTxt = snT2+ATWUrlToBitly.uuu+snT3
        for part in snTxt.split('\n'):
            gggg.send_keys(part)
            ATWSteChrome.ActionChains(ATWSteChrome.chrome).key_down(ATWSteChrome.Keys.SHIFT).key_down(ATWSteChrome.Keys.ENTER).key_up(ATWSteChrome.Keys.SHIFT).key_up(ATWSteChrome.Keys.ENTER).perform()

        os.system("pause")  #   QQQQQQQQQQ

        # 點sn鍵
        gggg.send_keys('\n')
        time.sleep(2)

        # 回頁2
        ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[1])

    #   有找舊對話
    else:
        print('sn過 next')
        # 回頁2
        ATWSteChrome.chrome.switch_to.window(ATWSteChrome.chrome.window_handles[1])
        # 回 _OpenriceJob
        #print('回下個工作')





































































AdminLoginWTS()










































































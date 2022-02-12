
'''
py3

自動臨時網址
ATW202107042228
mokaki
    


pip install selenium


'''











#################################################################################import
import os
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time
import datetime
import re
import random




















##############################################################################Data
GithubIo = '.github.io'




















YourAc = 0
####################################################################################填寫資料
def InputYourData(): 
    global YourAc

    print('\n自動临时網址 歡迎您`````````````\n')
    print('\n```````````````````````````修改临时網址資料\n')
    print('如果您已有github帳號，您可以使用\n (YouAc)',GithubIo,'\n作您的临时網址\n\n')
    print('在這裡您可以上傳靜態網頁(HTML)，作您的临时網頁')
    print('\n```````````````````````````\n')
    
    YourAc = input('請填寫您的 GITHUB 帳號\n如沒有，將退出程式。\n如您的.json數據保存在 .py 的同位置，將自動登入 GITHUB \n')
    if YourAc == '':
        print('沒有 GITHUB 帳號，將退出程式!!\n')
        _OUT()

    else:
        YourAcJson = YourAc + '.json'
        if os.path.isfile(YourAcJson):             #YourAc檔在
            print(YourAc,'您好\n正在登入',YourAc,GithubIo,'\n')
            _LoingGithub()

        else:                             #YourAc檔不在   SAVE
            Yourpw = input('請填寫您的 密碼')
            informations = {
                'GITHUBAc': YourAc,
                'GITHUBPwd': Yourpw,
            }
            path = YourAc + '.json'
            json_str = json.dumps(informations, ensure_ascii=False, indent=4)     #缩进4字符
            with open(path, 'a', encoding="utf-8") as json_file:
                json_file.write(json_str)
            print ('已保存您的 GITHUB 資料\n' + str(informations).replace(',', ',\n') + '\n')
            _LoingGithub()




















tt = 0                                                                  # 查 临时網址 有冇
############################################################################_LoingGithub
def _LoingGithub(): 
    global chrome
    global tt
    print('\n```````````````````````````_Loing Github\n')

    #取DATA文件
    YourAcJson = YourAc + '.json'
    with open(YourAcJson, 'r', encoding="utf-8") as j:
        d = json.load(j)
        Ac = d['GITHUBAc']
        Pw = d['GITHUBPwd']
        #print ("\GITHUBAc: ",Ac),print ("\GITHUBPwd: ",Pw)

    #selenium chrome 配置
    options = Options()
    #options.add_argument('--headless')  # 配置无界面
    options.add_argument("--incognito")  # 配置隐私模式 https://blog.csdn.net/weixin_35757704/article/details/112975153
    options.add_argument("--disable-notifications")

    #防github
    #https://stackoverflow.com/questions/49565042/way-to-change-google-chrome-user-agent-in-selenium/49565254#49565254
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    chrome = webdriver.Chrome('../exe/chromedriver', chrome_options=options)

    #random window_siz
    W = [280,540,1024,768,375,414,375,320,411,411,360]
    H = [653,720,1366,1024,812,736,667,568,823,731,640]
    N = int(random.uniform(0, 10))
    chrome.set_window_size(W[N], H[N])

    #到github login
    chrome.get("https://github.com/login")

    #AC PW click
    chrome.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]').send_keys(Ac)
    time.sleep(random.uniform(2, 5)) 
    chrome.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[1]').send_keys(Pw)
    time.sleep(random.uniform(2, 5)) 
    chrome.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/div/input[12]').click()

    #檢查登入
    while True:
        NowUrl = chrome.current_url
        if NowUrl == 'https://github.com/':
            break
        else:
            continue

    #Your account has been flagged.
    while True:      
        try:  
            bb = chrome.find_element_by_xpath('/html/body/div[1]/div')
        except:    #冇
            #print('帳號正常可用\n')
            break
        else:      #有
            print('您的帳號被 github 限制了，其他人不可查看您的 临时網址!!!\n建議換帳號再試\n')
            print((bb).text)
            print ("---------------------------")
            break

    #查 临时網址 有冇
    U = str("https://github.com/"+YourAc+"/"+YourAc+".github.io")
    chrome.get(U)
    while True:      
        try:  
            tt = chrome.find_element_by_xpath('/html/body/div[4]/div/main/div[1]/div[1]/div/h1/strong')
        except:    #冇
            #print('c临时網址 未開設\n')
            tt = 0
            break
        else:      #有
            #print((tt).text)
            tt = 1
            break
    _SetGithubDomain()




















############################################################################SET Github 網址
def _SetGithubDomain(): 
    print('\n```````````````````````````SET Github 網址\n')

    if tt == 0:     #開設 临时網址
        N = str(YourAc+".github.io")
        M = str("Temp URL is "+YourAc+".github.io")
        print('開設 临时網址\n')
        chrome.get('https://github.com/new')
        chrome.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input').send_keys(N)
        chrome.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/dl/dd/input').send_keys(M)
        chrome.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]').click()
        #https://stackoverflow.com/questions/8832858/using-python-bindings-selenium-webdriver-click-is-not-working-sometimes
        chrome.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').submit()
        print('已開設 临时網址\n您可將修改好的HTML文件拉到此!!')

    if tt == 1:     #修改 临时網址
        O = str('https://github.com/'+YourAc+'/'+YourAc+'.github.io/archive/refs/heads/main.zip')
        chrome.get(O)
        print('修改 临时網址\n備份已下載!!\n')
        print('您可將修改好的HTML文件拉到此!!\n')

    _OUT()






























































#########################################################################按鍵退出程式
def _OUT():
    print ("---------------------------")
    '''
    SelBtn = input('任何字符    =    製作網頁\n            =    退出程式\n')
    if SelBtn != " ":
        os.system("python ./自動製作網頁.py")
        return
    '''
    print('按鍵退出程式')
    os.system("pause")





















InputYourData()


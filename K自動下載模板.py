
'''
py3

自動下載模板
ATW202107041324
mokaki

pip install requests
pip install rarfile
pip install Pillow
pip install fonttools
pip install threaded
pip install PyClassicRound



.woff2','.eot']     未有    舊BRO有字不看到
'''
# -*- coding: UTF-8 -*-














##########################################################################import
import os
import requests
import urllib
import sys
from urllib.request import urlretrieve
import time
from PyClassicRound import classic_round
import rarfile
import io
from PIL import Image
from threading import *
from fontTools.ttLib import TTFont


















##############################################################################Data
template = '../template/'                                             #模板存檔位置
selTimeBTN = 0                       #各FUN用計時退出選擇 0 = 下載完 1 = 自己加入FUN


















htmlname = '18353'                                                    #模板的尾數
htmlname1 = htmlname + ".rar"                                          #模板rer名
url = 0                                                                  #選下URL
#########################################################################選下載檔
def _SeeHTML():    
    global htmlname
    global htmlname1
    global url
    print('\n自動下載模板 歡迎您`````````````\n')
    print('```````````````````````````請選下載檔\n')
    if selBTN == 0:
        os.system('start chrome {}'.format('http://www.mobanwang.com/'))
    htmlname = input('請填寫模板的尾數,如'+ htmlname +'\n')
    if htmlname == '':
        print('沒有模板尾數,將自動下載模 18350 \n')
        htmlname = '18350'
    htmlname1 = htmlname+".rar"
    url = 'http://www.mobanwang.com/mb/showsoftdown.asp?urlid=1&softid=' + htmlname
    _MakdFolder()


















selBTN = 0                        #0=新使用,打開網頁 1=已開始不打開網頁 _SeeHTML()
#########################################################################创文件夾
def _MakdFolder():    
    global selBTN
    global selTimeBTN
    print('\n``````````````````````````````````下載模板\n')

    #如檔在
    if os.path.isfile(template + htmlname + '/' + htmlname1):
        print ("模板已存在,請選其他模板...")
        selBTN = 1
        _SeeHTML()

    #创文件夾
    file = template + htmlname #+ "\\html"
    mkdir(file)

    #同時計時及下載
    #https://t.codebug.vip/questions-2459684.htm
    selTimeBTN = 0
    t = Timer(0.0, _DwlHTML)                                           #下載模板
    t2 = Timer(0.0, hahaTimer)                                             #計時
    t.start()
    t2.start()


















############################################################################下載模板
def _DwlHTML():    
    tt=time.time()
    
    #下載寫入
    r = requests.get(url)

    with open(template + htmlname + '/' + htmlname1, "wb") as code:
        code.write(r.content)

    urllib.request.urlretrieve(url, template + htmlname + '/' + htmlname1, progress)
    print()

    tt2=time.time()

    print('完成下載!!\n總時間',round(tt2-tt,3),'秒',round(((tt2-tt)/60),1),'分鐘\n')
    print('``````````````````````````````````\n')

    _MakdFolder2()


















##############################################################################创ALL文件夾
def _MakdFolder2():    
    b = []
    i = 0
    #創文件                                           \\html\\assets\\images\\banner2.jpg
    #打開RAR文件複製                                            html/assets/images/g5.jpg

    rf = rarfile.RarFile(template + htmlname + '/' + htmlname1) 

    for f in rf.infolist():
        if f.file_size == 0:    #查文件 size == 0 https://rarfile.readthedocs.io/api.html

            b.append(str(f.filename).replace('/', '\\'))           #html\\assets\\fonts\\

            while i < len(b):
                #創文件
                file = template + htmlname + "\\" + b[i][:-1]    #18338\html\assets\fonts
                #print(file)
                mkdir(file)
                i+=1
    _UnRAR()


















a = []                                                      # !=0 all f.filename
#########################################################################解壓文件
def _UnRAR():    
    global a
    #global selTimeBTN

    #原始檔案名
    rf = rarfile.RarFile(template + htmlname + '/' + htmlname1)
    for f in rf.infolist():
        if f.file_size != 0:
            a.append(f.filename)        # !=0 all f.filename
            #print(f.filename)

    #解壓文類
    _txtOpen()


















keyword1 = ['.html','.css','.js','.svg','.php']                                    #文類檔
#########################################################################文類檔保存
def _txtOpen():
    print('------------開始保存文字檔!!\n')
    #轉文類檔檔案名 \ /
    txtOpenFile = []                         #文類檔 打開RAR文件複製 html/index.html
    i = 0
    for i in range(len(keyword1)):
        for j in range(len(a)):
            if a[j].find(keyword1[i]) == -1:
                continue
            txtOpenFile.append(a[j])

    #文類檔保存
    bb = "/"                                                     # /html/index.html
    i = 0
    while i < len(txtOpenFile):
        Data3 = template + htmlname + bb + txtOpenFile[i]   # 18338/html/index.html
        fp = open( Data3 , "w", encoding="utf-8" )    
        rf = rarfile.RarFile(template + htmlname + '/' + htmlname1)
        for f in rf.infolist():
            if f.filename == txtOpenFile[i]:
                ewqqew1 = rf.read(f)
                ewqqew1 = ewqqew1.decode("utf-8")
                fp.writelines(ewqqew1)
        fp.close()
        print(Data3,'文字檔已保存!!\n')
        i+=1
    print('所有文字檔已保存!!\n')
    print('------------------------------\n')
    _ttfOpen()


















keyword2 = ['.ttf','.woff','.otf']  #.woff2,.eot'] 未有                                    #字體檔
########################################################################################字體檔保存
def _ttfOpen():
    #轉字體檔檔案名 \ /
    ttfOpenFile = []                                            #字體檔 打開RAR文件複製 html/字體檔
    i = 0
    for i in range(len(keyword2)):
        for j in range(len(a)):
            if a[j].find(keyword2[i]) == -1:
                continue
            ttfOpenFile.append(a[j])
    
    ttfOpenFileAddUrl = []                              #字體檔 創文件 html\\assets\\images\\字體檔
    i = 0
    while i < len(ttfOpenFile):
        ttfOpenFileAddUrl.append(str(ttfOpenFile[i]).replace('/', '\\\\'))
        i+=1

    #字體檔保存
    aa = "\\\\"                                                   # \\html\\assets\\images\\字體檔
    i = 0
    while i < len(ttfOpenFile):
        #http://python-learnnotebook.blogspot.com/2019/12/python-indexerror-list-index-out-of.html
        Data3 = template + htmlname + aa + ttfOpenFileAddUrl[i]
        rf = rarfile.RarFile(template + htmlname + '/' + htmlname1)
        for f in rf.infolist():
            if f.filename == ttfOpenFile[i]:
                #https://stackoverflow.com/questions/51177475/python3-how-to-install-ttf-font-file
                try: 
                    font = TTFont(io.BytesIO(rf.read(f))) 
                    font.save(Data3)
                    print(Data3,'字體已保存!!\n')
                except:
                    if i == len(ttfOpenFile):
                        break
                    else:
                        continue
        i+=1

    print('所有字體已保存!!\n')
    print('------------------------------\n')
    _ImageOpen()


















keyword0 = ['.jpg','.jpeg','.png','.gif','.ico']                                                     #圖類檔
###################################################################################################圖類檔保存
def _ImageOpen():
    global TimeOutBTN
    #轉圖類檔檔案名 \ /
    ImageOpenFile = []                                      #圖類檔 打開RAR文件複製 html/assets/images/g5.jpg
    i = 0
    for i in range(len(keyword0)):
        for j in range(len(a)):
            if a[j].find(keyword0[i]) == -1:
                continue
            ImageOpenFile.append(a[j])                        
    ImageOpenFileAddUrl = []                                 #圖類檔 創文件 html\\assets\\images\\banner2.jpg
    i = 0
    while i < len(ImageOpenFile):
        ImageOpenFileAddUrl.append(str(ImageOpenFile[i]).replace('/', '\\\\'))
        i+=1

    #圖類檔保存
    aa = "\\\\"                                                        # \\html\\assets\\images\\banner2.jpg
    i = 0
    while i < len(ImageOpenFile):
        Data3 = template + htmlname + aa + ImageOpenFileAddUrl[i] # 18338\\html\\assets\\images\\banner2.jpg
        rf = rarfile.RarFile(template + htmlname + '/' + htmlname1)
        for f in rf.infolist():
            if f.filename == ImageOpenFile[i]:
                img = Image.open(io.BytesIO(rf.read(f))) 
                img.save(Data3)
        print(Data3,'圖片已保存!!\n')
        i+=1

    print('所有圖片已保存!!\n')
    print('------------------------------\n')
    _ChangeCopyright()
















CN = "mokaki"                                                                                    #預設版权所有者
CU  = "https://github.com/mokaki/AutoWeb"                                                          #預設版权網址
######################################################################################################轉版權網址
def _ChangeCopyright():                                                                              #轉版權網址
    global CN                                                                                        #版权所有者
    global CU                                                                                          #版权網址
    n1 = 'W3Layouts'
    u1 = 'https://w3layouts.com/'
    n2 = 'Colorlib'
    u2 = 'https://colorlib.com'

    print('------------開始版權資料!!\n')

    CN = input('請填寫版权所有者，如沒有將使用 mokaki。\n')                                         #輸入版权所有者
    if CN == '':                                                                                       #如沒輸入
        CN = 'mokaki'                                                                            #=預設版权所有者

    CU = input('請填寫版权網址，如沒有將使用 https://github.com/mokaki/AutoWeb。\n** https:// **\n')  #輸入版权網址
    if CU == '':                                                                                       #如沒輸入
        CU = 'https://github.com/mokaki/AutoWeb'                                                   #=預設版权網址

    print('\n版权所有者:',CN,'\n版权網址:',CU,'\n')

    #找出所有 .HTML文件名                                                 #https://zhuanlan.zhihu.com/p/142652629
    itemList = []                                                                     #itemList = 所有 .HTML文件
    path = template + htmlname + "/html"                                              # path = 要找尋的文件夾路径
    filelist=os.listdir(path)                                               # 返回path下所有文件构成的一个list列表
    for item in filelist:                                                         # 遍历输出每一个文件的名字和类型
        if(item.endswith('.html')):                                               # item = 输出指定后缀类型的文件
            itemList.append(item)                                                            #itemList 加入 item
            #print(item)                                                                                # 文件名
    #print(itemList)

    #抄寫新文件
    j = 0                                                                                        #itemList計算器
    while j < len(itemList):                                                #當 itemList計算器 少於 itemList 總長
        Data = template + htmlname + "\\html\\" + itemList[j]                     # Data = 原 單個 .HTML 文件路径
        fp = open( Data , "r", encoding="utf-8" )                                        # 打開 原 文件 R = 只讀
        count=len(open(Data,'r',encoding='UTF-8').readlines())                       # count= 單個 文件 內容 總長

        Data2 = template + htmlname + "\\html\\" + CN + "_" + itemList[j]       # Data2 = 新 單個 .HTML 文件路径
        f2p = open( Data2 , "w", encoding="utf-8" )                                   # 打開 新 文件 w = 创新删舊
        
        #寫入 新文件 內容
        i = 0                                                                                    #文件 行 計算器
        while i < count:                                                        #當 計算器 少於 單個 文件 行 總長
            line = fp.readline()                                                           # line =  原文件 一行
            f2p.writelines(line.replace(u1, CU).replace(n1, CN).replace(u2, CU).replace(n2, CN))    # 寫入並替換
            #print(line)
            i+=1                                                                      #文件 行 計算器 +1 = 下一行
        j+=1                                                                       #itemList計算器 +1 = 下個文件
        f2p.close()                                                                               # 關閉 新 文件

    print('\n',htmlname,'已修改\n版权所有者:',CN,'\n版权網址:',CU,'\n')
    print('------------------------------\n')
    _OUT()




















































#########################################################################計時10分
def hahaTimer():
    while(True):
        for i in range(630):
            print(round(((i)/60),1),'分鐘...',"\r已使用%s秒  " % (1+i), end="")
            time.sleep(1)
            if selTimeBTN == 0:
                if os.path.isfile(template + htmlname + '/' + htmlname1):
                    exit()


















###########################################################################進度條
def progress(block_num, block_size, total_size):
    #進度條 https://home.gamer.com.tw/creationDetail.php?sn=4800729
    sys.stdout.write('\r下載模板 %s %.1f%%' % (htmlname1, float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()


















#########################################################################创文件夾
def mkdir(path):
#https://blog.csdn.net/vip_lvkang/article/details/76906718
    folder = os.path.exists(path)
    if not folder:                      #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)         #makedirs 创建文件时如果路径不存在会创建这个路径
        print ("\n---  成功创建文件夾...  ---")
    else:
        print ("---  文件已存在,將加入新內容...!  ---")


















#########################################################################按鍵退出程式
def _OUT():
    print ("---------------------------")
    print('按鍵退出程式')
    os.system("pause")

    '''
    SelBtn = input('0    =    製作網頁\n1    =    自動臨時網址\n     =    退出程式\n')
    if SelBtn == '':
        print('按鍵退出程式')
        os.system("pause")
    if SelBtn == 0:
        os.system("python ./自動製作網頁.py")
        return
    if SelBtn == 1:
        os.system("python ./自動臨時網址.py")
        return
    '''








_SeeHTML()
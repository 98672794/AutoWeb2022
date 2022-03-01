#!/usr/bin/env python




'''
winpy3

翻譯句子GoogleTranslator
ATWLanguage
ATW202202051827
mokaki
https://98672794.github.io/
inputENisGood
'''
# -*- coding: UTF-8 -*-
from deep_translator import (GoogleTranslator,PonsTranslator,LingueeTranslator,MyMemoryTranslator,YandexTranslator,DeepL,QCRI,single_detection,batch_detection)
import ATWREADME



###################################################################################
############################################################# README 說明
def README(): 

    ThisREADME = [
        '*** ATWLanguage.README ***', # PYfileName
        'printList =\n        翻譯句子GoogleTranslator',
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202042',
        'https://98672794.github.io/'

    ]

    ATWREADME._READYourME(ThisREADME)

























########################################################################## 翻譯功能
def _AutoWebChangeLanguage(BassLan01): 

    #BassLan = 'zh-Hant'

    Talk0 = '您好 請直接填寫您語言之中的任何一個單詞，如: 语言,您好,Hello,こんにちは,สวัสดี...\n',
    Talk1 = '不能用數字',
    Talk2 = '不能空值',
    Talk3 = '語言已經轉換為',
    Talk4 = '保存',
    Talk5 = '重新修改語言'

    Talk0000 = '''
    您好 請直接填寫您語言之中的任何一個單詞，如: 语言、您好、Hello、こんにちは、สวัสดี...\n///
    不能用數字///
    不能空值///
    語言已經轉換為///
    保存///
    重新修改語言
    '''

    while True: # 驗try 2 轉 Language

        while True: # 1 驗答

            Talk0All2 = _AutoWeb翻譯功能(Talk0000,BassLan01)
            Talk0All3 = Talk0All2.split('///')          #   str扮list指定 \n 分隔符號

            填寫您語言取目標語言 = input(Talk0All3[0])

            # 不能數字
            NoNb0 = []
            NoNb = [1,2,3,4,5,6,7,8,9,0]
            NoNb1 = []
            i = 0
            while i < len(填寫您語言取目標語言):
                NoNb0.append(填寫您語言取目標語言[i])
                i+=1
            NoNb1.clear()
            for nb in NoNb:
                for word in NoNb0:
                    word,nb = str(word),str(nb)
                    if word in nb:
                        NoNb1.append(word)
            if NoNb1:
                print ('XXX ',Talk0All3[1],' XXX\n')
                continue    # 回驗答

            # 不能空值
            if 填寫您語言取目標語言 == '':
                print ('XXX ',Talk0All3[2],' XXX\n')
                continue    # 回驗答
            break   # 出驗答

        # 2 試轉 Language
        try:
            # https://deep-translator.readthedocs.io/en/latest/usage.html#language-detection
            目標語言 = single_detection(填寫您語言取目標語言, api_key='1521de38ddf080ba292f64dfe40a0438')



            Changed = _AutoWeb翻譯功能(Talk0000,目標語言)
            Changed2 = Changed.split('///')          #   str扮list指定 \n 分隔符號



            print (Changed2[3],目標語言)
            print ('\n   0 === ',Changed2[4],'\n   1 === ',Changed2[5])
            
            InputYourLanguageGoto = input()

            if InputYourLanguageGoto != '0':
                BassLan01 = 目標語言 # 轉預言
                continue    # 回驗try
            else:
                break   # 出驗try
        except:
            # 不支持
            print ('XXX This Language [',目標語言,'] cannot be used XXX\n change Language to [zh-Hant] ')
            目標語言 = BassLan01
            #TalkToYou = _AutoWeb翻譯功能(Talk,目標語言) # 轉預言
            continue    # 回驗try

    ReData = 目標語言

    return ReData   # txt























































########################################################################## 翻譯功能
def _AutoWeb翻譯功能(原文,您言): 

    #print ('=翻譯句子= \n[',原文入,']\n--------------------------\n')
    
    #NewLanguageText = []    # 已翻譯句子all
    #NewLanguageText.clear()

    # 翻譯句子
    if 您言 != 'zh-Hant':
        Txted = GoogleTranslator(source='auto', target=您言).translate(原文)
        #print ('已翻譯句子= ',Txted,' XXX\n')
        ReData = Txted
    else:
        # 繁中不需
        ReData = 原文


    return ReData   # list





'''


    #if 您言 != 'zh-Hant':

    for txt in 原文:    # 每句翻入
        Txted = GoogleTranslator(source='auto', target=您言).translate(txt)
        NewLanguageText.append(Txted)
        print ('已翻譯句子= ',Txted,' XXX\n')
    ReData = NewLanguageText

    #else:
        # 繁中不需
    #    ReData = 原文




'''
































if __name__ == "__main__":
    README()
    
    



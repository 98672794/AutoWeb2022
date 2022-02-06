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
def _AutoWebChangeLanguage(): 

    Talk = [
        '您好 請直接填寫您語言之中的任何一個單詞，如: 语言,您好,Hello,こんにちは,สวัสดี...\n',
        '不能用數字',
        '不能空值',

        # 2 轉 Language
        '語言已經轉換為',
        '保存',
        '重新修改語言'
    ]
    # 預言
    TalkToYou = _AutoWeb翻譯功能(Talk,'en')

    while True: # 驗try 2 轉 Language

        while True: # 1 驗答
            填寫您語言取目標語言 = input(TalkToYou[0])

            # https://chercher.tech/python-questions/check-number-integer-python-questions
            if type(isinstance) == int:
                # https://blog.51cto.com/alsww/1787848
                print ('XXX ',TalkToYou[1],' XXX\n')
                print ('XXX isinstance XXX\n') 
                continue    # 回驗答

            if 填寫您語言取目標語言 == '':
                print ('XXX ',TalkToYou[2],' XXX\n')
                continue    # 回驗答
            break   # 出驗答

        print ('XXX 3123123123121 XXX\n')    
        # 2 轉 Language
        try:
            # https://deep-translator.readthedocs.io/en/latest/usage.html#language-detection
            目標語言 = single_detection(填寫您語言取目標語言, api_key='1521de38ddf080ba292f64dfe40a0438')

            YourLanguage1 = '',TalkToYou[3],'   '+目標語言+'\n   0 === ',TalkToYou[4],'\n   1 === ',TalkToYou[5],'\n\n'
                            # '語言已經轉換為',                           '保存',                     '重新修改語言'
            # 選動

            ggsdgsdg = _AutoWeb翻譯功能(YourLanguage1,目標語言) #qqqq

            InputYourLanguageGoto = input(ggsdgsdg)
            if InputYourLanguageGoto != '0':
                TalkToYou = _AutoWeb翻譯功能(Talk,目標語言) # 轉預言
                continue    # 回驗try
            else:
                break   # 出驗try
        except:
            # 不支持
            print ('XXX This Language [',填寫您語言取目標語言,'] cannot be used XXX\n change Language to [EN] ')
            目標語言 = 'en'
            TalkToYou = _AutoWeb翻譯功能(Talk,目標語言) # 轉預言
            continue    # 回驗try

    ReData = 目標語言

    return ReData   # txt























































########################################################################## 翻譯功能
def _AutoWeb翻譯功能(原文,您言): 

    #print ('=翻譯句子= \n[',原文入,']\n--------------------------\n')
    
    NewLanguageText = []    # 已翻譯句子all
    NewLanguageText.clear()

    if 您言 != 'zh-Hant':
        for txt in 原文:    # 每句翻入
            Txted = GoogleTranslator(source='auto', target=您言).translate(txt)
            NewLanguageText.append(Txted)
            print ('已翻譯句子= ',Txted,' XXX\n')
        ReData = NewLanguageText
    else:
        # 繁中不需
        ReData = 原文

    return ReData   # list






































if __name__ == "__main__":
    README()
    
    



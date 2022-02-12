




'''
winpy3

List get txt 
ATWTxtAndList
ATW202202060109
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-

import ATWREADME





###################################################################################
############################################################# ATWFolder說明
def README(): 

    ThisREADME = [
        '*** ATWTxtAndList.README ***', # PYfileName
        'AutoWeb 文字轉list =\n         _StrToList(txt,cut)',
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202051218',
        'https://98672794.github.io/'
    ]

    ATWREADME._READYourME(ThisREADME)












###################################################################################
################################################################ AutoWeb 文字轉list

def _StrToList(txt,cut):                 #   (文字,分割符號)
    TrueList = []
    TrueList.clear()                     #                  清空列表

    txt,cut = str(txt),str(cut)
    StrNotList = txt.split(cut)          #   str扮list指定 \n 分隔符號

    for t in StrNotList:
        TrueList.append(t)   #   將 data[a] 加入 TrueList

    return TrueList













if __name__ == "__main__":
    README()
    
    



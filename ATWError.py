




'''
winpy3

发生异常動作
ATWError
ATW202202042022
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-

import ATWREADME
import ATWLanguage
from copy import Error




###################################################################################
############################################################# ATWFolder說明
def README(): 

    ThisREADME = [
        '*** ATWError.README ***', # PYfileName
        '发生异常所在的文件行数 =\n         _Error(e)',
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202051218',
        'https://98672794.github.io/',
        ' ********* 用 *********** ',

    '   except Exception as e:                 \n',
    '       for 异常 in ATWError._Error(e):    \n',
    '           print(异常)                    \n',
    '       NowKO = "Start() Run  = Error"     \n',
    '   # /                                    \n',
    '   return NowKO                           \n',


        ' ********* / 用 *********** '
    ]

    print(ThisREADME)













def _Error(e):
    # 翻譯
    #t1 = ATWLanguage._AutoWeb翻譯功能(e,'zh')    ## zh-Hant
    异常 = [
        '========= _Error ===========',
        e,      # Error說明,
        e.__traceback__.tb_frame.f_globals["__file__"], # 位置
        e.__traceback__.tb_lineno,  # 行
        '========= \ ==========='
    ]
    return 异常




if __name__ == "__main__":
    README()
    
    



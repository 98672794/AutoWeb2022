




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
from copy import Error




###################################################################################
############################################################# ATWFolder說明
def README(): 

    ThisREADME = [
        '*** ATWError.README ***', # PYfileName
        '发生异常所在的文件行数 =\n         _Error(e)',
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202051218',
        'https://98672794.github.io/'
    ]

    ATWREADME._READYourME(ThisREADME)













def _Error(e):
    #print(e)
    #print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    #print(e.__traceback__.tb_lineno)                        # 发生异常所在的行数

    异常 = 'Error***'
    + (e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    +(e.__traceback__.tb_lineno)                        # 发生异常所在的行数
    +'***'
    
    return 异常




if __name__ == "__main__":
    README()
    
    



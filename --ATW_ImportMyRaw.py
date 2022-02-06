




'''
winpy3

說明
ATW_ImportMyRaw
# https://www.codestudyblog.com/programmershop/index.php


ATW202202061727
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-


import os
import _atw._py.ATWREADME  
# auto my import
try:
    
    import requests
    import _atw._py.ATW_LoginATW    
    import _atw._py.ATWREADME  
    # thisPY/_atw/_py/ATW_LoginATW  
except ImportError:
    os.system('pip install requests')
    import requests

    #os.system('pip install ATWREADME')
    #import ATWREADME




###################################################################################
############################################################# ATW_Import 說明
def README(): 

    ThisREADME = [
        '*** ATW_ImportMyRaw.README ***', # PYfileName
        'try =\n        try',
        ' ==== 恭賀新禧 ==== ',
        'mokaki ATW202202061727',
        'https://98672794.github.io/'
    ]

    ATWREADME._READYourME(ThisREADME)








if __name__ == "__main__":
    README()












'''
winpy3

說明
ATW_Import
# https://www.codestudyblog.com/programmershop/index.php


ATW202202061727
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-



import ATWREADME


###################################################################################
############################################################# ATW_Import 說明
def README(): 

    ThisREADME = [
        '*** ATW_Import.README ***', # PYfileName
        'try =\n        try',
        ' ==== 恭賀新禧 ==== ',
        'mokaki ATW202202061727',
        'https://98672794.github.io/'
    ]

    ATWREADME._READYourME(ThisREADME)










###################################################################################
############################################################# _ATWImportThis
def _ATWImportThis(py): 

    try:
        import py
        OK = '_ATWImportThis = OK'
    except ImportError:
        ffff = 'pip install ' + str(py)
        ATWREADME.os.system(ffff)
        import py
        OK = '_ATWImportThis = Error'

    return OK

        #os.system('pip install ATWREADME')
        #import ATWREADME





if __name__ == "__main__":
    importThisHaHa = 'nltk'
    print(_ATWImportThis(importThisHaHa))
    #README()
    
    



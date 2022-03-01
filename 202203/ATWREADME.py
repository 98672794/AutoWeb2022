




'''
winpy3

說明
README
ATW202202051150
mokaki
https://98672794.github.io/
'''
# -*- coding: UTF-8 -*-

import os



###################################################################################
############################################################# README 說明
def README(): 

    ThisREADME = [
        '*** ATWREADME.README ***', # PYfileName
        'printList =\n        _READYourME(READMETxtList)',
        ' ==== 恭賀新禧 ==== ',
        'mokaki202202042',
        'https://98672794.github.io/'

    ]

    _READYourME(ThisREADME)





########################################################################## READ your ME
def _READYourME(READMETxtList): # printYourREADME(READMETxtList)

    # TxtList loop print
    for txt in READMETxtList:
        print ("\n   ",txt,"\n")
    
    # END
    print ("\n    *** / ***\n")
    os.system("pause")








if __name__ == "__main__":
    README()
    
    



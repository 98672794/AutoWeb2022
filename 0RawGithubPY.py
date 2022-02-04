

'''
winpy3

0RawGithubPY
執行Github中的.py
ATW202202042022
mokaki
https://98672794.github.io/

https://stackoverflow.com/questions/54963794/read-python-code-from-github-and-execute-locally

'''

# -*- coding: UTF-8 -*-
##########################################################################import
import os
import urllib.request

ATW202202041958 = 'https://raw.githubusercontent.com/98672794/py/main/1index.py'





###################################################################################
############################################################# 0RawGithubPY 說明
def README(): 
    print ("\n*** README ***\n")
    t = [
        ' ==== BUG ==== ',
        ' rwa不能import ',
        ' ==== BUG ==== ',
        'mokaki',
        'https://98672794.github.io/',
        '202202042044',
        ' ==== 恭賀新禧 ==== ',
        '0RawGithubPY.',
        '執行在Github的PYRaw檔 =\n    執行GithubPYRaw(PYRaw網址)'
    ]
    for txt in t:
        print ("\n   ",txt,"\n")
    print ("\n*** /README ***\n")
    os.system("pause")








###################################################################################
############################################################# 執行GithubPYRaw(PYRaw網址)
def 執行GithubPYRaw(PYRaw網址):

    # 解碼
    response = urllib.request.urlopen(PYRaw網址)
    data = response.read()
    # 執行
    exec(data)









if __name__ == "__main__":
    README()
    執行GithubPYRaw(ATW202202041958)
    os.system("pause")
    
    



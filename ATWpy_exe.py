
'''

202202262155 mokaki

https://zhuanlan.zhihu.com/p/162237978
'''


# -*- coding: UTF-8 -*-

from multiprocessing import Event
import os


def MakeExe():

    Talk = '''
        ****************
        將 Python.py 封裝exe 
        歡迎您 

        請將您的 .py .ico 放在本文件夾

        *生成的.exe會放在dist文件夾

        您可以將python程式分享給朋友
        朋友的電腦無需安裝python 也不需任何設定 
        即可直接執行封裝好的.exe
        ****************
        '''


    # install pyinstaller
    os.system('pip install pyinstaller')


    # 找出現在目錄所有.py 2022
    #ss = os.listdir(".")
    print(Talk)
    for item in os.listdir("."): 
        if(item.endswith('.py')):
            print(item)
        if(item.endswith('.ico')):
            print(item)


    print('****************')
    while True: # 不能空值loo
        PyName = input('請填寫要封裝的.py文件名(不需.py)')
        if PyName == '': continue
        IcoName = input('請填寫圖示的.ico名(不需.ico)')
        if IcoName == '': continue
        break

    # 加副檔名
    AllName = 'pyinstaller -F -w -i '+IcoName+'.ico '+PyName+'.py'

    # 封裝exe
    os.popen(AllName)

    ok = '生成的.exe已放在dist文件夾'
    return ok





if __name__=='__main__':
    
    print(MakeExe())
    print('****************')
    #os.system("pause")

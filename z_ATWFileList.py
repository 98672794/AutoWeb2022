
import os


def ATWFileList(HtmlUrl,n2):
    global ATWFileList0
    # ATWFileList
    # 找出現在目錄所有.py
    L1 = [] 
    L1.clear()
    ss = os.listdir(HtmlUrl)
    for item in ss: 
        if(item.endswith(n2)):
            L1.append(item)
    i = 0
    while i < len(L1):
        print('   ',i,'=====',L1[i],'\n')
        i+=1

    while True:
        ImportPyUrl = input('\n   請填寫文件號\n   或直接填寫文件名和路徑，如 ./path'+n2+'\n')
        # 不能空值
        if ImportPyUrl == '':
            continue
        # 查 ImportPyUrl 是否 int
        try:
            ATWFileList0 = L1[int(ImportPyUrl)]
            break
        except:
            break

    # 不存在，請從試 返回 ImportPyUrl
    #ATWFileList0 = ImportPyUrl


    ###########################################











######################################################################################################
######################################################################## 用「例外處理」檢查檔案是否存在  
def IfHaveFile(target_file):

    try:
        file = open(target_file, 'r')
    except FileNotFoundError:
        gfdg = (target_file + '不存在')
        OK = 0
    except PermissionError:
        gfdg = (target_file + '不是檔案')
        OK = 0
    else:
        gfdg = (target_file + '檔案存在')
        OK = 1
        file.close()

    print ('gfdg,',gfdg)
    return OK




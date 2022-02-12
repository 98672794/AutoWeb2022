

def ATWReadFile(OutData,NewData,sel):
    
    #global ATWReadFileList0

    #print(' *OutData** ',OutData,' *** ')
    



    if sel == 'LSF':
        # loop Save File                   loop save
        f2p = open( NewData , "a", encoding="utf-8" )
        f2p.writelines(OutData+'\n')
        f2p.close()

    # List to File list 轉 新文件    w = 创新删舊
    if sel == 'LTF':
        f2p = open( NewData , "w", encoding="utf-8" ) 
        count=len(OutData)      #   OutData = list
        i = 0
        while i < count: 
            f2p.writelines(OutData[i])
            i+=1 
        f2p.close()




    # File to List 查看文件每一行 返回 List
    elif sel == 'FTL':
        with open( OutData , 'r', encoding="utf-8" )   as fp:
            count=len(open( OutData , 'r', encoding="utf-8" ) .readlines())
            
            ATWReadFileList0 = [] 
            ATWReadFileList0.clear()
            i = 0
            while i < count: 
                line = fp.readline()
                ATWReadFileList0.append(line)   
                i+=1
    
        return ATWReadFileList0


    # File to File 抄寫新文件    w = 创新删舊
    elif sel == 'FTF':
        with open( OutData , 'r', encoding="utf-8" )   as fp:
            count=len(open( OutData , 'r', encoding="utf-8" ) .readlines())

            f2p = open( NewData , "w", encoding="utf-8" ) 
            i = 0
            while i < count: 
                line = fp.readline()
                f2p.writelines(line)
                i+=1 
            f2p.close()
            

    #print("\n *** SAVE ",NewData, " DONE *** \n")









    ###########################################

#   sel == 'LTF':    List to File               list 轉 新文件 
#   sel == 'FTF':    File to File                   抄寫新文件
#   sel == 'FTL':    File to List     查看文件每一行 返回 List
#   sel == 'LSF':    loop Save File                 loop save










# /././.
# List to File list 轉 新文件    w = 创新删舊
def ListToFile(List,FileName):
    count=len(List)      #   OutData = list
    i = 0
    with open(FileName, 'w', encoding="utf-8") as kf:
        while i < count: 
            kf.writelines(List[i])
            i+=1 
        kf.close()








# 202111021505
# Txt To list 多文用 to 轉 list 
# https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
def TxtToList(txt,to):
    NewTxt = txt.split(to)
    return NewTxt
    
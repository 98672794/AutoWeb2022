

def ATWGetListKeyTxt(KeyTxt,List,NewTxt,sel):
    
    global ATWGetListKeyTxt0
    global ATWGetListKeyTxt1Nb

    ATWGetListKeyTxt0 = []
    ATWGetListKeyTxt0.clear()

    if sel == 'LGT':
        # kw = List 中所有
        for kw in List:
            # 如 關鍵字在 add list
            if KeyTxt in kw:
                ATWGetListKeyTxt0.append(kw)

    if sel == 'LCT':
        # List 轉新 關鍵字
        i = 0
        while i < len(List):
            ttt = List[i]   # QQQQQQQQ
            if KeyTxt == ttt:
                #print('   List[',i,']  =\n{',List[i],'}\n')
                List[i] = NewTxt+"\n"
                ATWGetListKeyTxt1Nb = i
                #print('   List[',i,']  =\n{',List[i],'}\n')
            i+=1
        for kw in List:
            ATWGetListKeyTxt0.append(kw)

    #print('   ATWGetListKeyTxt0 =\n{',ATWGetListKeyTxt0,'}\n')

    ###########################################

# sel == 'LGT' == List中找關鍵字
# sel == 'LCT' == List 轉新 關鍵字
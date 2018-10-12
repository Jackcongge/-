Money=input("请输入要转换的金额数目:")
if Money[-1] in ['y','Y']:
    M=eval(Money[:-1])/6
    print("兑换后的美元是{:.2f}D".format(M))
elif Money[-1] in ['d','D']:
    M=6*eval(Money[:-1])
    print("兑换后的人民币是{:.2f}F:".format(M))
else:
    print("输入格式错误:")

Tempstr=input("请输入带有符号的温度值：")
if Tempstr[-1]   in   ['f','f']:
    C=eval(Tempstr[0:-1]-32)/1.8
    print("华氏温度{}转换为摄氏温度是:{:.2f}C".format(tempstr,c))
elif  Tempstr[-1]in['c','c']:
       F=eval(Tempstr[0:-1])*1.8+32
       print("摄氏温度{}转换为华氏温度是:{:.2f}F".format(Tempstr,F))
else:
    print("输入格式错误")

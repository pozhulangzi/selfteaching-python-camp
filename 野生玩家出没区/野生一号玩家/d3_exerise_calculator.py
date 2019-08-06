################ 计 算 器 1.0 #########################

# #定义函数
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multipy(x,y):
#     return x*y
# def divide(x,y):
#     return x/y

# #用户输入
# print('''
# 选择运算：
# 1、加    2、减
# 3、乘    4、除''')


# choice=input("请输入你的选择(序号)：")

# num1=int(input('请输入第一个数字:'))
# num2=int(input('请输入第二个数字:'))

# if choice=='1':
#     print(num1,'+',num2,'=',add(num1,num2))
# elif choice=='2':
#     print(num1,'-',num2,'=',subtract(num1,num2))
# elif choice=='3':
#     print(num1,'*',num2,'=',multipy(num1,num2))
# elif choice=='4':
#     print(num1,'/',num2,'=',divide(num1,num2))
# else:
#     print('非法输入')


################### 计 算 器 2.0 ########################

#定义函数
def divide(x,y):
    if y==0:
        print("两数相除，分母不得为零")
    else:
        return x/y

#用户选择
choice=int(input('''
请选择运算:
1、相加   2、相减
3、相乘   4、相除'''))

##输入数字
num1=int(input("请输入第一个数字："))
num2=int(input('请输入第二个数字：'))

#后台运算
if   choice==1:
    print("{}+{}={}".format(num1,num2,num1+num2))
elif choice==2:
    print("{}-{}={}".format(num1,num2,num1-num2))
elif choice==3:
    print("{}*{}={}".format(num1,num2,num1*num2))
elif choice==4:
    print("{}/{}={}".format(num1,num2,divide(num1,num2)))
else:
    print("你的输入非法！")

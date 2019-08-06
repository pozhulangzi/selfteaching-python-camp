#版本1.0
# for x in range(1,10):
#     for y in range(1,x+1):
#         print("{}*{}={}".format(y,x,x*y),end=" ")
#     print()

#版本2.0
for x in range(1,10):
    while x % 2==0:
        break
    else:
        for y in range(1,x+1):
            print("{}*{}={}".format(y,x,x*y),end=" ")
    print( )

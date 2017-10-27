#__author:  sujunjun
#date:  17/10/3

# _user = "jun"
# _pass = "123"
# count = 0
# #flag = False;
# #for i in range(3):
# while count < 3:
#     userName = input("user")
#     passWord = input("passwd")
#     if userName == _user and _pass == passWord:
#         print("success,Welcome %s" %(userName))
#         #flag = True
#         break
#     else:
#         print("userName or passWord error!")
#     count += 1
#     if count == 3:
#        go_on  = input("还想玩吗");
#        if go_on == "y":
#            count = 0
# else:  #只要循环正常执行完毕之后就会走else,当有break时不会走else
#      print("滚犊子")
# #if not flag:
#     #print("滚")
#
# print("end")
flag = False
for i in range(10):
    for j in range(10):
        if j == 5:
            flag = True
            break;
        print(j,end=" ")
    print(i)
    if flag == True:
        break;
#bcd
#第三个负号代表方向从右往左取, 反之从左向右取
a = ['a','b','c','d','e']  #[loc:取多少个元素]
#print(a[-2::-2])  #想让bd 颠倒
#print(a[3::-2])  #想让bd 颠倒
print(a[1:-1:-1]) #????首先从左往右数:第一位是b ,第二位-1是e,所以不包括e,也就是中间的bcd ,第三位是负数2,所以从起点b开始往左变换步长为2,因为不够所以为空

#只要第二位为负数,并且第三位还是负数,那么就是空  -2 : :1
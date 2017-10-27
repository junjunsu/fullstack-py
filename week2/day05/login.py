#__author:  sujunjun
#date:  17/10/3


# for i in range(1,101):
#     if i % 2 == 1:
#         print(i);

_user = "jun"
_pass = "123"
flag = False;
for i in range(3):
    userName = input("user")
    passWord = input("passwd")
    if userName == _user and _pass == passWord:
        print("success,Welcome %s" %(userName))
        flag = True
        break
    else:
        print("userName or passWord error!")
# else:  #只要循环正常执行完毕之后就会走else,当有break时不会走else
#     print("滚犊子")
if not flag:
    print("滚")

print("end")




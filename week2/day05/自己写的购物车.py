#__author:  sujunjun
#date:  17/10/4

salary = 600

shop = ['iphone6s','mac_book','coffee','python_book','bicycle']

shop_info = '''
%s    5800
%s    9000
%s    32
%s    80
%s    1500
'''%(shop[0],shop[1],shop[2],shop[3],shop[4])
print(shop_info)
final_money = flag5 = flag4 = flag3 = flag1 = flag2 =  0

while True:
    choice_num = input("请选择您要购买的商品:")
    if choice_num == '0':
            flag1 = 5800
            print("已加入%s到您的购物车" %(shop[0]))
    elif choice_num == '1':
            flag2 = 9000
            print("已加入%s到您的购物车" % (shop[1]))
    elif choice_num == '2':
            flag3 = 32
            print("已加入%s到您的购物车" % (shop[2]))
    elif choice_num == '3':
            flag4 = 80
            print("已加入%s到您的购物车" % (shop[3]))
    elif choice_num == '4':
            flag5 = 1500
            print("已加入%s到您的购物车" % (shop[4]))

    final_money = salary - flag1 - flag2 - flag3 - flag4 - flag5
    if final_money <=  0:
         go_on_buy = 'y'
         print("余额不足 %s ,请充值" %(salary - 5800))
    go_on_buy = input("是否继续购买y/n")
    if go_on_buy == 'n':
        if  final_money and final_money > 0:
            print("当前余额为%s"%final_money)
            print("您已经购买以下商品")
            if flag1:
                print("%s ---- %s" %(shop[0],5800))
            if flag2:
                print("%s ---- %s" %(shop[1],9000))
            if flag3:
                print("%s ---- %s" %(shop[2],32))
            if flag4:
                print("%s ---- %s" %(shop[3],80))
            if flag5:
                print("%s ---- %s" %(shop[4],1500))
            print("欢迎下次光临!")
            break
        else:
            print("欢迎下次光临!")
            break;
    else:
        continue

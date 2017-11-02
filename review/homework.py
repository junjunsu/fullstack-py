import re
# 实现加减乘除及括号优先级解析
# 用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
# 必须自己解析里面的(),+,-,*,/符号和公式(不能调用eval等类似功能偷懒实现)，运算后得出结果，结果必须与真实的计算器所得出的结果一致


s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#去掉空
def formatStr(string):
    string = string.replace(' ', '')
    string = string.replace('+-', '-')
    string = string.replace('++', '+')
    string = string.replace('/+', '/')
    string = string.replace('--', '+')
    string = string.replace('-+', '-')
    string = string.replace('*+', '*')
     #*-
     #/-怎么替换
    return string

#检查表达式合法性
def check_expression(string):
    check_result = True
    #括号是否匹配
    if not string.count("(") == string.count(")"):
        print('表达式错误,括号未闭合')
        check_result = False
    if re.search('[a-z]+', string.lower()):
        print('表达式包含非法字符')
        check_result = False

    return check_result

#计算乘除法:
def calcMulDiv(string):
    #2+2.4*4.2*22
    #从字符串获取一个乘法或除法的表达式
    regular = '\d+\.?\d*([*/]|\*\*)[\-]?\d+\.?\d*'
    #如果还能找到乘法或除法表达式
    while re.findall(regular,string):
        #获取表达式
        expression = re.search(regular,string).group()

        #如果是乘法
        if expression.count("*") == 1:
            #获取要计算的两个数
            x, y = expression.split("*")
            #计算结果
            mul_result = str(float(x) * float(y))
            #将计算的表达式替换成计算结果值
            string = string.replace(expression,mul_result)
            #格式化一下
            string = formatStr(string)

        #如果是除法:
        if expression.count("/"):
            # 获取要计算的两个数
            x, y = expression.split("/")
            # 计算结果
            mul_result = str(float(x) / float(y))
            # 将计算的表达式替换成计算结果值
            string = string.replace(expression, mul_result)
            # 格式化一下
            string = formatStr(string)
        if expression.count("*") == 2:
            x,y = expression.split("**")
            pow_result = 1
            for i in range(int(y)):
                pow_result *= int(x)
            string = string.replace(expression,str(pow_result))
            string = formatStr(string)
    return string

    # res = re.search('\d+\.?\d*[*/]\d+\.?\d*',s)  #2.4*4.2
    # if res:
    #     p = res.group()
    #     if  re.search('[*]',p):
    #         resp = re.split('[*]', p)
    #         ress = float(resp[0]) * float(resp[1])
    #     else:
    #         resp = re.split('[/]', p)
    #         ress = float(resp[0]) / float(resp[1])
    #     #替换:
    #     ress_int = int(ress)
    #     s = s.replace(p,str(ress_int))
    # return s[1:-1]

def calcAddSub(string): #2776672.6952380957
    add_regular = '[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'
    sub_regular = '[\-]?\d+\.?\d*\-[\-]?\d+\.?\d*'
    #开始加法:
    while re.findall(add_regular,string):
        #把所有的加法都算完,获取所有加法表达式
        add_list = re.findall(add_regular,string)
        for add_str in add_list:
            #获取两个加法的数
            x, y = add_str.split("+")
            add_result = "+" + str(float(x) + float(y))
            string = string.replace(add_str,add_result)
        string = formatStr(string)
    # 开始减法:
    while re.findall(sub_regular, string):
        # 把所有的加法都算完,获取所有加法表达式
        sub_list = re.findall(sub_regular, string)
        for sub_str in sub_list:
            # 获取两个加法的数
            numbers = sub_str.split("-")
            #-3-5的情况split会返回3个值
            if len(numbers) == 3:
                result = 0
                for v in numbers:
                    if v:
                        result -= float(v)
            else:
                x, y = numbers
                result = float(x) - float(y)
            #替换字符串
            string = string.replace(sub_str, "+" + str(result))
        string = formatStr(string)
    return string



if __name__ ==  "__main__":
    #s = '(1+5)*5'
    source = s
    if check_expression(source):
        print("source:",source)
        print("eval_result:",eval(source))
        source = formatStr(source)
    while source.count("(") > 0: #
        #格式化
        #去括号,得到括号的字符串,结果如(30+6/3)
        strs = re.search('\([^()]*\)', source).group()
        #将括号的表达式进行乘除运算
        replace_str = calcMulDiv(strs)
        #将运算的结果在进行加减运算
        replace_str = calcAddSub(replace_str)
        #将括号的字符串替换为计算结果,结果包含(),替换时去掉() -> [1:-1]
        source = formatStr(source.replace(strs,replace_str[1:-1]))
    else:
        #没有括号就到最后的单一表达式
        replace_str = calcMulDiv(source)
        #算乘除
        replace_str = calcAddSub(replace_str)
        #算加减
        source = source.replace(source,replace_str)
    print("result:",source.replace("+",""))


    # while source.count("(") > 0: #
    #     #处理里面的表达式
    #     rek = re.search('\([^()]+\)', res)
    #     if rek:
    #        k = rek.group()
    #
    #         #处理表达式
    #        reb = handelCompute(k)
    #        rel = handlePlusSub(reb)
    #        res = res.replace(k,str(rel))
    #        res = formatStr(res)
    #
    # else:
    #     #直接计算
    #     pass




#-*-coding:utf-8-*-
import json
dic = {"name":"小军","age":18,"hobby":"singsing"}
format_dic = json.dumps(dic)
#print(format_dic)

f = open('json_t','w')
f.write(format_dic)
f.close()


#===========================dump
#dump省略了f.write()
# dic1 = {"name":"小军","age":18,"hobby":"singsing"}
# f = open('json_t2','w')
# format_dic1 = json.dump(dic1,f)
# f.close()

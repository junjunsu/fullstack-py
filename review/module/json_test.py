import json
# dumps--------------------------------------
# dict = {"user_name":"张三","age":"100"}
# data = json.dumps(dict)
# f = open('json_t','w')
# f.write(data)

# f = open('json_t','r')
# data = json.loads(f.read())
# print(data.get('user_name'))
# print(data['age'])


#dump----------------------------------------
# dict = {"user_name":"张三小三","age":"10000"}
# f = open('json_t','w')
# json.dump(dict,f)

f = open('json_t','r')
#json.load(f)['user_name']
data = json.load(f)
print(data.get('user_name'))


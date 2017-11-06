import shelve

#dict = {"userName":"小红",'job':"it"}
f = shelve.open(r'shelve_t')
#f['info'] = dict
data = f.get('info')
#data = f['info']
print(data)
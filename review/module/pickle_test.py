import pickle
# def foo():
# 	print('ok')
#data = pickle.dumps(foo) #b'\x80\x03c__main__\nfoo\nq\x00.'
#print(data)
#exit()
#f = open('pickle_t','wb')
#f.write(data)

# f = open('pickle_t','rb')
# data = f.read()
# print(pickle.loads(data)())

#_---------------------------------dump
def foofoo():
	print('oks')
# f = open('pickle_t','wb')
# pickle.dump(foofoo,f)
f = open('pickle_t','rb')
print(pickle.load(f)())





#如果遇到跟当前当前某一个对象相关的方法的时候,我们定义成普通方法就可以了,不依赖用类方法或静态方法
#uuid根据本机ip或版本号,主板,当前时间自动生成的随机字符串,永远不重复
import uuid   #唯一标识用uuid标识(学校)
print(uuid.uuid1())
#以后进行关联用唯一id
#唯一id弊端:

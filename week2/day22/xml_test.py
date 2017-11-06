import xml.etree.ElementTree as ET

tree = ET.parse("xml_test.xml")  #
#print(tree)#<xml.etree.ElementTree.ElementTree object at 0x10c27f2b0>
root = tree.getroot()
#print(root.tag) #data 根

# 遍历xml文档
#for child in root:
	#print(child.tag, child.attrib)
	# for i in child:
	# 	print(i.tag, i.text)

# 只遍历year 节点
# for node in root.iter('year'):
# 	print(node.tag, node.text)
# ---------------------------------------

import xml.etree.ElementTree as ET

tree = ET.parse("xml_test.xml")
root = tree.getroot()

# 修改
# for node in root.iter('year'):
# 	new_year = int(node.text) + 1
# 	node.text = str(new_year)
# 	node.set("is_update", "yes") #设置属性
#
# tree.write("xml_test.xml")

# 删除node
for country in root.findall('country'):
	rank = int(country.find('rank').text)
	if rank > 50:
		root.remove(country)
tree.write('output.xml')
exit()


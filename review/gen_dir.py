

import os


class dir(object):
	def __init__(self):
		self.SPACE = ""
		self.list = []

	def getCount(self, url):
		files = os.listdir(url)
		count = 0;
		for file in files:
			myfile = url + "/" + file #window就把\ 改成\\就行
			if os.path.isfile(myfile):
				count = count + 1
		return count

	def getDirList(self, url):
		files = os.listdir(url)
		fileNum = self.getCount(url)
		tmpNum = 0

		for file in files:
			myfile = url + "/" + file
			size = os.path.getsize(myfile)

			if os.path.isfile(myfile):
				tmpNum = tmpNum + 1
				if (tmpNum != fileNum):
					self.list.append(str(self.SPACE) + "├─" + file + "\n")
				else:  # www.iplaypy.com
					self.list.append(str(self.SPACE) + "└─" + file + "\n")

			if os.path.isdir(myfile):
				self.list.append(str(self.SPACE) + "├─" + file + "\n")
				# change into sub directory
				self.SPACE = self.SPACE + "│  "
				self.getDirList(myfile)
				# if iterator of sub directory is finished, reduce "│  "
				self.SPACE = self.SPACE[:-4]
		return self.list

	def writeList(self, url):
		f = open(url, 'w',encoding='utf8')
		#print(self.list)

		f.writelines(self.list)
		print("ok")

		f.close()


if __name__ == '__main__':
	d = dir()
	path = os.path.dirname(os.path.abspath(__file__))+'/alex_atm'

	d.getDirList(path)  # input directory
	d.writeList(path+"/READ")  # write to fil
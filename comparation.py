#!coding=utf-8
import xlrd

def run(name):				#创建一个函数run()
	lists=[]   				#创建列表
	workbook = xlrd.open_workbook(name)         #打开一个workbook
	worksheet = workbook.sheets()[0]		    #通过索引顺序获取
	num_rows = worksheet.nrows             		#遍历行num_rows

	for rown in range(num_rows):
			cella = worksheet.cell_value(rown,0)   #找到变量中的内容
			lists.append(cella)               #append() 增加对象     把找到的变量加到lists中

	return lists 

if __name__=="__main__":          #规范写法，函数在这里开始执行

	a=run("a.xls")
	b=run("b.xls")

	for i in a:
		for j in b:
			if i==j:
			 print "same content:%s" % i
		





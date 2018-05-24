from multiprocessing import Pool
import os

def copy_file(name, oldFolderName, newFolderName):
	'完成copy一个文件的功能'

	with open(oldFolderName+'/'+name,'rb') as fr:
		content = fr.read()

	with open(newFolderName+'/'+name,'wb') as fw:
		fw.write(content)


def main():

	#获取用户copy文件名
	oldFolderName = input('请输入你要拷贝的文件名: ')
	#1.创建一个文件夹
	newFolderName = oldFolderName + '-复件'
	#print(newFolderName)
	os.mkdir(newFolderName)
	#2.获取old文件夹中所有文件的文件名
	oldFileName = os.listdir(oldFolderName)
	#print(oldFileName)
	#3.使用多进程的方式copy源文件中的所有文件到新的文件夹中


	pool = Pool(5)

	for name in oldFileName:
		pool.apply_async(copy_file, args=(name,oldFolderName,newFolderName))
	
	pool.close()
	pool.join()

if __name__ == '__main__':
	main()
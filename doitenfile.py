import os
def sapxep(sort,files):
	for i in range(len(sort)-1):
		for j in range(i,len(sort)):
			if (sort[i]>sort[j]):
				temp=sort[j]
				sort[j]=sort[i]
				sort[i]=temp
				temp=files[j]
				files[j]=files[i]
				files[i]=temp
	return files

def doiten():
	duong_dan=os.getcwd()+"\\Data\\"
	files=os.listdir(duong_dan)
	name_change=input('Nhap ten can doi: ')
	sort=[]
	print(files)
	for i in files:
		sort.append(os.path.getctime(duong_dan+i))
	files=sapxep(sort,files)
	print(files)
	for i in range(len(files)):
		find=files[i].find(".")
		temp_file=files[i]
		temp=duong_dan+"\\"+files[i]
		rename=duong_dan+name_change+"_"+str(i+1)+temp_file[find:]
		os.rename(temp,rename)
if __name__=='__main__':
	print("Copy file can doi ten vao thu muc data ")
	doiten()
	print("Done")
import os
from shutil import copyfile
def gen_path(group,sub):
	return '/fdisk/dataset/'+str(group).zfill(3)+'/Display/pic_14_'+str(sub)+'.bmp'
def gen_path_out(group,sub):
	return '/fdisk/dataset_mix/'+str(group).zfill(3)+'_'+str(sub).zfill(3)+'.bmp'
for group in range(1,81):
	for sub in range(1,15):
		path=gen_path(group,sub)
		path_out=gen_path_out(group,sub)
		if os.path.exists(path):
			copyfile(path, path_out)
		else :
			print('error occur:'+path)

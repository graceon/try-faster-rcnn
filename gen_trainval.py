import os
import sys


path_trainval='/fdisk/tf-faster-rcnn/data/VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt'
path_cache='/fdisk/tf-faster-rcnn/data/cache/voc_2007_trainval_gt_roidb.pkl'

start=1
end=31+1

exclude= set()
for i in range(41,52):
	exclude.add(i)
exclude.add(57)
exclude.add(80)



flag_first=1

if os.path.exists(path_trainval)==0:
	print('error occur:'+path_trainval)
	exit(-1)
handle=open(path_trainval,mode='w')

for group in range(start,end):
	if group in exclude:
		continue
	for sub in range(1,15):
		if flag_first==1:
			flag_first=0
		else:
			handle.write('\n')
		handle.write(str(group).zfill(3)+'_'+str(sub).zfill(3))
handle.close()

if os.path.exists(path_cache):
	os.remove(path_cache)
	print('remove cache')
(base) root@GK5CS:~# source /temp/venv/bin/activate

(venv) (base) root@GK5CS:/fdisk/tf-faster-rcnn# cd /usr/local/cuda/lib64/
(venv) (base) root@GK5CS:/usr/local/cuda/lib64# ln -s libcufft.so.10 libcufft.so.10.0
(base) root@GK5CS:/fdisk/labelImg# python labelImg.py

./experiments/scripts/train_faster_rcnn.sh 0 pascal_voc res101
(base) root@GK5CS:/fdisk/try-faster-rcnn# python3 gen_test.py 28

tf.test.is_gpu_available()
export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:"$LD_LIBRARY_PATH:/usr/loacl/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"
tfconfig.gpu_options.allow_growth=True
tfconfig.gpu_options.per_process_gpu_memory_fraction = 0.4




step 1:
	rm /fdisk/tf-faster-rcnn/data/cache
	rm /fdisk/tf-faster-rcnn/data/VOCdevkit2007/annotations_cache
todo :
	edit res101yml
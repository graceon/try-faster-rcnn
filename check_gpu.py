import tensorflow as tf

res=tf.test.is_gpu_available()


tfconfig = tf.ConfigProto(allow_soft_placement=True)
tfconfig.gpu_options.allow_growth=True
tfconfig.gpu_options.per_process_gpu_memory_fraction = 0.4
print(res)
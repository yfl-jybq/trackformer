import os 


for i in range(18,29):
    with open("result.txt", "a") as f:
        f.writelines("id:"+str(i)+";")
    '''
    path = '/home/yfl/passenger-flow-detection/yolov5-deepsort/'+'test_vedio/hualian_test_'+str(i)+'.mp4'
    os.system('rm -rf data/test2/*')
    os.system('ffmpeg -i '+path+' -vf fps=15 data/test2/%06d.png')
    '''
    input_name = '/home/yfl/passenger-flow-detection/yolov5-deepsort/'+'test_vedio/hualian_test_'+str(i)+'.mp4'
    output_name = 'result'+str(i)+'.mp4'
    os.system('python src/track.py with \
    dataset_name=DEMO \
    data_root_dir=data/test2 \
    output_dir=data/test2 \
    output_name='+output_name+' \
    input_name='+input_name+' \
    write_images=pretty')
'''
input_name = '/home/yfl/passenger-flow-detection/yolov5-deepsort/'+'test_vedio/test'+'.mp4'
output_name = 'result'+'.mp4'
os.system('python src/track.py with \
dataset_name=DEMO \
data_root_dir=data/test2 \
output_dir=data/test2 \
output_name='+output_name+' \
input_name='+input_name+' \
write_images=pretty')
'''
    
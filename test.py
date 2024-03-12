import os 

'''
for i in range(18,29):
    with open("result.txt", "a") as f:
        f.writelines("id:"+str(i)+";")
    path = '/home/yfl/passenger-flow-detection/yolov5-deepsort/'+'test_vedio/hualian_test_'+str(i)+'.mp4'
    os.system('rm -rf data/test2/*')
    os.system('ffmpeg -i '+path+' -vf fps=15 data/test2/%06d.png')
    #input_name = '/home/yfl/passenger-flow-detection/yolov5-deepsort/'+'test_vedio/hualian_test_'+str(i)+'.mp4'
    input_name = "test_1.mp4"
    output_name = 'result'+str(i)+'.mp4'
    os.system('python src/track.py with \
    dataset_name=DEMO \
    data_root_dir=data/test2 \
    output_dir=data/test2 \
    output_name='+output_name+' \
    input_name='+input_name+' \
    write_images=pretty')

for i in range(13,14):
    with open("result.txt", "a") as f:
        f.writelines("id:"+str(i)+";")
    input_name = '/home/yfl/Passenger-flow-detection/data'+'/test_'+str(i)+'.mp4'
    output_name = 'result'+str(i)+'.mp4'
    os.system('python src/track.py with \
    dataset_name=DEMO \
    data_root_dir=data/test2 \
    output_dir=data/test \
    output_name='+output_name+' \
    input_name='+input_name+' \
    write_images=pretty')
'''
os.system('python src/track.py with \
dataset_name=DEMO \
data_root_dir=data \
output_dir=data \
output_name=result_34.mp4 \
input_name=/home/linhui/test_trackformer/trackformer/test_34.mp4 \
poly_pass=1007,711,492,1076,2189,1274,2239,746 \
write_images=pretty')
    
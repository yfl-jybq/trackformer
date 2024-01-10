
import cv2
 
# 打开视频文件
video = cv2.VideoCapture('/home/yfl/passenger-flow-detection/yolov5-deepsort/'+'test_vedio/hualian_test_'+str(20)+'.mp4')
 
# 获取视频的帧数、每帧的时间等信息
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
# 设置需要截取的起始帧和结束帧（这里从第1帧到第500帧）
start_frame = 1
end_frame = 2000
 
# 创建输出视频对象并指定编码器类型及参
output_file = '/home/yfl/passenger-flow-detection/yolov5-deepsort/'+'test_vedio/test2'+'.mp4'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height), isColor=True)
 
# 读取视频帧并写入输出视频对象
for i in range(total_frames):
    ret, frame = video.read()
    
    if not ret or i < start_frame - 1:
        continue
        
    # 判断当前帧是否为所选区间内的帧
    if start_frame <= i <= end_frame:
        out.write(frame)
    
    # 显示处理过程
    print("Processing Frame {}/{}".format(i+1, total_frames))
 
# 关闭视频流和输出视频对象
video.release()
out.release()
print("Finished!")
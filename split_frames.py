import cv2

vidcap = cv2.VideoCapture('dataset/Video/S07_Brownie_Video/S07_Brownie_7150991-1431.avi')
success, image = vidcap.read()
count = 0

while success and count < 706:
    cv2.imwrite('dataset/frames/S07/frame_%d.jpg' % count, image)
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
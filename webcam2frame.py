import cv2

save='./ourfaces/'
current_video = cv2.VideoCapture(0)
# set webcam size
current_video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
current_video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

idx = 0
img_idx = 0

while current_video.isOpened():
    status, current_frame = current_video.read()
    current_crop = current_frame[:,100:381]
    scale_percent = 50 # percent of original size
    width = int(current_crop.shape[1] * scale_percent / 100)
    height = int(current_crop.shape[0] * scale_percent / 100)
    dim = (width, height)
     # resize image
    resized = cv2.resize(current_crop, dim, interpolation = cv2.INTER_AREA)
    filename = 'webcam_'+str(img_idx)+'.png'
    if idx>0 and idx%5 == 0:
        img_idx += 1
        cv2.imwrite(save+filename,current_frame)
    cv2.imshow("webcam", current_frame)
    idx += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#out.release()
current_video.release()
cv2.destroyAllWindows()
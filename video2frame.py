import cv2

save='write saving directory'
current_video = cv2.VideoCapture('write video directory')
idx = 0
img_idx = 0

while current_video.isOpened():
    status, current_frame = current_video.read()
    #write x,y to crop image
    current_crop = current_frame[:,:]
    
    scale_percent = 50 # percent of original size
    width = int(current_crop.shape[1] * scale_percent / 100)
    height = int(current_crop.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(current_crop, dim, interpolation = cv2.INTER_AREA)
    # save image
    filename = 'crop_'+str(img_idx)+'.jpg'
    
    if idx>0 and idx%2 == 0:
        img_idx += 1
        cv2.imwrite(save+filename,resized)
    cv2.imshow("Sobel", resized)
    idx += 1
    #press Q to break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

current_video.release()
cv2.destroyAllWindows()
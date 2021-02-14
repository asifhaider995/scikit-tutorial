import os
import cv2
import time

img_arr = []
dataPath = os.getcwd()+("/data/train")
dataP = os.getcwd() + "/data-p"

for i in os.listdir(dataPath):
    img = cv2.imread(dataPath+'/'+i, 1)
    img_arr.append(img)

# i = 0    
# while True:
val = 0
# print(img_arr)
count = 0
for image in img_arr:
    img = image
    h = 130
    w = 65
    x = 0
    y = 0
    step_w = 25
    step_h = 50
    H, W = img.shape[:2]
    for height in range(0, H, step_h):
        for width in range(0, W, step_w):
            crop = img[height: height+h , width: width+w]
            crop_h, crop_w = crop.shape[:2]
            if crop_h == h and crop_w == w: 
                cv2.imwrite(dataP+"/"+str(count)+".jpg", crop)
            count += 1
    # while True:
    #     cv2.imshow("Actual", img)
    #     cv2.imshow("Cropped", cropped)
    #     # i += 1
    #     # time.sleep(1)
    #     if cv2.waitKey(1) & 0xFF == ord('n'):
    #         break
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         val = 1
    #         break
    # if val == 1:
    #     break
# H, W = img.shape[:2]
# count = 0
# for y in range(0, H, h):
#     for x in range(0, W, w):
#         crop = img[y: y+h, x: x+w]
#         cv2.imwrite(dataP+"/"+str(count)+".jpg", crop)
#         count += 1


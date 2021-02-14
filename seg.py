import os
import cv2

# src = os.getcwd() + "/data-p"

dest_n = os.getcwd() + "/negatives"
dest_p = os.getcwd() + "/positives"

# src_f = os.listdir(src)

# def segregate():
#     for f in src_f:
#         img = cv2.imread(src + "/" + f)
#         cv2.imshow("Image", img)
#         # file_src = src+"/"+f
#         if cv2.waitKey(10000) & 0xFF == ord('i'):
#             cv2.imwrite(dest_n+"/"+str(f)+".jpg", img)
#         elif cv2.waitKey(10000) & 0xFF == ord('e'):
#             cv2.imwrite(dest_p+"/"+str(f)+".jpg", img)
#         elif cv2.waitKey(10000) & 0xFF == ord('q'):
#             break
#         cv2.destroyAllWindows()

#     cv2.destroyAllWindows()

# segregate()

pos_len = len(os.listdir(dest_p))
neg_len = len(os.listdir(dest_n))
print(pos_len, neg_len, pos_len + neg_len)

# count = 1
# for i in os.listdir(dest_n):
#     filePath = dest_n + "/" + i
#     img = cv2.imread(filePath)
#     newName = str(count) + ".jpg"
#     cv2.imwrite(dest_n+"/"+newName, img)
#     os.remove(filePath)
#     count += 1

pos_len = len(os.listdir(dest_p))
neg_len = len(os.listdir(dest_n))
print(pos_len, neg_len, pos_len + neg_len)
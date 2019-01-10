# https://blog.gtwang.org/programming/how-to-crop-an-image-in-opencv-using-python/
import cv2

# 讀取圖檔
img = cv2.imread("lena.jpg")

# 裁切區域的 x 與 y 座標（左上角）
x = 100
y = 100

# 裁切區域的長度與寬度
w = 250
h = 150

# 裁切圖片
crop_img = img[y:y+h, x:x+w]

# 顯示圖片
cv2.imshow("cropped", crop_img) # 裁切
cv2.waitKey(0) # waitKey()函数的功能是不断刷新图像，频率时间为delay，单位为ms

# 寫入圖檔
cv2.imwrite('crop.jpg', crop_img)
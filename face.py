import cv2
import matplotlib.pyplot as plt 


image = cv2.imread('a.jpg') #read image
model = cv2.CascadeClassifier('modell.xml') # read xml and adress
face = model.detectMultiScale(image)


x = face[0][0]
y = face[0][1]
a = face[0][2]
b = face[0][3]

image = cv2.rectangle(image, (x,y), (x+a, y+b), (0, 255, 0), 4 )
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
# plt.imshow(image)


print("From xx.png to yy.png? Type in x and y")
x = int(input())
y = int(input())
print("\nimport cv2")
print("import numpy as np")
print("x = 0")
print("y = 44")
print("w = 2880")
print("h = 750\n")

for i in range(x,y+1):
    print("img", end = '')
    print(i, end = '')
    print('= cv2.imread("0', end = '')
    print(i, end = '')
    print('.png")')
    print("crop_image", end = '')
    print(i, end = '')
    print(" = img", end ='')
    print(i, end ='')
    print("[y:y+h, x:x+w]")
print("combine_photo = np.vstack((", end ='')
for k in range(x, y+1):
    print("crop_image", end = '')
    print(k, end='')
    if(k == y):
        print('', end = '')
    else:
        print(", ", end = '') 
print("))")
print("cv2.imwrite('combine_photo.png', combine_photo)", end ='')
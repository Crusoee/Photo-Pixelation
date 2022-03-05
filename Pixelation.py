from PIL import Image

picture_origonal = Image.open("Andrew.jpg")

width, height = picture_origonal.size

pixel_origonal = picture_origonal.load()

print(width, height)


#PIXEL SIZE MUST DIVIDE INTO WIDTH AND HEIGHT OR ELSE AN ERROR OCCURS.
ans = int(input('Enter a pixel size if you would!\n'))
run = True
while run:
    if width % ans == 0:
        if height % ans == 0:
            run = False
    else:
        if ans < height:
            ans += 1
        else:
            run = False
            print('Pixel dimension is bigger than height! Error!')

#I DESIGNATE THE PIXEL SIZE AND THEN FIND ALL THE RGB INFO INSIDE THAT PIXEL SIZE, FIND THE AVERAGE AND THEN SET ALL
#THE PIXELS TO THOSE RGB VALUES
ps = ans
z=[]
for col in range(0, width, ps):
    for row in range(0, height, ps):
        for num1 in range(col,col+ps,1):
            for num2 in range(row,row+ps,1):
                z.append(pixel_origonal[num1,num2])
        
        rv=0
        gv=0
        bv=0
        for i in range(0,ps**2,1):
            rv += z[i][0]
            gv += z[i][1]
            bv += z[i][2]

        r = int(rv / ps**2)
        g = int(gv / ps**2)
        b = int(bv / ps**2)

        for num1 in range(col,col+ps,1):
            for num2 in range(row,row+ps,1):
                pixel_origonal[num1,num2] = (r, g, b)

        z=[]

picture_origonal.show()
picture_origonal.save("Profile Pic.jpg")
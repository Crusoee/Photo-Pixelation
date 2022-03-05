# Photo-Pixelation
Takes any photo and pixelates it! You can set the pixel size!
In order to create a big pixel, made from smaller pixels, you must find the mean RGB values of a group of pixels, then set those same pixels all to those new RGB values,
and so on. A good way to do this, and the way that I achieved this was to use 4 for loops. I used two to set the new pixel demensions, and the other two to find every
single RGB value for each individual pixel inside the new pixel demensions. I then would use the mean formula for each R, G, and B value.

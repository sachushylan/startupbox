from itertools import izip
import Image
import urllib, cStringIO
import Tkinter


#type the url of image in the given format file1 = cStringIO.StringIO(urllib.urlopen("<url>").read())
#root=Tkinter.Tk()
#text =Text(root)
#tex=Text(root)

#print text
file1 = cStringIO.StringIO(urllib.urlopen("http://www.clipartbest.com/cliparts/9i4/oy9/9i4oy9b6T.png").read())
file2 = cStringIO.StringIO(urllib.urlopen("http://images.clipartpanda.com/earth-clipart-Earth-clip-art-8.png").read())
i1 = Image.open(file1)
i2 = Image.open(file2)
print i1.mode == i2.mode, "Different kinds of images."
print i1.size == i2.size, "Different sizes."

 
pairs = izip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:
    # for gray-scale jpegs
    dif = sum(abs(p1-p2) for p1,p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
 
ncomponents = i1.size[0] * i1.size[1] * 3
print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents
#root.mainloop()

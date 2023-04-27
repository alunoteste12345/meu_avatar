from fileinput import filename
import pagan
inpt = 'Python Developer'
img = pagan.Avatar(inpt, pagan.SHA512)
img.show()
outpath = 'output/'
filename = inpt
img.save(outpath, filename)
img.change('new input', pagan.SHA256)
img.change('new input', pagan.SHA224)
img.change('new input', pagan.SHA384)


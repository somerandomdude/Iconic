import os



path = './../../raster/'
original = path+"original/iconic_r0g0b0/"
optimized = path+"optimized/iconic_r0g0b0/"

if not os.path.exists(optimized):
	os.makedirs(optimized)

listing = os.listdir(original)
for infile in listing:
	os.system("./pngcrush -reduce -brute "+original+infile+" "+optimized+infile)
	
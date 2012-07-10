import os


path = './../../vector/'
original = path+"original/"
optimized = path+"optimized/"

if not os.path.exists(optimized):
	os.makedirs(optimized)

listing = os.listdir(original)
for infile in listing:
	os.system("python ./scour-0.26/scour.py -i "+original+infile+" -o "+optimized+infile+" --strip-xml-prolog --enable-comment-stripping --enable-id-stripping --set-precision=2 --shorten-ids --indent=none")
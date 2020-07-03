import os 
i=1
os.chdir("1rot")
print (os.getcwd())
#print (os.listdir())
for files in os.listdir():
    print (files)
    os.rename(files, str(i)+".jpg")
    i = i+1
    print ("-----------------------------")
print (os.listdir())
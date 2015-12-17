text = open("NUData.csv").read()
f = open("myNUData.csv","w")
for i in range(len(text)):
	if "\n" == text[i]:
		if "\r" != text[i-1]:
			continue
	f.write(text[i])
f.close()
#post,SlfRef,NU,MntlHlth,Wish/Want,Request,flame,joke,Gravity,Topic,TabooTopic,Identity,format

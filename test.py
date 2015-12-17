lines = open("StatsForQuestionsWithCodedCommentsGender.csv").readlines()
f = open("StatsForQuestionsWithCodedCommentsGenderRatio.csv","w")
line = lines[0].replace("\n","")+"|maleViableRatio|femaleViableRatio|maleMeanRatio|femaleMeanRatio\n"
f.write(line)
for line in lines[1:]:
	col = line.split("|")
	viableMale, viableFemale = int(col[-4]),int(col[-3])
	meanMale, meanFemale = int(col[-2]),int(col[-1])
	totalMale, totalFemale = int(col[-6]),int(col[-5])

	if totalMale == 0:
		maleMeanRatio = "0"
		maleViableRatio = "0"
	else:

		maleViableRatio = str(viableMale/totalMale)
		maleMeanRatio = str(meanMale/totalMale)

	if totalFemale == 0:
		femaleMeanRatio = "0"
		femaleViableRatio = "0"

	else:
		femaleViableRatio = str(viableFemale/totalFemale)
		femaleMeanRatio = str(meanFemale/totalFemale)

	newLine = line.replace("\n","")+"|"+maleViableRatio+"|"+femaleViableRatio+"|"+maleMeanRatio+"|"+femaleMeanRatio+"\n"
	f.write(newLine)










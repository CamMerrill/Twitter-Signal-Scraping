#fileName = raw_input("Enter file name to clean: ")
fileName = "US100BrandsRaw"
inputFile = open(fileName+".txt", 'r')
outputFile = open("Clean/" + fileName[:-3] + "-clean.txt", 'w')



for line in inputFile:
	atIndex = line.find("@")
	if atIndex != -1:
		#We have a handle
		subLine = line[atIndex:]
		endIndex = subLine.find(")")
		subLine = line[atIndex+1:endIndex+atIndex]
		outputFile.write(subLine + "\n")


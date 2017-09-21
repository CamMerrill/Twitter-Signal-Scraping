fileName = raw_input("Enter file name to clean: ")
inputFile = open(fileName, 'r')
outputFile = open(fileName + "-clean", 'w')


for line in inputFile:
	atIndex = line.find("@")
	if atIndex != -1:
		#We have a handle
		subLine = line[:atIndex]
		print subLine



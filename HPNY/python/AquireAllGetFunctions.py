inputFile = open("allFunctions.txt", 'r')
lines = inputFile.readlines()
inputFile.close()


targetString = "\"get"
outputFile = open("allGetFunctions.txt", "w")
for currentLine in lines:
    if targetString in currentLine:
        outputFile.writelines(currentLine) 

outputFile.close()
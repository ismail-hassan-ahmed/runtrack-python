def readContentFile():
    file = open('output.txt', 'r') 
    print(file.read())
    file.close()

readContentFile()
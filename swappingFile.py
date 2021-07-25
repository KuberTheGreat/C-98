def swapFileData():
    fileName1 = input('Enter name of file 1: ')
    fileName2 = input('Enter name of file 2: ')

    fileData1 = open(fileName1, 'r')
    data_1 = fileData1.read()

    fileData2 = open(fileName2, 'r')
    data_2 = fileData2.read()

    fileData1 = open(fileName1, 'w')
    fileData1.write(data_2)

    fileData2 = open(fileName2, 'w')
    fileData2.write(data_1)

swapFileData()
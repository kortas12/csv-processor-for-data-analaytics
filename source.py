"""
*the source of the data processor program I made all the mathematical functions at this file
*at the first we have the functions that deal with the big databases:
1 avrage
2 mediator
3 mod
4 minor value
5 great value
then we have the work functions:
1 read csv
2 write csv
3 process csv
*the basic program function that made by all the previous functions: process data
*I divided the functions of the work to give the flexibility to the program algorithm
*the program.py is the interface code takes the program algorithm from the source and let it work on interface
*you can use the source with a simple interface as an educational subject for databases processing and csv reading and writing
*all rights received to me© (im just ceding I don't have any real copy rights :) )

"""

# package importing
from csv import reader, writer


#data processing tools
def avrage(*values):  # whole values / number of values
    result = 0

    for i in values:
        result += i
    result = result / len(values)

    if round(result) == result:
        return int(result)
    else:
        return result

def mode(*values):  # most repeated value(avrage of most repeated values)
    preV = {}
    for i in values:
        preV[str(i)] = values.count(i)

    biggest = []
    for i in preV:
        for ii in preV:
            if not ii == i:
                if preV[i] >= preV[ii]:
                    biggest.append(float(i))
                else:
                    break
    if len(biggest) == 1:
        return biggest[0]
    else:
        result = avrage(*biggest)
        if round(result) == result:
            return int(result)
        else:
            return result

def mediator(*values):  # the central value
    result = [0 for _ in values]

    for i in values:
        place = len(values) - 1
        for ii in values:
            if i < ii:
                place -= 1
        result[place] = i

    if len(result) % 2 == 1:
        result = result[(round(len(result) / 2)) - 1]
    else:
        result = ((result[(round(len(result) / 2) - 1)]) + (result[round(len(result) / 2)])) / 2

    if round(result) == result:
        return int(result)
    else:
        return result

def great(*value):  # the biggest value
    for i in value:
        idx = 0
        for ii in value:
            if i < ii:
                break
            idx += 1
            if idx == len(value):
                return i

def minor(*value):  # the smallest value
    for i in value:
        idx = 0
        for ii in value:
            if i > ii:
                break
            idx += 1
            if idx == len(value):
                return i


#program functions
def readCSV(pathfile):  # read the csv and convert it to dictionary
    with open(pathfile, "r") as file:
        result = {}
        read = [i for i in reader(file)]

        for i in range(len(read[0])):
            result[read[0][i]] = [float(read[data][i]) for data in range(1, len(read))]

        for i in result:
            for ii in range(len(result[i])):
                if round(result[i][ii]) == result[i][ii]:
                    result[i][ii] = int(result[i][ii])
        return result


def processCSV(value):  # process the csv data
    for i in value:
        value[i] = (minor(*value[i]), great(*value[i]), avrage(*value[i]), mediator(*value[i]), mode(*value[i]), len(value[i]))
    return value


def writeCSV(pathfile, value):   # write the processed data ate ney file
    with open(pathfile, "w", newline="") as file:
        write = writer(file)
        write.writerow(["", "minor value", "great value", "avrage", "mediator", "mode", "extent"])
        for i in value:
            write.writerow([i, *value[i]])


def processData(A, B):  # the basic function of the program take the path of file and save the result at another
    writeCSV(A, processCSV(readCSV(B)))

import math

def getData(xFile, yFile):
    with open(xFile, "r") as dataset:
        list = dataset.read().strip("null").strip("'").split()
    setTechX = []
    for num in list:
        setTechX.append(num)
    map(float, setTechX)
    with open(yFile, "r") as dataset:
        list = dataset.read().strip("null").strip("'").split()
    setTechY = []
    for num in list:
        setTechY.append(num)
    map(float, setTechY)
    techCoords = {"x": setTechX,
                  "y": setTechY}
    return(techCoords)

def average(numList):
    sum = 0.0
    for num in numList:
        sum = sum + float(num)
    return(sum/(len(numList)))

def generateModel(dataCoords):
    n = float(len(dataCoords.get('x')))
    sumXY = 0.0
    sumX = 0.0
    sumY = 0.0
    sumX2 = 0.0
    for j in range (0, int(n)):
        sumX += float(dataCoords.get("x")[j])

    for k in range (0, int(n)):
        sumY += float(dataCoords.get("y")[k])

    for i in range (0, int(n)):
        sumXY += float(dataCoords.get("x")[i]) * float(dataCoords.get("y")[i])

    for l in range (0, int(n)):
        sumX2 += float(dataCoords.get("x")[l]) ** 2
    a = ((n * sumXY) - (sumX * sumY)) / ((n * sumX2) - sumX**2)
    b = (average(dataCoords.get("y"))) - (a * average(dataCoords.get("x")))
    model = {"a": a,
             "b": b}
    return(model)

def compareModel(modelA, modelB):
    diffA = abs(modelA.get("a") - modelB.get("a"))
    diffB = abs(modelA.get("b") - modelB.get("b"))
    diffPair = {"a": diffA,
                "b": diffB}
    return(diffPair)

def errorAnalysis(modelA, modelB):
    pctError = abs((modelB.get("a") - modelA.get("a"))/modelA.get("a"))
    return(pctError)

def CCErrorAnalysis(ccA, ccB):
    pctError = abs((ccB - ccA)/ccA)
    return(pctError)

def guessIndustry(techModel, enerModel, testModel):
    testToTech = errorAnalysis(techModel, testModel)
    testToEner = errorAnalysis(enerModel, testModel)

    if testToTech < testToEner:
        print("I think this is a TECH company.")
    elif testToTech > testToEner:
        print("I think this is an ENERGY company.")


def correlCoeff(dataCoords):
    n = float(len(dataCoords.get('x')))
    sumXY = 0.0
    sumX = 0.0
    sumY = 0.0
    sumX2 = 0.0
    sumY2 = 0.0
    for j in range(0, int(n)):
        sumX += float(dataCoords.get("x")[j])

    for k in range(0, int(n)):
        sumY += float(dataCoords.get("y")[k])

    for i in range(0, int(n)):
        sumXY += float(dataCoords.get("x")[i]) * float(dataCoords.get("y")[i])

    for l in range(0, int(n)):
        sumX2 += float(dataCoords.get("x")[l]) ** 2

    for m in range(0, int(n)):
        sumY2 += float(dataCoords.get("y")[m]) ** 2

    r = ((n*sumXY) - (sumX*sumY)) / math.sqrt( (n*sumX2 - (sumX)**2)*(n*sumY2)-(sumY)**2 )

    return(r)

def CCGuessIndustry(techCC, enerCC, testCC):
    testToTech = CCErrorAnalysis(techCC, testCC)
    testToEner = CCErrorAnalysis(enerCC, testCC)

    if testToTech < testToEner:
        print("I think this is a TECH company.")
    elif testToTech > testToEner:
        print("I think this is an ENERGY company.")

# print("TECH: ", generateModel(getData("modelTechX.txt", "modelTechY.txt")))
# print("ENER: ", generateModel(getData("modelEnerX.txt", "modelEnerY.txt")))
# # print("UNKW: ", generateModel(getData("testX.txt", "testY.txt")))

guessIndustry( generateModel(getData("modelTechX.txt", "modelTechY.txt")),
                generateModel(getData("modelEnerX.txt", "modelEnerY.txt")),
                generateModel(getData("testX.txt", "testY.txt")) )

CCGuessIndustry(correlCoeff(getData("modelTechX.txt", "modelTechY.txt")), correlCoeff(getData("modelEnerX.txt", "modelEnerY.txt")), correlCoeff(getData("testX.txt", "testY.txt")))
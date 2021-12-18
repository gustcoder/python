def checkIfIsDirtBike(dict):
    text =  dict["isDirtBike"] and " is a dirt bike" or " is not a dirt bike"
    print(dict["model"] + text)

def showItemsFromDict(listOfDict):
    for dict in listOfDict:
        checkIfIsDirtBike(dict)

def showItemsFromDictUsingItems(listOfDict):
    for key, value in listOfDict.items():
        print(key +" rides "+ value)

listOfDict = [
    {"brand": "honda", "model": "crf230", "isDirtBike": True},
    {"brand": "honda", "model": "cg160", "isDirtBike": False},
    {"brand": "yamaha", "model": "ttr230", "isDirtBike": True},
    {"brand": "yamaha", "model": "xt660", "isDirtBike": False},
]
showItemsFromDict(listOfDict)

ridersAndBrands = {"Carmichael": "Suzuki", "Stewart": "Kawasaki", "Reed": "Yamaha"}
showItemsFromDictUsingItems(ridersAndBrands)

def getKeysFromDict(dict):
    return dict.keys()
    
keys = getKeysFromDict(listOfDict[0])
print(keys)

riders = dict(trail='Phil', mx='Carmichael', sx='Stewart')
print(riders)
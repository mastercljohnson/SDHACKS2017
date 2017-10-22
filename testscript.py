a=[{"confidence":0.46,"name":"hair color type","value":"not natural"}]

def checkKeyValuePairExistence(dic, key, value):
        try:
            return dic[key] == value
        except KeyError:
            return False

for dic in a:
    c=checkKeyValuePairExistence(dic, "name", "hair color type")
    print(c)
    print('hahahah')

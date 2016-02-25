
def main():
    
    names = inputNames()
    scores = DonutsChalange()
    output = CountNames(names,scores)
    print(output)

   
def inputNames():
    names = input()
    nameList = []
    names = names.split()
    for name in names:
        nameList.append(name)
    return nameList

def DonutsChalange():
    donutsNames = input()
    donutsChalangeList = []
    words = donutsNames.split()
    for word in words:
        donutsChalangeList.append(word)
    return donutsChalangeList

def CountNames(inputName, donutsList):
    output = []
    for i in range(len(inputName)):
        output.append((inputName[i],donutsList.count(inputName[i])))
        output = sorted(output,key=lambda x: x[1], reverse=True)
    return output

       

if __name__ == "__main__":
    main()
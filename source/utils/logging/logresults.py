def logResults(MainClass,target,handler):
    print("| " + MainClass.name + ":")
    for result in MainClass.out:
        print("|     " + result)
    for result in handler:
        print("| E/W " + result)
def removeDuplicate( li ):
    output=[]

    for x in li:
        if x not in output:

            output.append(x)

    return output
li=[12,24,35,24,88,120,155,88,120,155]

print removeDuplicate(li) [::-1]  #reversed the data

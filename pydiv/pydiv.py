def intconvert(d,x,y):
    numar=[]
    denar=[]
    for i in range(1,x):
        for j in range(1,y):
            q=i/j
            if (str(d) in str(q)) and float(q)-float(d)<1.0:
                numar.append(int(i))
                denar.append(int(j))
    if numar!=None or denar!=None:
        return numar,denar

def convert(d,x,y):
    ar=[]
    for i in range(1,x):
        for j in range(1,y):
            q=i/j
            if (str(d) in str(q)) and float(q)-float(d)<1.0:
                ar.append(str(i)+"/"+str(j))
    try:
        if ar[0]:
            return ar
    except IndexError:
        pass

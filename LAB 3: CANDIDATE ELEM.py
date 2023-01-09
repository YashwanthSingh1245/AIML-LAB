import csv
with open("3.csv") as f:
    csv_file=csv.reader(f)
    data=list(csv_file)
    s=data[0][:-1]
    g=[['?' for i in range(len(s))] for j in range(len(s))]
    for i in data:
        if i[-1]=="true":
            for j in range(len(s)):
                if i[j]!=s[j]:
                    s[j]='?'
                    g[j][j]='?'
        elif i[-1]=="false":
            for j in range(len(s)):
                    if i[j]!=s[j]:
                        g[j][j]=s[j]
                    else:
                        g[j][j]="?"
        print("\nSteps of Candidate Elimination Algorithm: ",data.index(i)+1)
        print(s)
        print(g)
    gh=[]
    for i in g:
        for j in i:
            if j!='?':
                gh.append(i)
                break
    print("\nFinal specific hypothesis: ",s)
    print("\nFinal general hypothesis: ",gh)

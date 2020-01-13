data1 = {"ret":{"A":1, "B":2}, "ret1":{"A":3, "B":4}}
for i in data1 # ret, ret1
    for tmp in i # ret[0]..ret[len(i)]
        print(tmp)
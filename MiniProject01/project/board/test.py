
# MM=['01','02','03','04','05','06','07','08','09']
# for i in range(10, 13, 1):
#     MM.append(str(i))
a = list('0123')
b = list('0123456789')
serial= [i+j for i in a for j in b]
MM = serial[1:13]
DD = serial[1:32]
SS = serial[:24]
print(SS)

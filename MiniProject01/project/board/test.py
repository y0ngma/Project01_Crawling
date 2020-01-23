# GN = ["10대","20대","30대","40대","50대이상"]
# MM = [int(i) for i in range(1,13)]
# DD = [int(i) for i in range(1,32)]
# SS = [int(i) for i in range(0,24)]
# RK = [int(i) for i in range(1,21)]

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


 # html에서 dropdown 메뉴에서 보내줄 get name값 리스트    
        # MM=['01','02','03','04','05','06','07','08','09']
        # for i in range(10, 13, 1):
        #     MM.append(str(i))

        # MM = [int(i) for i in range(1,13)]
        # DD = [int(i) for i in range(1,32)]
        # SS = [int(i) for i in range(0,24)]
        # RK = [int(i) for i in range(1,21)]

        # GN = ["10대","20대","30대","40대","50대이상"]

        # a = list('0123')
        # b = list('0123456789')
        # serial= [i+j for i in a for j in b]
        # MM = serial[1:13]
        # DD = serial[1:32]
        # SS = serial[:24]
        # RK = [str(i) for i in range(1,21)]
    
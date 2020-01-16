# 판다스 데이터전처리 기본 연습
import pandas as pd
# csv 구분자는 "," 또는 "\t"(탭)
df = pd.read_csv('./resources/exam1.csv', delimiter=",")
print(df)

df = df.dropna() #NaN 제거:결측치
print(df)

list1 = df.values.tolist() #df->list
    # print('리스트화=======================','\n', list1)
dict1 = df.to_dict() #df->dict
    # print('딕셔너리화=======================','\n', dict1)
html1 = df.to_html() #df->html
    # print('html화=======================','\n', html1)

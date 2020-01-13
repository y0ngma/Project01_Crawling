import requests
import json

url     = "http://ihongss.com/json/exam4.json"
str1    = requests.get(url).text 
data1   = json.loads(str1)
# data1 -> {ret:[{}, {}, {}, {}], ret1:[{}, {}, {}, {}]}
print(data1)
[{'name': 'AAA', 'species': 'cat', 'foods': {'likes': ['tuna', 'catnip'], 'dislikes': ['ham', 'zucchini']}},
 {'name': 'BBB', 'species': 'dog', 'foods': {'likes': ['bones', 'carrots'], 'dislikes': ['tuna']}},
  {'name': 'CCC', 'species': 'cat', 'foods': {'likes': ['mice'], 'dislikes': ['cookies']}}]

  
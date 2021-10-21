import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
data2 = json.dumps({'name': '郝君豪', '年级': 21,'年龄':17},indent=1,ensure_ascii=False)
print(data2)
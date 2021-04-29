import json

__name__  == "__main__"
    
def some_func(*args,**kwargs):
    result = {}
    list_ = []
    list_4 = []
    kol = 0
    index_ = 0
    for i in args:
        list_4.append(args)
        if kol < 3:
            kol +=1
            continue
        list_.append(list_4)
        list_4 = []
        kol = 0
    print(list_4)
    index_ = 0
    for v in kwargs:
        result[v] = list_4
        index_ +=1

    return result
 
 
def load_dict(some_dict, json_path):
    with open(json_path, 'w') as less13:
        json.dump(result, less13, indent=1)


p_arg =list(range(1,21))       
result = some_func(p_arg, name = "name1", good = "good1", make = "make1", done = "done1", ok = "ok1")
print(result)
load_dict(result, json_path = "/Users/mac/less9/13/less13.json")
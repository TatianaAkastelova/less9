import json

def main():
    pass

def some_func(*args,**kwargs):
    result = {}
    list_ = []
    list4_ = []
    kol = 0
    for i in args:
        list4_.append(i)
        if kol < int(len(args) / len(kwargs)) -1 :
            kol +=1
            continue
        list_.append(list4_)
        list4_ = []
        kol = 0
    print(list_)
    index_ = 0
    for k, v in kwargs.items():
        result[v] = list_[index_]
        index_ +=1
    
    return result

def load_dict(some_dict, json_path):
    with open(json_path, 'r') as less13:
        js_less13 = json.load(less13)
    with open(json_path, 'w') as less13:
        js_target = js_less13["employee"]
        js_target.append(some_dict)
        json.dump(js_less13, less13, indent=4)
        
if __name__  == "__main__":
    main()

    result = some_func(21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
                       name = "name1", good = "good1", make = "make1", done = "done1", ok = "ok1")
dict_result = result
print(dict_result)
    
load_dict(dict_result, json_path = "/Users/mac/less9/13/less13.json")


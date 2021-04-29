from time import time
def main():
    create_list_of_dict(int(input("enter the number:")))

def fun_time_decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time()
        func(*args,**kwargs)
        stop_time = time()
        print(f"фунция выполнилась за {stop_time - start_time} секунд")
    return wrapper

@fun_time_decorator
def create_list_of_dict(n):
    new_list = []
    new_dict = {}
    for val in range(n):
        new_dict[val] = val **2
        new_list.append(dict(new_dict))
    print(new_list)

if __name__ == '__main__':
    main()
    
    
    
    
    
import time

def generate_key_and_value_lists(d):
    """
    Given a dictionary, generates two lists,
    one with the keys and another one with the values
    of the dictionary
    """
    keys=[k for k in d.keys()]
    values=[v for v in d.values()]
    return keys,values

def generate_dictionary(n):
    """
    Generate a dictionary with n key-value pairs
    """
    
    d={i:i for i in range(n)}
    return d 

n=1_000_000
# n=100
# d=generate_dictionary(n)
# keys,values=generate_key_and_value_lists(d)
# target=(n-1)//4
# start=time.time()
# result=target in keys
# stop=time.time()
# print(f"Time to search key in a list of keys (millisecs): {(stop-start)*1.0e+3}")

# start=time.time()
# result=target in d 
# stop=time.time()
# print(f"Time to search key in a dictionary (millisecs): {(stop-start)*1.0e+3}")

n=1_000_000
lst = [i for i in range(n)]
stt = set(lst)
target=(n-1)
start=time.time()
result=target in lst
stop=time.time()
print(f"Time to search key in a list   (millisecs): {(stop-start)*1.0e+3}")

start=time.time()
result=target in stt 
stop=time.time()
print(f"Time to search key in a set (millisecs): {(stop-start)*1.0e+3}")

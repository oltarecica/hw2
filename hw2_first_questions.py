#Answer 1
def triple(x):
    return x * 3

#test
print(triple(7))


#Answer 2
def subtract(a, b):
    return b-a

#test
print(subtract(10,22))


#Answer 3
def dictionary_maker(tuples):
    result={}
    for key, value in tuples:
        result[key]=value
    return result

#test
data = [('foo', 1), ('age', 22), ('bar', 3)]
print(dictionary_maker(data))



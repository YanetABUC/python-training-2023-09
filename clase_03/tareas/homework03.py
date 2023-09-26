def exercise6():
    result = ["a", "aa", "aaa"]
    list2 = ["b", "bb", "bbb"]
    result += list2

    print(result)

def exercise7():
    list = ["abc", "def", "fgh"]

    print(list)
    list[0] += "0"
    list[1] += "1"
    list[2] += "2"
    print(list)  

def exercise8():
    list = ["abc", "def", "fgh"]

    print(list)
    del list[0]
    print(list)

def exercise9():
    items = ["abc", "def", "fgh", ["aab", "bbc", "ccd"]]

    for item in items:
        if type(item) is list:
            for sub_item in item:
                print(sub_item)
        else:
            print(item)


#exercise6()
#exercise7()
#exercise8()
exercise9()
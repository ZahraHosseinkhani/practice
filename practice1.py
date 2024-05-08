def remove_all(lst,value):
    while (value in lst):
        index = lst.index(value)
        lst.pop(index)
        if (index < len(lst)):
            lst.insert(index,None)
        return lst
lst = [200,"zahra",1,5.28,"18",33,"maryam",5,9,28]  
print(remove_all(lst,5))
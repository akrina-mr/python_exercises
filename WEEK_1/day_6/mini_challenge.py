# Create a function that receives a list and returns a new list with no duplicate elements

def remove_duplicates(lists):
    return list(set(lists))

lists = [1,2,2,4,5,5,6]

print(remove_duplicates(lists))
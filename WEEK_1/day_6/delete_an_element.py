# delete b and print the result

letters = {"a","b","c"}

letters.discard("b")
print(letters)


"""
Question:
    What's the difference between discard() and remove() methods in sets?
The main difference between the discard() and remove() methods in sets is how they handle the situation when the element to be removed 
is not present in the set:
- discard(): If you use the discard() method to remove an element that is not present in the set, it will not raise an error. 
  It simply does nothing and leaves the set unchanged.
- remove(): If you use the remove() method to remove an element that is not present in the set, 
  it will raise a KeyError. This means that you need to be sure that the element exists in the set before using remove(),
  or you should handle the potential exception.
In summary, discard() is safer to use when you are not sure if the element exists in the set,
while remove() should be used when you want to ensure that the element is removed and are prepared to handle the case where it might not be present.
"""
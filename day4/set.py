myself= {1,3,"srikanth","teja","prudhvi","nandan","455.645"}
print(myself[0]) # prints 1
print(len(myself)) # prints the length of list i.e., 6
print("Element at index 2 is :",myself[2]) # prints "Element at index 2 is : srikanth"</s>
myself.update()

fs = frozenset(myself)
print("\nFrozen Set:")
print(fs)
# Adding an element to a FrozenSet raises TypeError


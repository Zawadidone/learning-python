# Python3 :)

## Memory management
Names - References -> Objects

### Object
An object stores: type, value, reference count

A variable name is just a label for an object

*Simple*
* numbers
* strings

*Containers*
* dict
* list
* user defined class

### Reference count
a name or a container object that points t

reference count - the number of references

increase reference count

```
x = 300
y = 300
```
PyObject
|type|integer|
|refcount|2|
|value|300|

2 references

`del(x)`
It removes the name to the object and reduces the reference count by 1.

If a object has no references it wil be deleted by the garbage collection


```
def print_word():
  word = 'Seven'
```
if a object is out of scope the reference count goes to 0

local vs global namespace
glob

the reference count never goes to 0 because of global
```
>>> x = 30
>>> y = 30
>>> print(id(x))
1471732352
>>> print(id(y))
1471732352
>>> x is y
True
```

### Garbage collection
A way for a program to automatically release memory when the object taking up that space is no longer in use(reference counting, tracing)

If reference count is 0 -> Objects -> Garbage

Every reference count is stored for every object/assignment

```
Class Node:
  def __init__(self, value):
    self.value = value
  
  def next(self, next):
    self.next = next
    
root = Node('root')
left = Node('left')
right = Node('right')

root.next(left)
left.next(right)
rigt.next(left)

root - 1
left - 3
right - 2

del root
del node1
del node2








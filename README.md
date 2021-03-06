# Python3
Python code -> CPython compiling -> .pyc -> Byte code -> CPython virtual machine -> Machine language -> Processor


## OOP
"__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

## Memory management
Names -> References -> Objects

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

```
x = 300
y = 300
```

|PyObject||
|---|---|
|type|integer|
|refcount|2|
|value|300|

ob_refcnt: reference count

ob_type: pointer to another type


2 references

`del(x)`
It removes the name to the object and reduces the reference count by 1 of object `300`.

If a object has no references it wil be deleted by the garbage collection

```
def print_word():
  word = 'Seven'
  
print_word() #  ref count object 'Seven' is 1 
sleep(5)
```
After the function `print_word()` is done the object 'Seven' is out of scope and the reference count goes to 0 by the garbage collection.

local vs global namespace

the reference count never goes to 0 because of global

`id()` - Returns the address of the object in memory.
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
The addresses of the object `30` and `30` are the same of in memory.

### Garbage collection
A way for a program to automatically release memory when the object taking up that space is no longer in use(reference counting, tracing)

### Reference counting
If reference count is 0 -> Garbage

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
```
Reference count

root - 1

left - 3

right - 2

del root

del node1

del node2

reference count

root - 0

left - 1

right - 1 

### Tracing 
mark and sweep

Follow the references, mark an sweep

python maintains a list of every object created as a program is run

only a container with refcount > 0 will be stored in the list

garbage collection cycle
Python makes a list of objects to discard

It runs an algorithm to detect reference cycles

if an object has no outside references, it's put on the discard list

objects that survive will be promoted to the next generation

reference counting is not thread safe

## Global Interpreter Lock (Gil)
The solution to the problem of dealing with shared resources, like memory in a computer. When two threads try to modify the same resource at the same time, they can step on each other's toes. The end result can be a garbled mess where neither of the threads ends up with what they wanted.

Python’s GIL accomplishes this by locking the entire interpreter, meaning that it’s not possible for another thread to step on the current one. When CPython handles memory, it uses the GIL to ensure that it does so safely.

Python’s GIL accomplishes this by locking the entire interpreter, meaning that it’s not possible for another thread to step on the current one. When CPython handles memory, it uses the GIL to ensure that it does so safely.

Only one thread can run in the interpreter at a time

:) - Fast & simple garbage collection
:( - Only one thread wil be executed at a time

Use multi-processing instead of multi-threading, so each processor wil have it's own Gil

# Byte code

Generate bytecode
python -m py_compile {file}

Dissembler
Python code -> Bytecode/Assembly language
A computer program that translates machine language into assembly language- the inverse operation to tha of an assembler:
* [Dissambler for Python bytecode](https://docs.python.org/3/library/dis.html)
* [Pycdas](https://github.com/zrax/pycdc)

Decompiler
A decompiler takes an executable file as input, and attempts to create a high level source file which can be recompiled successfully.
Python Byte code -> Python code
[Pycdc][https://github.com/zrax/pycdc]

import uncompyle6
`uncompyle6.uncompyle_file('__pycache__/ref.cpython-37.pyc')`


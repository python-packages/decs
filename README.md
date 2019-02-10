# Decs

A handful of useful general-purpose python decorators.

### Installing

$ `pip install decs`

### How to use

Verify functions inputs and outputs types:
```python
from decs import accepts, returns


@returns(str)
@accepts(str)
def my_print(string):
    print(string)
    return string
```

Verify methods inputs and outputs types:
```python
from decs import accepts, returns

class SomeClass:

    @returns(float)
    @accepts('self', int, float)
    def class_method(self, int_arg, float_arg):
        return int_arg + float_arg
```

Repeat test case N times:
```python
from decs import repeat

N = 42

@repeat(N)
def test_something(arg):
    pass
```
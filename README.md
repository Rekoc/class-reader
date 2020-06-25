## Usage

### Basic Usage

After downloading, simply import the ClassReader, instance a ClassReader and send it your class you want to read or debug and call the appropriate function.
**It is working with both Python 2 and 3.**

### Example
```
from classreader import ClassReader

class TestClass:
    arg = 1

class ToRead:
    arg1 = ['ok', 52, "hkgjsdfgjds gj ndjknhrtuk  4553", {1: 12569, 'ok': 'alex'}, [5], 125.3, None]
    arg2 = None
    arg3 = '1'
    arg4 = 458723316
    arg5 = "OKUFHJY HGEZJYFB hjrdbg yjdrhbsj yugbdjs gb"
    arg6 = 6.51
    arg7 = {1526.5: "ok"}
    arg8 = TestClass()
    agr9 = (1, 2 , 3, 5)
    arg10 = test_function
    very_long_variable_name_which_is_anoying = "haha"

    def __init__(self, **kwargs):
        pass

    def func_one(self):
        pass

    def func_two(self):
        pass

    def __str__(self):
        return "ToRead Class"

if __name__ == "__main__":
    to_read = ToRead()
    obj = ClassReader(obj = to_read)
    
    print("get_all_variable_and_value = {}".format(obj.get_all_variable_and_value()))
    print("get_all_variable = {}".format(obj.get_all_variable()))
    print("gavav = {}".format(obj.gavav())) # Same then get_all_variable_and_value()
    print("gav = {}".format(obj.gav())) # Same then get_all_variable()
    
    obj.save_on_file('./test.txt', 'a') # Create a file where the result will be saved
    obj.sof('./test.txt', 'a') # Same then obj.save_on_file() but shorter function's name
    
    print("get_variable_by_type(1) STRING = {}".format(obj.get_variable_by_type(1)))
    print("get_variable_by_type(2) INT/FLOAT = {}".format(obj.get_variable_by_type(2)))
    print("get_variable_by_type(3) CALLABLE = {}".format(obj.get_variable_by_type(3)))
    print("get_variable_by_type(4) LIST = {}".format(obj.get_variable_by_type(4)))
    print("get_variable_by_type(5) DICT = {}".format(obj.get_variable_by_type(5)))
    print("get_variable_by_type(6) OBJ = {}".format(obj.get_variable_by_type(6)))
    print("get_variable_by_type(7) TUPLE = {}".format(obj.get_variable_by_type(7)))
    print("get_variable_by_type(8) CLASS = {}".format(obj.get_variable_by_type(8, TestClass)))
    
    # you can also take a snapshot and compare to another snapshot later on
    obj.catch_snapshot(to_read) # First snapshot
    to_read.arg4 = 99999999999999 # We update a variable
    obj.catch_snapshot(to_read) # second snapshot
    print("make_a_diff = {}".format(obj.make_a_diff())) # Dict who contains diff and variable name
    
    del obj, to_read
```

## Bugs and Issues

Have a bug or an issue with this tool? [Open a new issue](https://github.com/Rekoc/class-reader/issues) here on GitHub.

## Usage

### Basic Usage

After downloading, simply import the ClassReader, instance a ClassReader and send it your class you want to read or debug and call the appropriate function.

### Example
```
from classreader import ClassReader

class ToRead:
    arg1 = ["toRead", "toRead2"]
    arg2 = None
    arg3 = '1'
    arg4 = 458723316
    arg5 = "BLABLA"
    arg6 = 6.51

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
    print(obj.return_variable()) # Return a dict with all the variables in it
    obj.save_on_file('./test.txt', 'a') # Create a file where the result will be saved
    del obj, to_read
```

## Bugs and Issues

Have a bug or an issue with this template? [Open a new issue](https://github.com/Rekoc/class-reader/issues) here on GitHub.

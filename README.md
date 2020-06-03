## Usage

### Basic Usage

After downloading, simply import the ClassReader, instance a ClassReader and send it your class you want to read or debug and call the appropriate function.

### Example

from classreader import ClassReader


class ToRead:
    arg1 = ['ok', 52, "hkgjsdfgjds gj ndjknhrtuk  4553", {1: 12569, 'ok': 'alex'}, [5], 125.3, None]
    arg2 = None
    arg3 = '1'
    arg4 = 458723316
    arg5 = "OKUFHJY HGEZJYFB hjrdbg yjdrhbsj yugbdjs gb"
    arg6 = 6.51

    def __init__(self, **kwargs):
        # print(kwargs)
        pass

    def func_one(self):
        pass

    def func_two(self):
        pass

    def __str__(self):
        return "ToRead Object"


if __name__ == "__main__":
    kwargs = {"arg1": 1, "arg2": 2, "arg3": 3, "arg4": 4}
    to_read = ToRead()
    # print(to_read.__dict__)
    obj = ClassReader(obj = to_read, haha= kwargs)
    print(obj.return_variable())
    obj.save_on_file('./ok.txt', 'a')
    # print(obj.__dict__)
    del obj, to_read

## Bugs and Issues

Have a bug or an issue with this template? [Open a new issue](https://github.com/Rekoc/django-startbootstrap-clean-blog/issues) here on GitHub.

from datetime import datetime


class ClassReaderException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class FileError(ClassReaderException):
    def __init__(self, *args, **kwargs):
        ClassReaderException.__init__(self, "Wrong method or path.")


class ClassReader:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.option = kwargs
        self.__dict__.update(kwargs)
        self.var_list = {}
        self.__extract_all_variable()

    def __extract_all_variable(self):
        for var in dir(self.obj):
            if var[:2] == "__":
                # Private function
                continue
            elif callable(getattr(self.obj, var)):
                # Public function
                continue
            else:
                # We find a variable
                self.var_list.update({"{}".format(var): getattr(self.obj, var)})

    def return_variable(self):
        return self.var_list

    def save_on_file(self, path, method='a'):
        if not method in ['a', 'w', 'r+', 'a+', 'w+'] or len(path) == 0:
            raise FileError
        with open(path, method) as f:
            f.write("________________________________________\n")
            f.write("Class: {}\n".format(self.obj))
            f.write("{}\n".format(datetime.now()))
            for var_name, var in self.var_list.items():
                f.write("\t{}\t\t--->\t{}\n".format(var_name, var))
            f.write("________________________________________\n")

    def __str__(self):
        return "ClassReader"

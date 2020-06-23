from datetime import datetime


class ClassReaderException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class FileError(ClassReaderException):
    def __init__(self, *args, **kwargs):
        ClassReaderException.__init__(self, "Wrong method or path.")


class VarTypeError(ClassReaderException):
    def __init__(self, *args, **kwargs):
        ClassReaderException.__init__(self, "Wrong variable type.")


class ClassReader:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.option = kwargs
        self.__dict__.update(kwargs)
        self.var_dict = {}
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
                self.var_dict.update({"{}".format(var): getattr(self.obj, var)})

    def __get_str_variable(self):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if isinstance(var, str) or isinstance(var, basestring):
                ret_list.append({var_name: var})
        return ret_list

    def __get_int_variable(self):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if isinstance(var, int) or isinstance(var, float) \
                or isinstance(var, long) or isinstance(var, complex):
                ret_list.append({var_name: var})
        return ret_list

    def __get_callable_variable(self):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if callable(var):
                ret_list.append({var_name: var})
        return ret_list

    def __get_list_variable(self):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if isinstance(var, list):
                ret_list.append({var_name: var})
        return ret_list

    def __get_dict_variable(self):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if isinstance(var, dict):
                ret_list.append({var_name: var})
        return ret_list

    def __get_obj_variable(self):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if isinstance(var, object):
                ret_list.append({var_name: var})
        return ret_list

    def __get_tuple_variable(self):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if isinstance(var, tuple):
                ret_list.append({var_name: var})
        return ret_list

    def __get_class_variable(self, obj):
        ret_list = []
        for var_name, var in self.var_dict.items():
            if isinstance(var, obj):
                ret_list.append({var_name: var})
        return ret_list

    def get_all_variable(self):
        """
            Return ONLY variables name sorted.
        """
        return sorted(self.var_dict, key=lambda x:x.lower())

    def get_all_variable_and_value(self):
        """
            Return variables and values name non-sorted.
        """
        return self.var_dict

    def get_variable_by_type(self, var_type, obj=None):
        """
            obj: class you want to look for
            var_type: integer
                1 --> string
                2 --> integer, float, complex, long
                3 --> callable (dict, class, function, list)
                4 --> list
                5 --> dictionnary
                6 --> object (list, dict, None, class, ...)
                7 --> tuple
                8 --> class (you need to provide a class in the 'obj' parameter)
        """
        if var_type == 1:
            return self.__get_str_variable()
        elif var_type == 2:
            return self.__get_int_variable()
        elif var_type == 3:
            return self.__get_callable_variable()
        elif var_type == 4:
            return self.__get_list_variable()
        elif var_type == 5:
            return self.__get_dict_variable()
        elif var_type == 6:
            return self.__get_obj_variable()
        elif var_type == 7:
            return self.__get_tuple_variable()
        elif var_type == 8:
            return self.__get_class_variable(obj)
        else:
            raise VarTypeError


    def save_on_file(self, path, method='a', padding_truncate=22):
        """
            path: string who contains the path of your file
            method: character method to create your log file
            padding_truncate: integer, number of character to truncate your variable name
                but also the padding of your variables name, by default 22
        """
        if not method in ['a', 'w', 'r+', 'a+', 'w+'] or len(path) == 0:
            raise FileError
        with open(path, method) as f:
            f.write("________________________________________\n")
            f.write("Class: {}\n".format(self.obj))
            f.write("{}\n".format(datetime.now()))
            for var_name, var in sorted(self.var_dict.items()):
                f.write("\t{:.<{}.{}} --->\t{}\n".format(var_name, padding_truncate, padding_truncate, var))
            f.write("________________________________________\n")

    def __str__(self):
        return "ClassReader"

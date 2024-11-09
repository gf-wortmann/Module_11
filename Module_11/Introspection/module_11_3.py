# Домашнее задание по теме "Интроспекция"
# Цель задания:
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.


import inspect


class TestClass:
    def __init__(self):
        self.text_attr = 'text'
        self.float_attr = 122.2
        self.list_attr = ['list', 'attr']
    
    @staticmethod
    def quadratic(float_number: float):
        return float_number ** 2
    
    def set_text_attr(self, text):
        self.text_attr = text
    
    def append_attr(self):
        setattr(self, 'quad_attr', self.quadratic(self.float_attr))


def introspection_info(obj):
    result = {'type': type(obj).__name__}
    attributes = []
    methods = []
    for attr_name in dir(obj):
        if not callable(getattr(obj, attr_name)):
            attributes.append(attr_name)
        if callable(getattr(obj, attr_name)):
            methods.append(attr_name)
    result['attributes'] = attributes
    result['methods'] = methods
    result['module'] = inspect.getmodule(obj)
    
    return result


t = TestClass()


# check up the task

print(introspection_info(42))
print(introspection_info(22.2))
print(introspection_info(t))

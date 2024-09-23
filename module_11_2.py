from pprint import pprint
import inspect


class Product:
    def __init__(self, name, weight, category):
        self.name: str = name
        self.weight: float = weight
        self.category: str = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def show(self):
        print(self.name)


def introspection_info(obj):
    info_obj = {'type': type(obj),
                'attributes': dir(obj),
                'methods': [attr for attr in dir(obj) if inspect.ismethod(obj.__getattribute__(attr))],
                'module': inspect.getmodule(obj)
                }
    return info_obj


test = Product('Яблоко', '2', 'Фрукт')
pprint(introspection_info(test))

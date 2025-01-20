import inspect

class Food():
    def __init__(self):
        self.all_vegetables = []

    def add_vegetables(self, vegetable: str):
        self.all_vegetables.append(vegetable)
        return self.all_vegetables


test_1 = Food()
print(dir(test_1))
print(test_1.add_vegetables("zukini"))

def introspection_info(obj):
    final_info = {}
    final_info['type'] = type(obj).__name__
    final_info['attr'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    final_info['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    final_info['module'] = inspect.getmodule(obj).__name__
    return final_info

number_info = introspection_info(test_1)
print(number_info)


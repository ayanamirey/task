# chain_sum(5)()  # 5
# chain_sum(5)(2)()  # 7
# chain_sum(5)(100)(-10)()  # 95

# Готово
def chain_sum1(number):
    def wrapper(number2=None):
        if number2 is None:
            return wrapper.result
        wrapper.result += number2
        return wrapper

    wrapper.result = number
    return wrapper


# Сделать без if
def chain_sum2(number):
    def wrapper(number2=None):
        try:
            number2 = int(number2)
        except TypeError:
            return wrapper.result
        wrapper.result += number2
        return wrapper

    wrapper.result = number
    return wrapper


# Сделать без if и без try except
def chain_sum(number):
    def wrapper(number2=None):
        def inner():
            wrapper.result += number2
            return wrapper

        logic = {
            type(None): lambda: wrapper.result,
            int: inner,
        }
        return logic[type(number2)]()
        wrapper.result += number2
        return wrapper

    wrapper.result = number
    return wrapper


print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())


# chain_sum_v2 без последних скобок
# chain_sum_v2(5)  # 5
# chain_sum_v2(5)(2)  # 7
# chain_sum_v2(5)(100)(-10)  # 95

class Chain_sum:
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return Chain_sum(self._number + value)

    def __str__(self):
        return f'{self._number}'


class Chain_sum(int):
    def __call__(self, addition=0):
        return Chain_sum(self + addition)


print(1 + Chain_sum(5))
print(1 + Chain_sum(5)(2))
print(1 + Chain_sum(5)(100)(-10))

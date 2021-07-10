from configuration import *
import random
import string


def rand_gen():
    alphabet_string = string.ascii_uppercase
    name = ''
    for i in range(5):
        name = name + random.choice(alphabet_string + str(random.randint(0, 100)))
    return name


class Product:
    def __init__(self):
        self.features = {'Бренд': str(random.choice(BRANDS)).capitalize(),
                         'Имя': f'{str(random.choice(NAMES)).capitalize()}' + '-' + f'{rand_gen()}',
                         'Категория': str(random.choice(CATEGORIES)).capitalize(),
                         'Цена': random.randint(5000, 100000)}
        for feature in FEATURES:
            self.features[feature] = random.choice(FEATURES_DICT[feature])


import pandas as pd

from configuration import *
import random
import string
import shutil

used_slugs = []


def rand_gen(len_to_gen):
    alphabet_string = string.ascii_uppercase
    name = ''
    global used_slugs
    for i in range(len_to_gen):
        name = name + random.choice(alphabet_string + str(random.randint(0, 100)))
    if name not in used_slugs:
        used_slugs.append(name)
        return name
    else:
        rand_gen(len_to_gen)


class Product:
    def __init__(self):
        self.slug = str(f'{rand_gen(15)}').lower()
        # shutil.copy(random.choice(PHOTOS), f'output/{self.slug}.jpg')
        self.features = {'Категория': str(random.choice(CATEGORIES)).capitalize(),
                         'Имя': f'{str(random.choice(NAMES)).capitalize()}' + '-' + f'{rand_gen(4)}',
                         'Slug': f'{self.slug}',
                         'Image': f'{self.slug}.jpg',
                         'Описание': DESCRIPTION,
                         'Цена': random.randint(5000, 100000)//100*100,
                         'Бренд': str(random.choice(BRANDS)).capitalize(),
                         }
        for feature in FEATURES:
            self.features[feature] = random.choice(FEATURES_DICT[feature])


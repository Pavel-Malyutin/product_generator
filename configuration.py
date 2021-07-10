FEATURES = ('Память', 'Экран', 'Стандарт связи', 'АКБ', 'Камера', 'Корпус', )

CATEGORIES = ('Смартфон',)

with open('input/brands.txt') as f:
    BRANDS = f.read().splitlines()

with open('input/names.txt') as f:
    NAMES = f.read().splitlines()

FEATURES_DICT = {}
FILE_NUM = 1
for v in FEATURES:
    with open(f'input/feature_{FILE_NUM}.txt', encoding='UTF-8') as file:
        FEATURES_DICT[v] = file.read().splitlines()
    FILE_NUM += 1

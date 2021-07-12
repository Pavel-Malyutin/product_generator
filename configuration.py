import glob

ITEMS_TO_GEN = 100000000

# FEATURES = ('Диагональ экрана', 'CPU', 'RAM', 'SSD', 'Видеокарта',)     # ноутбуки
FEATURES = ('Диагональ экрана', 'Стандарт связи', 'АКБ', 'Камера', 'Корпус', )     # смартфоны

CATEGORIES = ('Смартфон',)

DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce condimentum, sem quis bibendum finibus, ' \
              'risus lorem varius turpis, at ultrices dolor orci ac nibh. Donec sit amet sapien risus. Vivamus ' \
              'interdum tortor eu eros fringilla sollicitudin at at eros. Maecenas aliquet placerat purus, ' \
              'nec ornare felis dictum eu. Mauris non scelerisque nisl. Cras id ullamcorper augue. Nulla justo nibh, ' \
              'suscipit ultricies erat sit amet, interdum ultrices mauris. Suspendisse potenti. '

with open('input_smartphones/brands.txt') as f:
    BRANDS = f.read().splitlines()

with open('input_smartphones/names.txt') as f:
    NAMES = f.read().splitlines()

FEATURES_DICT = {}
FILE_NUM = 1
for v in FEATURES:
    with open(f'input_smartphones/feature_{FILE_NUM}.txt', encoding='UTF-8') as file:
        FEATURES_DICT[v] = file.read().splitlines()
    FILE_NUM += 1

PHOTOS = glob.glob("input_smartphones/images/*.jpg")
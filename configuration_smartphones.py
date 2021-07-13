import glob

FEATURES = ('Диагональ экрана', 'Стандарт связи', 'АКБ', 'Камера', 'Корпус', )

CATEGORY = 2

DESCRIPTION = 'Современный смартфон со свежим и интересным дизайном и достаточной для любых задач мощностью. Девайс ' \
              'оснащен великолепным экраном и отличной камерой. Этот компактный гаджет очень удобен в использовании. ' \
              'Накопитель большой емкости — еще один плюс модели. Сканер отпечатков на задней крышке молниеносно ' \
              'разблокирует телефон. Селфи-камера красиво размывает фон на портретах. Эффект боке доступен и для ' \
              'ранее сделанных фотографий. Это удачное предложение в данном ценовом классе.'

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

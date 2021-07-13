import glob

COLUMNS = ['id', 'title', 'slug', 'image', 'description', 'price', 'brand', 'diagonal', 'cpu', 'ram', 'ssd', 'video',
           'category_id']

FEATURES = ('Диагональ экрана', 'CPU', 'RAM', 'SSD', 'Видеокарта',)

CATEGORY = 1

DESCRIPTION = 'Смотрите фильмы, общайтесь по видеосвязи и редактируйте документы на отличном экране с высоким ' \
              'разрешением. Он показывает яркую, чёткую и детализированную картинку. Подключайте всё, ' \
              'что вам понадобится, от флешки до внешнего монитора и от портативного жёсткого диска до принтера. Для ' \
              'этого на корпусе есть выход HDMI и порты USB – один из них соответствует стандарту Type C и ' \
              'обеспечивает особенно простое подсоединение совместимых устройств и передачу данных с минимальными ' \
              'затратами времени.'

with open('input_notebooks/brands.txt') as f:
    BRANDS = f.read().splitlines()

with open('input_notebooks/names.txt') as f:
    NAMES = f.read().splitlines()

FEATURES_DICT = {}
FILE_NUM = 1
for v in FEATURES:
    with open(f'input_notebooks/feature_{FILE_NUM}.txt', encoding='UTF-8') as file:
        FEATURES_DICT[v] = file.read().splitlines()
    FILE_NUM += 1

PHOTOS = glob.glob("input_notebooks/images/*.jpg")

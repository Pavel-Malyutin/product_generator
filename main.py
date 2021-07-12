import pandas as pd

from generator import Product
from configuration import ITEMS_TO_GEN

if __name__ == '__main__':
    counter = 0
    items = pd.DataFrame()
    while counter < ITEMS_TO_GEN:
        p = Product()
        items = items.append(pd.DataFrame(p.features.values(), index=p.features.keys()))
        # print(p.features)
        counter += 1

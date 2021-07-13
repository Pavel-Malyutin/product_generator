import pandas as pd

from generator import Product

ITEMS_TO_GEN = 10001

if __name__ == '__main__':
    counter = 0
    items = pd.DataFrame()
    while counter < ITEMS_TO_GEN:
        p = Product()
        features_list = []
        for i in p.features.values():
            features_list.append(i)
        items = items.append(pd.Series(features_list), ignore_index=True)
        counter += 1
    items.to_csv('out.csv')

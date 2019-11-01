# let's use these classes and write an acme_report.py module to generate random products
# and print a summary of them. For the purposes of these functions we will
# only use the Product class.

# Your module should include two functions:

# generate_products() should generate a given number of products (default 30), randomly, and return them as a list
# inventory_report() takes a list of products, and prints a "nice" summary
# For the purposes of generation, "random" means uniform - all possible
# values should vary uniformly

# You should implement only depending on random from the standard library, your Product class from
# acme.py, and built-in Python functionality.
from random import randint, sample, uniform
import numpy as np
import pandas as pd

ADJ = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUN = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    rand_products = []

    for i in range(num_products):
        random_adj_num = (np.random.randint(0, len(ADJ)))
        random_noun_num = (np.random.randint(0, len(NOUN)))
        ran_price = (np.random.randint(5, 100))
        ran_weight = (np.random.randint(5, 100))
        ran_flam = (np.random.randint(0.0, 2.5))
        random_adj = ADJ[random_adj_num]
        random_noun = NOUN[random_noun_num]
        rand_products.append([str(random_adj) + ' ' + str(random_noun),
                              int(ran_price), int(ran_weight), int(ran_flam)])
    return rand_products


print(generate_products(2))


def inventory_report(generate_products):
    df = pd.DataFrame(
        data=generate_products,
        columns=[
            'products',
            'price',
            'weight',
            'flam'])
    unique_prod = df.products.nunique()
    price_avg = df.price.mean()
    weight_avg = df.weight.mean()
    flam_avg = df.flam.mean()
    return (f'total unique products: {unique_prod}, price average: {price_avg}, \n\
    weight average {weight_avg}, flammability average: {flam_avg}')

# if __name__ == '__main__':
#     print(inventory_report(generate_products()))

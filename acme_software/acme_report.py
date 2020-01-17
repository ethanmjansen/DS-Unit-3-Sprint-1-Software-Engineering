#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    name = Product()
    price = 
    weight = 
    return products


def inventory_report(products):
    unique = 
    avgprice = mean(products.price)
    avgweight = mean(products.weight)
    avgflammability = mean(products.flammability)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names' + unique)
    print('Average price' + avgprice)
    print('Average weight' + avgweight)
    print('Average flammability' + avgflammability)
    

if __name__ == '__main__':
    inventory_report(generate_products())
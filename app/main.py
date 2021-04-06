# This is a sample Python script.
from itertools import chain

import boto3

from utils import (
    get_s3_file, get_json_file, sorted_array, write_json_file,
    print_elements, get_products, profundidad, frequency_product
)
from variables import (
    CATEGORIAS, PRODUCTOS, ORDEN,
    NINETYNINE, SUBPRODUCTOS, ID, NOMBRE
)

s3 = boto3.client('s3')


def generate_json_ordered():
    homeria_sorted = {
        CATEGORIAS: sorted_array(categories, ORDEN, default=NINETYNINE),
        PRODUCTOS: sorted_array(products, ORDEN, default=NINETYNINE)
    }
    write_json_file('datos/homeria_sorted.json', homeria_sorted)
    write_json_file(
        'datos/homeria_categories_sorted.json',
        sorted_array(categories, 'nombre', default='')
    )


def print_subproducts():
    subprod_categories = list(chain.from_iterable(
        [subprod[PRODUCTOS] for subprod in categories if
         subprod[PRODUCTOS]])
    )
    list_subproducts = list(
        filter(lambda x: True if x[SUBPRODUCTOS] else False, products)
    )
    subprod_products = list(
        chain.from_iterable(
            list(map(lambda x: x[SUBPRODUCTOS], list_subproducts))
        )
    )

    subproducts = [product for product in homeria[PRODUCTOS]
                   if product[ID] not in subprod_categories and product[
                       ID] in subprod_products]
    print('\nSubproductos')
    print('------------')
    print_elements(subproducts)


def print_products_and_subproducts_for_menu():
    products_menu = list(
        chain.from_iterable(
            [category[PRODUCTOS] for category in
             categories if category[NOMBRE] == 'Menús']
        )
    )
    products_menu = sorted_array(
        get_products(products, products_menu), ORDEN, default=NINETYNINE
    )
    print("\nProductos y Subproductos de la categoria Menús")
    print("------------------------------------------------")
    print_elements(products_menu)


def write_json_frequency_products():
    result = list()
    for prod in products:
        total = 0
        total = frequency_product(categories, prod[ID], key=PRODUCTOS)
        total += frequency_product(products, prod[ID], key=SUBPRODUCTOS)
        result.append({prod['name']: total})
    write_json_file('datos/frecuencia_productos.json', result)


if __name__ == '__main__':
    get_s3_file(s3)
    homeria = get_json_file('datos/homeria.json')
    categories = homeria[CATEGORIAS]
    products = homeria[PRODUCTOS]
    generate_json_ordered()
    print_subproducts()
    print_products_and_subproducts_for_menu()
    print(f'\nLa Profundidad del json es: {profundidad(homeria)}')
    write_json_frequency_products()

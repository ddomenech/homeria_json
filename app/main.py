# This is a sample Python script.
import json
from itertools import chain

import boto3

NINETYNINE = 99

FILENAME = 'homeria'
BUCKET = 'homeria-coding-interview'

s3 = boto3.client('s3')


def get_s3_file():
    # get s3 information json file
    result = None
    for key in s3.list_objects_v2(Bucket=BUCKET, Prefix=FILENAME)['Contents']:
        print((key['Key']))
        if key['Key'][:7] == FILENAME:
            result = key['Key']
            break
    return result


def get_products(list_products, ids=[]):
    result = []
    for prod in list_products:
        if prod['id'] in ids:
            result.append(prod)
            if prod['subproductos']:
                result += get_products(list_products, prod['subproductos'])
    return result


def get_json_file(filename):
    return json.load(open(filename, encoding='utf-8'))


def write_json_file(file: str, data):
    with open(file, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False)


def frequency_product(elements, id, key=''):
    result = [element for element in elements if
              element[key] and id in element[key]]
    return len(result)


if __name__ == '__main__':
    object_name = get_s3_file()
    s3.download_file(BUCKET, object_name, 'homeria.json')
    homeria = get_json_file('homeria.json')
    categoris = homeria['categorias']
    products = homeria['productos']
    homeria_sorted = {
        'categorias': sorted(
            categoris,
            key=lambda data: data.get('orden', NINETYNINE)),
        'productos': sorted(
            products,
            key=lambda object: object.get('orden', NINETYNINE)
        )
    }
    write_json_file('homeria_sorted.json', homeria_sorted)

    categories_name = sorted(
        categoris,
        key=lambda object: object.get('nombre', '')
    )
    write_json_file('homeria_categories_sorted.json', categories_name)

    subprod_categories = list(chain.from_iterable(
        [subprod['productos'] for subprod in categoris if
         subprod['productos']])
    )
    mylist = [subprod['subproductos'] for subprod in homeria['productos'] if
              subprod['subproductos']]
    subprod_products = list(chain.from_iterable(mylist))

    subproducts = [product for product in homeria['productos']
                   if product['id'] not in subprod_categories and product[
                       'id'] in subprod_products]
    print('\nSubproductos:')
    for product in subproducts:
        print(f"Nombre: {product['name']}, id: {product['id']}")

    mylist = [category['productos'] for category in
              homeria['categorias'] if category['nombre'] == 'Menús']
    products_menu = list(chain.from_iterable(mylist))
    products_menu = sorted(get_products(homeria['productos'], products_menu),
                      key=lambda data: data.get('orden', NINETYNINE))
    print("\nProductos y Subproductos de la categoria Menús")
    for prod in products_menu:
        print(f"Nombre: {prod['name']}, id: {prod['id']}")
        result = list()
    for prod in products:
        total = 0
        total = frequency_product(categoris, prod['id'], key='productos')
        total += frequency_product(products, prod['id'], key='subproductos')
        result.append({prod['name']: total})
    print(result)
    write_json_file('frecuencia_productos.json', result)

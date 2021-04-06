import json

from variables import FILENAME, BUCKET, SUBPRODUCTOS, ID


def get_s3_file(s3):
    result = None
    for key in s3.list_objects_v2(Bucket=BUCKET, Prefix=FILENAME)['Contents']:
        if key['Key'][:7] == FILENAME:
            result = key['Key']
            break
    return s3.download_file(BUCKET, result, 'datos/homeria.json')


def get_products(list_products, ids=[]):
    result = []
    for prod in list_products:
        if prod[ID] in ids:
            result.append(prod)
            if prod[SUBPRODUCTOS]:
                result += get_products(list_products, prod[SUBPRODUCTOS])
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


def sorted_array(array, key, default=None):
    return sorted(array, key=lambda data: data.get(key, default))


def print_elements(elements):
    def prin_element(element):
        print(f"Nombre: {element['name']}, id: {element['id']}")

    list(map(prin_element, elements))


def profundidad(json):
    result = 0
    if isinstance(json, dict):
        result += 1 + (max(map(profundidad, json.values()) if json else 0))
    if isinstance(json, list):
        result += 1 + (max(map(profundidad, json) if json else 0))
    return result

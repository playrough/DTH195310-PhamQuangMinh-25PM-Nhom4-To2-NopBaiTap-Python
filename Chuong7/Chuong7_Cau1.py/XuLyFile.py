def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(data + "\n")

def DocFile(path):
    arrProduct = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()
            arr = data.split(';')
            arrProduct.append(arr)
    return arrProduct

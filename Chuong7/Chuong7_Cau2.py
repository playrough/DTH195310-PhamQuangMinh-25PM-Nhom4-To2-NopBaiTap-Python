def DocFile(path):
    arrSo = []
    with open(path,'r',encoding='utf-8') as file:
        for line in file:
            arr = [int(x) for x in line.strip().split(',')]
            arrSo.append(arr)
    return arrSo

def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:
        for number in row:
            if number < 0:
                print(number, end='\t')
        print()

arrSo = DocFile("csdl_so.txt")
print("Các số âm trên mỗi dòng:")
XuatSoAmTrenMoiDong(arrSo)

from XuLyFile import *

dssp = DocFile("database.txt")

def XuatSanPham(dssp):
    for row in dssp:
        print('\t'.join(row))

def SortSp(dssp):
    dssp.sort(key=lambda x: float(x[2]), reverse=True)

print("Danh sách sản phẩm:")
XuatSanPham(dssp)
SortSp(dssp)
print("\nSản phẩm sau khi sắp xếp giá giảm dần:")
XuatSanPham(dssp)

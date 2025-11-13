from openpyxl import load_workbook # type: ignore
wb = load_workbook('demo.xlsx')
ws = wb.active
for row in ws.values:
    print(*row, sep="\t")

from openpyxl import *

wb = load_workbook(filename="modelList.xlsx")
sheet = wb.active


def getModelsList():
    models = []
    for i in range(1,sheet.max_row+1):
        col = "A"+str(i)
        models.append(sheet[col].value)
    return models






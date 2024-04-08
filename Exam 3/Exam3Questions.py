# Random question generator

import random
from openpyxl import load_workbook

num = random.randint(2, 36)

ch = f'A{num}'
cell = f'C{num}'


wb = load_workbook(r"Exam 3\Questions.xlsx", data_only=True)
sh = wb["Questions"]

print(f'\n{sh[ch].value}: {sh[cell].value}\n')


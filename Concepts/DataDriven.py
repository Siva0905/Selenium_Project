import openpyxl

import os


def create_excel_data():
    """Create Excel test data for name field"""

    os.makedirs("test_data", exist_ok=True)

    workbook = openpyxl.Workbook()

    sheet = workbook.active

    sheet.title = "NameTests"

    # Headers

    sheet['A1'] = 'TestCaseID'

    sheet['B1'] = 'Name'

    sheet['C1'] = 'ExpectedResult'

    # Test data

    test_data = [

        ('TC001', 'John Doe', 'Valid'),

        ('TC002', '', 'Invalid'),

        ('TC003', 'Jane Smith', 'Valid'),

        ('TC004', 'Test123', 'Invalid')

    ]

    for i, data in enumerate(test_data, start=2):
        sheet[f'A{i}'] = data[0]

        sheet[f'B{i}'] = data[1]

        sheet[f'C{i}'] = data[2]

    workbook.save('test_data/excel_data.xlsx')

    print("Excel test data created: test_data/excel_data.xlsx")


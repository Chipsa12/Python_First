import xlsxwriter
from db.DB import DB

db = DB()
tests = db.getAllTestResults()

workbook = xlsxwriter.Workbook('example.xlsx')  # создаем документ
worksheet = workbook.add_worksheet()  # создаем вкладку в документе
# форматирование
cellPass = workbook.add_format(dict(font_color='green'))
failPass = workbook.add_format(dict(font_color='red', bold=True))
# названия столбцов
worksheet.write('A1', '№')
worksheet.write('B1', 'Название теста')
worksheet.write('C1', 'Успех')
worksheet.write('D1', 'Фиаско')
worksheet.write('E1', 'Дата')
# значения
for i, test in enumerate(tests):
    worksheet.write('A' + str(i + 2), i+1)
    worksheet.write('B' + str(i + 2), test['name'])
    if test['result']:
        worksheet.write('C' + str(i + 2), 1, cellPass)
    else:
        worksheet.write('D' + str(i + 2), 1, failPass)
    #worksheet.write('E' + str(i + 2), test['date_time'])
# подсчет сумм
worksheet.write('F1', 'Успешные')
worksheet.write('G1', 'Неуспешные')
worksheet.write('F2', '=SUM(C:C)')
worksheet.write('G2', '=SUM(D:D)')
# рисуем графики
chart = workbook.add_chart(dict(type='column'))
chart.add_series(dict(values='=Sheet1!$F2'))
chart.add_series(dict(values='=Sheet1!$G2'))
worksheet.insert_chart('H7', chart)
# записать данные
workbook.close()

'''

'''
import jinja2
import os
import pdfkit


def report_1(Period:str, list_data, temp='./temp'):
    '''Состовляем первый отчет'''

    templateLoader = jinja2.FileSystemLoader(searchpath="/home/dima/PycharmProjects/telegramBot_thermobox/moduls/report/templase")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "index.html"
    template = templateEnv.get_template(TEMPLATE_FILE)


    outputText = template.render(data=Period, info=list_data)

    html_file = open(os.path.join(temp, 'report_1.html'), 'w')
    html_file.write(outputText)
    html_file.close()
    pdfkit.from_file(os.path.join(temp, 'report_1.html'), os.path.join(temp, 'report_1.pdf'))
    return os.path.join(temp, 'report_1.pdf')


if __name__ == '__main__':
    Period = '01/12/2020-08/12/2020'
    data = [['01-12-2020', 'Shumelev Dmitry Igorevith', '36.6', '37.8', 'Проходит', '/home/dima/Изображения/Nnec5EGL3oo.jpg'],
            ['01-12-2020', 'Шумелев дмири чсывсыу', '36.6', '37.8', 'Подазрительный', '/home/dima/Изображения/Nnec5EGL3oo.jpg'],
            ['01-12-2020', 'Shumelev ывсыв Igorevith', '36.6', '37.8', 'Проходит', 'image']]

    #report_1(Period, data)

    from moduls.dataBase import DATA_BASE_TELEGRAM_BOT
    test = DATA_BASE_TELEGRAM_BOT('/home/dima/PycharmProjects/telegramBot_thermobox/rc/database.bd')
    period, data_db = test.get_data_for_report_1()
    report_1(period, data_db, '/home/dima/PycharmProjects/telegramBot_thermobox/moduls/report/temp')
    #pdfkit.from_file(r'/home/dima/PycharmProjects/telegramBot_thermobox/moduls/report/temp/report_1.html', '/home/dima/PycharmProjects/telegramBot_thermobox/moduls/report/temp/out.pdf')
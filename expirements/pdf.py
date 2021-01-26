# simple_table.py

from fpdf import FPDF


def simple_table(data, spacing=1):
    '''

    :param info: [['01-12-2020', 'Shumelev Dmitry Igorevith', '36.6', '37.8', image]]
    :param spacing:
    :return:
    '''


    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()

    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height * spacing,
                     txt=item, border=1)
        pdf.ln(row_height * spacing)

    pdf.output('simple_table.pdf')


if __name__ == '__main__':
    info = [['Дата', 'ФИО', 'Тепловизор', 'Пирометр', 'Фото'],
            ['01-12-2020', 'Shumelev Dmitry Igorevith', '36.6', '37.8', 'image'],
            ['01-12-2020', 'Шумелев дмири чсывсыу', '36.6', '37.8', 'image'],
            ['01-12-2020', 'Shumelev ывсыв Igorevith', '36.6', '37.8', 'image']]

    info = [['First Name', 'Шумелев Name', 'email', 'zip'],
            ['Mike', 'Driscoll', 'mike@somewhere.com', '55555'],
            ['John', 'Doe', 'jdoe@doe.com', '12345'],
            ['Nina', 'Ma', 'inane@where.com', '54321']
            ]
    simple_table(info)
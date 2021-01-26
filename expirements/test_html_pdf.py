
data1 = '01/12/2020-08/12/2020'
data = [['01-12-2020', 'Shumelev Dmitry Igorevith', '36.6', '37.8', 'image'],
        ['01-12-2020', 'Шумелев дмири чсывсыу', '36.6', '37.8', 'image'],
        ['01-12-2020', 'Shumelev ывсыв Igorevith', '36.6', '37.8', 'image']]

import jinja2
from xhtml2pdf import pisa


def convertHtmlToPdf(sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")
    pisaStatus = pisa.CreatePDF(sourceHtml, dest=resultFile, encoding='UTF-8', show_error_as_pdf=True)
    resultFile.close()
    return pisaStatus.err


templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "index.html"
template = templateEnv.get_template(TEMPLATE_FILE)


outputText = template.render(data=data1, info=data)

html_file = open('test.html', 'w')
html_file.write(outputText)
html_file.close()

# pdf = pisa.CreatePDF(StringIO.StringIO(outputText.encode("UTF-8")), result, encoding='UTF-8', show_error_as_pdf=True)
convertHtmlToPdf(outputText, 'tesst.pdf')


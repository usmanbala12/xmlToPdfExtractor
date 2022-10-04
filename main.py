import xmltodict
from fpdf import FPDF, HTMLMixin
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape()
)

class MyFPDF(FPDF, HTMLMixin):
    pass

with open('FN2XML_20151202_100247_031.xml') as fd:
    doc = xmltodict.parse(fd.read())

for i in doc['FOLDER']['SHEET']['FIELD']:
    if '#text' in i.keys():
        text = i['#text'] 
    else:
        text = ''
    print(i['@TYPE'], text)
   
template = env.get_template("index.html")

html = template.render({'fields' : doc['FOLDER']['SHEET']['FIELD']})

pdf = MyFPDF()
pdf.add_page()
pdf.write_html(html)
pdf.output('html.pdf', 'F')


# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(json.dumps(doc['FOLDER']['SHEET']['FIELD']))

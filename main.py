import json
from fpdf import FPDF




with open('data.json') as user_file:
    file_contents = user_file.read()

parsed_json = json.loads(file_contents)

users = parsed_json['users']

for x in users:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size = 15)
    pdf.cell(200, 10, txt= f"{x['name']} {x['surname']}",ln = 1, align= 'L')
    pdf.cell(200, 10, txt= "Wygrales "+ f"{x['reward']}", ln = 1, align= 'L')

    pdf.output(f"{x['name']}.pdf")




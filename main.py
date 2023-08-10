from flask import *
from fpdf import FPDF
import zipfile
import glob

app = Flask(__name__)


@app.route('/', methods=['POST'])
def create_pdf():
    data = request.get_json()
    users = data['users']

    for x in users:
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Arial', '', 'c:\\windows\\Fonts\\Arial.ttf', uni=True)
        pdf.set_font('Arial', size=15)
        pdf.cell(200, 10, txt=f"{x['name']} {x['surname']}", ln=1, align='L')
        pdf.cell(200, 10, txt="Wygrałeś " + f"{x['reward']}", ln=1, align='L')
        pdf.output(f".\\output\\{x['name']}.pdf")
    with zipfile.ZipFile('files.zip', 'w') as f:
        for file in glob.glob('output/*'):
            f.write(file)
    return send_file('files.zip')


if __name__ == "__main__":
    app.run(debug=True)

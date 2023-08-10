from flask import *
import json
from fpdf import FPDF

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
        pdf.output(f"{x['name']}.pdf")

    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)

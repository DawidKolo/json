from flask import *
from fpdf import FPDF
import zipfile
import glob
import os
import datetime

calendar = datetime.datetime.now()

app = Flask(__name__)


@app.after_request
def delete_files(response):
    path = ".\\output\\"
    for file in os.listdir(path):
        os.remove(os.path.join(path, file))

    return response


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
    return send_file('files.zip'), 200


@app.route('/')
def html_placeholder():
    stamp_d = calendar.strftime("%d")
    stamp_m = calendar.strftime("%B")
    stamp_y = calendar.strftime("%Y")
    time_h = calendar.strftime("%H")
    time_m = calendar.strftime("%M")
    time_s = calendar.strftime("%S")
    return f"<p>Send json file, please.</p> {stamp_d} {stamp_m} {stamp_y} <br> {time_h} : {time_m} : {time_s}"


if __name__ == "__main__":
    app.run()

from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="DB_PY"
)

def Cadastrar():
    
    if atividadePY.radioButton.isChecked():
        corLed = 'led_vermelho'
    elif atividadePY.radioButton_2.isChecked():
        corLed = 'led_verde'
    elif atividadePY.radioButton_3.isChecked():
        corLed = 'IIHHH'
    else: 
        corLed = 'null'   
        
    cursor = banco.cursor()
    cursor.execute("INSERT INTO TB_LED (LED_COR) values (%s)", ([corLed]))
    banco.commit()
    print('Cadastrado com sucesso')
 

app = QtWidgets.QApplication([])
atividadePY = uic.loadUi("design.ui")
atividadePY.pushButton.clicked.connect(Cadastrar)

atividadePY.show()
app.exec()

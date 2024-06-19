from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_agenda"
)

def Cadastrar():
    campoNome = agenda.textEdit_4.text()
    campoEmail = agenda.textEdit_5.text()
    campoTelefone = agenda.textEdit_2.text()
    
    if agenda.radioButton_2.isChecked():
        tipoTelefone = 'residencial'
    elif agenda.radioButton.isChecked():
        tipoTelefone = 'celular'
    else :
        tipoTelefone = 'nao especificado'    
    
    cursor = banco.cursor()
    cursor.execute("INSERT INTO tb_contatos (nome, email, telefone, tipoTelefone) values (%s, %s, %s, %s)", (str(campoNome), str(campoEmail), str(campoTelefone), str(tipoTelefone)))
    banco.commit()
    print('Cadastrado com sucesso')


def ConsultarContato():
    listarContatos.show()
    agenda.hide()
    
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tb_contatos")
    contatosLidos = cursor.fetchall()
    
    listarContatos.tabelaCtt.setRowCount(len(contatosLidos))
    listarContatos.tabelaCtt.setColumnCount(5)
    
    for i in range(0, len(contatosLidos)):
        for f in range (0, 5) :
            listarContatos.tabelaCtt.setItem(i, f, QtWidgets.QTableWidgetItem(str(contatosLidos[i][f])))

def excluirContato():
    linhaContato = listarContatos.tabelaCtt.currentRow()
    listarContatos.tabelaCtt.removeRow(linhaContato)
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tb_contatos")

    contatos_lidos = cursor.fetchall()
    valorId = contatos_lidos[linhaContato][0]
    cursor.execute("DELETE FROM tb_contatos WHERE id=" + str(valorId))
    
def EditarCadastro():
    campoIdE = agenda.textEdit_3.text()
    campoNomeE = agenda.textEdit_4.text()
    campoEmailE = agenda.textEdit_5.text()
    campoTelefoneE = agenda.textEdit_2.text()
    
    if agenda.radioButton_2.isChecked():
        tipoTelefone = 'residencial'
    elif agenda.radioButton.isChecked():
        tipoTelefone = 'celular'
    else :
        tipoTelefone = 'nao especificado'    
    
    cursor = banco.cursor()
    cursor.execute(f"UPDATE tb_contatos set nome = '{campoNomeE}', email = ''{campoEmailE}' , telefone = '{campoTelefoneE}', tipoTelefone = '{tipoTelefone}' where id = {int(campoIdE)}")
    banco.commit()
    print('Editado com sucesso')

    
    
def gerarPdf():
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tb_contatos")
    contatos_lidos = cursor.fetchall()
    
    y = 0
    pdf = canvas.Canvas("lista_contatos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Lista de Contatos")
    
    pdf.setFont("Times-Bold", 15)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(60, 750, "NOME")
    pdf.drawString(180, 750, "EMAIL")
    pdf.drawString(370, 750, "TELEFONE")
    pdf.drawString(460, 750, "TIPO DE CONTATO")
    
    for i in range(0, len(contatos_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(contatos_lidos[i][0]))
        pdf.drawString(60, 750 - y, str(contatos_lidos[i][1]))
        pdf.drawString(180, 750 - y, str(contatos_lidos[i][2]))
        pdf.drawString(370, 750 - y, str(contatos_lidos[i][3]))
        pdf.drawString(460, 750 - y, str(contatos_lidos[i][4]))
    
    pdf.save()
    print("PDF GERADO COM SUCESSO")
        
def BotaoVoltarAgenda():
    listarContatos.hide()
    agenda.show()
    
def BotaoEditarContato():
    listarContatos.hide()
    editar.show()
    
def BotaoVoltarcontato():
    editar.hide()
    listarContatos.show()


    
app = QtWidgets.QApplication([])
agenda = uic.loadUi("design.ui")
listarContatos = uic.loadUi("contatos.ui")
editar = uic.loadUi("editar.ui")

agenda.btnCadastro.clicked.connect(Cadastrar)
agenda.btnConsCont.clicked.connect(ConsultarContato)

listarContatos.btnGerarPdf.clicked.connect(gerarPdf)
listarContatos.btnExcluirCtt.clicked.connect(excluirContato)
listarContatos.btnVoltar.clicked.connect(BotaoVoltarAgenda)
listarContatos.btnEditar.clicked.connect(BotaoEditarContato)
editar.btnVoltar_2.clicked.connect(BotaoVoltarcontato)

agenda.show()
app.exec()











    


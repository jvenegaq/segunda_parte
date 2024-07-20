import sys
import sqlite3
from PyQt5 import QtWidgets, uic

class MiVentana(QtWidgets.QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        uic.loadUi('mipantalla.ui', self)
        
        self.conectar_base_datos()
        self.crear_tabla_si_no_existe()
        self.cargar_datos()
    
        self.pushButton.clicked.connect(self.agregar_equipo)

        self.pushButtonBorrar.clicked.connect(self.borrar_equipo)
        
        self.pushButtonTabla.clicked.connect(self.agregar_tabla_resultados)

    def conectar_base_datos(self):
        self.conn = sqlite3.connect('base_solucion1.db')
        self.cursor = self.conn.cursor()

    def crear_tabla_si_no_existe(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def cargar_datos(self):
        self.cursor.execute("SELECT * FROM equipos")
        equipos = self.cursor.fetchall()
        for equipo in equipos:
            self.listaEquipos.addItem(f"{equipo[0]} - {equipo[1]}")

    def agregar_equipo(self):
        
        nombre_equipo = self.lineEdit.text()
        if nombre_equipo:  
           
            self.cursor.execute("INSERT INTO equipos (nombre) VALUES (?)", (nombre_equipo,))
            self.conn.commit()
            self.listaEquipos.addItem(nombre_equipo)
            self.lineEdit.clear()

    def borrar_equipo(self):
        selected_item = self.listaEquipos.currentItem()
        if selected_item:
            nombre_equipo = selected_item.text()
            self.cursor.execute("DELETE FROM equipos WHERE nombre = ?", (nombre_equipo,))
            self.conn.commit()
            self.listaEquipos.takeItem(self.listaEquipos.row(selected_item))

    def agregar_tabla_resultados(self):
        self.tablaResultados = QtWidgets.QTableWidget()
        self.tablaResultados.setRowCount(10)  
        self.tablaResultados.setColumnCount(3)  
        self.tablaResultados.setHorizontalHeaderLabels(['Equipo', 'Puntos', 'Posición'])
        self.tablaResultados.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())

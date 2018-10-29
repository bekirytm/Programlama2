import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui

class tabloOrnek(QDialog):
    def __init__(self,ebeveyn=None):
        super(tabloOrnek,self).__init__(ebeveyn)

#stylesheet 
        stylesheet="""
        QWidget#Pencere {background-image: url(arka.png);}
        QTableWidget#tablo {font:"Tahoma"; font-size:9pt;}
        """

        QtGui.qApp.setStyleSheet(stylesheet)

#grid kısmı
        grid=QGridLayout()

        self.tablo=QTableWidget()
        self.tablo.setFixedWidth(450)
        self.tablo.setFixedHeight(250)
        self.tablo.setRowCount(4)
        self.tablo.setColumnCount(3)
        grid.addWidget(self.tablo)
        self.tablo.setHorizontalHeaderLabels(['İsim', 'Soyisim', 'Bölüm'])
        self.tablo.setObjectName('tablo')
        item=QTableWidgetItem()
            

#Veri ekleme
        self.ogrenci=["Can","Aydın","YBS"]
        self.ogrenci2=["Semih","Yarar","YBS"]
        self.ogrenci3=["Büşra","Demirgüreşçi","İktisat"]
        self.tabloSıra=0
        self.tabloSutun=0
        for x in self.ogrenci:
            if self.tabloSıra==0:
                self.tablo.setItem(self.tabloSıra,self.tabloSutun,QTableWidgetItem(x))
                self.tabloSutun=self.tabloSutun+1

        for y in self.ogrenci2:
            if self.tabloSıra==0:
                self.tablo.setItem(self.tabloSıra,self.tabloSutun,QTableWidgetItem(y))
                self.tabloSutun=self.tabloSutun+1


        for z in self.ogrenci3:
            if self.tabloSıra==0:
                self.tablo.setItem(self.tabloSıra,self.tabloSutun,QTableWidgetItem(z))
                self.tabloSutun=self.tabloSutun+1
    

    
        self.setLayout(grid)
        self.tablo.show()
        self.setWindowTitle("Sınıf Tablo")
        self.resize(500,300)


uyg=QApplication([])
pencere=tabloOrnek()
pencere.setObjectName('Pencere')
pencere.show()
uyg.exec_
        












        

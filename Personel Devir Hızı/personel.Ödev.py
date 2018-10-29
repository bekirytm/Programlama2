import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui

class personel(QDialog):
    def __init__(self,ebeveyn=None):
        super(personel,self).__init__(ebeveyn)

        stylesheet="""
        QWidget#pencere {background-image: url(arkaplan1.png);}
        
        """    
        QtGui.qApp.setStyleSheet(stylesheet)
        
        grid=QGridLayout()

        grid.addWidget(QLabel("1. AY:"),0,0)
        self.birAy=QLineEdit()
        grid.addWidget(self.birAy,0,1)

        grid.addWidget(QLabel("2. AY:"),1,0)
        self.ikiAy=QLineEdit()
        grid.addWidget(self.ikiAy,1,1)

        grid.addWidget(QLabel("3. AY:"),2,0)
        self.ucAy=QLineEdit()
        grid.addWidget(self.ucAy,2,1)

        grid.addWidget(QLabel("4. AY:"),3,0)
        self.dortAy=QLineEdit("")
        grid.addWidget(self.dortAy,3,1)

        grid.addWidget(QLabel("5. AY:"),4,0)
        self.besAy=QLineEdit()
        grid.addWidget(self.besAy,4,1)

        grid.addWidget(QLabel("6. AY:"),5,0)
        self.altıAy=QLineEdit()
        grid.addWidget(self.altıAy,5,1)

        grid.addWidget(QLabel("7. AY:"),6,0)
        self.yediAy=QLineEdit()
        grid.addWidget(self.yediAy,6,1)

        grid.addWidget(QLabel("8. AY:"),7,0)
        self.sekizAy=QLineEdit()
        grid.addWidget(self.sekizAy,7,1)

        grid.addWidget(QLabel("9. AY:"),8,0)
        self.dokuzAy=QLineEdit()
        grid.addWidget(self.dokuzAy,8,1)

        grid.addWidget(QLabel("10. AY:"),9,0)
        self.onAy=QLineEdit()
        grid.addWidget(self.onAy,9,1)

        grid.addWidget(QLabel("11. AY:"),10,0)
        self.onbirAy=QLineEdit()
        grid.addWidget(self.onbirAy,10,1)

        grid.addWidget(QLabel("12. AY:"),11,0)
        self.onikiAy=QLineEdit()
        grid.addWidget(self.onikiAy,11,1)


        grid.addWidget(QLabel("Çıkarılan İşçi Sayısı:"),12,0)
        self.cikarilanSayi=QSpinBox()
        self.cikarilanSayi.setRange(0,25000)
        self.cikarilanSayi.setValue(1)
        grid.addWidget(self.cikarilanSayi,12,1)


        grid.addWidget(QLabel("İşletmedeki Toplam Çalışan Sayısı:"),13,0)
        self.aylıkOrt=QLabel("")
        grid.addWidget(self.aylıkOrt,13,1)

        grid.addWidget(QLabel("Personel Devir Hızınız:"),14,0)
        self.devirHiz=QLabel("")
        grid.addWidget(self.devirHiz,14,1)

        hesapButon=QPushButton("HESAPLA")
        grid.addWidget(hesapButon,15,1)
        self.connect(hesapButon,SIGNAL('pressed()'),self.hesapla)


        self.setLayout(grid)
        self.setWindowTitle("Yıllık Personel Devir Hızı Hesaplama")
        self.setObjectName('liste')
        self.resize(500,450)

    def hesapla(self):
        bir=int(self.birAy.text())
        iki=int(self.ikiAy.text())
        uc=int(self.ucAy.text())
        dort=int(self.dortAy.text())
        bes=int(self.besAy.text())
        alti=int(self.altıAy.text())
        yedi=int(self.yediAy.text())
        sekiz=int(self.sekizAy.text())
        dokuz=int(self.dokuzAy.text())
        on=int(self.onAy.text())
        onbir=int(self.onbirAy.text())
        oniki=int(self.onikiAy.text())
        cikan=int(self.cikarilanSayi.text())
        ortCalisan=(bir+iki+uc+dort+bes+alti+yedi+sekiz+dokuz+on+onbir+oniki)/12
        self.aylıkOrt.setText('<font color:"red">%0.1f</font>'%ortCalisan)
        perDevir=(cikan/ortCalisan)*100
        self.devirHiz.setText('<font color="Blue">%0.1f</font>'%perDevir)
        
        


        
uygulama=QApplication([])
pencere=personel()
pencere.setObjectName('pencere')
pencere.show()
uygulama.exec_

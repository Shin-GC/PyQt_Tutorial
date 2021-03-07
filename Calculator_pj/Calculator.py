import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Calculator')
        self.statusBar().showMessage('대기 중')

        btn = QPushButton('종료', self)
        btn.move(160,145)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        QToolTip.setFont(QFont('SansSerif',10))
        
        btn.setToolTip('프로그램을 종료합니다.')
        btn1 = QPushButton('1', self)
        btn1.move(0,100)
        btn1.resize(btn1.sizeHint())

        btn2 = QPushButton('2', self)
        btn2.move(55,100)
        btn2.resize(btn2.sizeHint())

        btn3 = QPushButton('3', self)
        btn3.move(110,100)
        btn3.resize(btn3.sizeHint())

        btn4 = QPushButton('4', self)
        btn4.move(0,130)
        btn4.resize(btn4.sizeHint())

        btn5 = QPushButton('5', self)
        btn5.move(55,130)
        btn5.resize(btn5.sizeHint())

        btn6 = QPushButton('6', self)
        btn6.move(110,130)
        btn6.resize(btn6.sizeHint())

        btn7 = QPushButton('7', self)
        btn7.move(0,160)
        btn7.resize(btn7.sizeHint())

        btn8 = QPushButton('8', self)
        btn8.move(55,160)
        btn8.resize(btn8.sizeHint())

        btn9 = QPushButton('9', self)
        btn9.move(110,160)
        btn9.resize(btn9.sizeHint())

        add_btn = QPushButton('+',self)
        add_btn.move(165,50)
        add_btn.resize(add_btn.sizeHint())
        
        #메뉴 추가
        exitaction = QAction('Exit',self)
        exitaction.setShortcut('Ctrl+Q')
        exitaction.setStatusTip('Exit Application')
        exitaction.triggered.connect(self.exit_Action)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitaction)
    
        self.center()
        self.resize(250, 300)
        self.show()

    def exit_Action(self):
        self.close()
        print('close')
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
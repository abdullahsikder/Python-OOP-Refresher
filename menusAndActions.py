import vtk
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QAction, QWidget , QVBoxLayout , QSlider
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtCore import Qt

class menuAndActions(object):
    def __init__(self , ren, ren2):
        self.ren = ren
        self.ren2 = ren2

        self.slider4 = QSlider( Qt.Horizontal )
        self.slider4.setValue( 80 )
        self.slider4.setRange( 0, 100 )
        self.slider4.setTickInterval( 1 )
        self.slider4.setTickPosition( QSlider.TicksRight )
        print(self)
    def changeBackground2(self):
        self.wid = QWidget()
        self.vb = QVBoxLayout()
        self.vb.addStretch( 1 )

        self.wid.setLayout( self.vb )
        self.wid.resize( 450, 150 )
        self.wid.setWindowTitle( 'Background')

        self.vb.addWidget( self.slider4 )
        self.wid.show()
        print('ss')
        self.slider4.valueChanged.connect( menuAndActions.setBackground2(self) )

    def setBackground2(self):
        sv = self.slider4.value()
        print( sv )
        # sv = self.slider4.value()
        #self.slider4.valueChanged.connect( self.menuAndActions.setBackground )

    def createActions(self) :
        self.aboutQtAct = QAction( "About &Qt", self,
                                   statusTip="Show the Qt library's About box",
                                   triggered=QApplication.instance().aboutQt )
        self.changeBgk = QAction( "&Background", self, shortcut="Ctrl+B",
                                  statusTip="Set Background", triggered=self.menuAndActions.changeBackground2 )

    def createMenus(self) :
        #self.editMenu = self.menuBar().addMenu( "&Edit" )
        #self.editMenu.addAction( self.changeBgk )

        self.helpMenu = self.menuBar().addMenu( "&Help" )
        self.helpMenu.addAction( self.aboutQtAct )





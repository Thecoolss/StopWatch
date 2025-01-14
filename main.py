import sys
from PyQt5.QtWidgets import QLabel,QPushButton,QApplication,QWidget,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import QTime,Qt,QTimer

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,200,300)
        
        self.time_label=QLabel("00:00:00.00",self)
        self.time=QTime(0,0,0,0)
        self.startbutton=QPushButton("Start",self)
        self.stopbutton=QPushButton("Stop",self)
        self.resetbutton=QPushButton("Reset",self)
        self.timer=QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        hbox=QHBoxLayout()

        hbox.addWidget(self.startbutton)
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)
        
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
                           QPushButton{
                               font-size:50px;
                               font-family:calibri;
                               font-weight:bold;
                               padding:15px 75px;
                               }
                           
                           QLabel{
                               font-size:150px;
                               font-weight:bold;
                               background-color:hsl(200,100%,85%);
                               }
                           """)
        self.stopbutton.clicked.connect(self.stop)
        self.startbutton.clicked.connect(self.start)
        self.resetbutton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update)
        
    def start(self):
        self.timer.start(10)
        
    def stop(self):
        self.timer.stop()
        
    def reset(self):
        self.timer.stop()
        self.time_label.setText(self.formattime(QTime(0,0,0,0)))
    
    def formattime(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        ms=time.msec()//10
        
        return f"{hours:02}:{minutes:02}:{seconds:02}.{ms:02}"
    def update(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.formattime(self.time))
        
        
        
app=QApplication(sys.argv)
stopwatch=Stopwatch()
stopwatch.show()
sys.exit(app.exec_())

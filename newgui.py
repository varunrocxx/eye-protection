from PyQt5 import QtCore, QtGui, QtWidgets 
import PyQt5.QtMultimedia as M

class Ui_Eye(object):
    min_ = int(20) 
    sec_ = int(00)  
    txt_b1 = 20
    txt_b2 = 20
    #n_mod=1
    working = False
    rest = False

    # Music 
    abc = QtCore.QUrl.fromLocalFile("m.wav")
    content = M.QMediaContent(abc)
    player = M.QMediaPlayer()
    player.setMedia(content)


    def eye_mode(self):
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider_2.setEnabled(False)    
        self.min_=int(20)
        self.sec_= int(0)
        self.txt_b2 = int(20)
        self.lcdNumber.display("20:00")

    def timer_(self):
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider_2.setEnabled(True)
        self.min_=self.txt_b1
        self.sec_=self.txt_b2    

    def start_timer(self,interval=950):
        def handler():
            self.display_timer()
            if not self.working :
                timer.stop()
                timer.deleteLater()
        timer = QtCore.QTimer()
        timer.timeout.connect(handler)
        timer.start(interval)

    def display_timer(self):
        abc_ = str(self.min_)+":"+str(self.sec_)
        self.lcdNumber.display(str(abc_))
        if self.sec_ == 0 :
            if self.min_ == 0 :
                self.player.play()
                #self.lcdNumber.display("Done!!")
                #self.working = False
                if self.rest == True:
                    self.min_ = self.txt_b1
                    self.sec_ = int(0)
                    self.rest = False
                else:
                    self.min_ = int(0)
                    self.sec_ = self.txt_b2
                    self.rest = True

            else:
                self.sec_ =59
                self.min_ = self.min_ - 1
        else :
            self.sec_ = self.sec_ - 1

    def start_press(self):
        if self.button1.text() == "Start":
            self.button1.setText("Pause")
            self.working = True
            self.start_timer()

        else:
            self.button1.setText("Start")
            self.working = False     
       
    def reset_Press(self):
        self.lcdNumber.display(self.sec_)
        self.working = False
        self.min_ = int(self.txt_b1)
        self.sec_ = int(0)
        ab_ = str(self.min_)+":00"
        self.lcdNumber.display(str(ab_))

    def valuechange_1(self):
        if self.working == True:
            pass
        else:
            self.txt_b1 = str(self.horizontalSlider.value())
            self.textBrowser1.setText(self.txt_b1)
            self.lcdNumber.display(str(str(self.txt_b1)+":00"))
            self.min_ = int(self.txt_b1)
            self.sec_ = int(0)

    def valuechange_2(self):
        self.txt_b2 = str(self.horizontalSlider_2.value())
        self.textBrowser2.setText(self.txt_b2)
        self.sec_ = int(self.txt_b2)
        #self.lcdNumber.display(str(str(self.txt_b1)+":" + str(self.txt_b2)))

    def mode_(self):
        if (self.radioButton_3.isChecked()):
            self.player.setVolume(100)
            self.eye_mode()
                #Eye Protection
        elif (self.radioButton_2.isChecked()):
            self.player.setVolume(100)
            self.timer_()    #custom Timer
        else:
            self.player.setVolume(0)           
         
#----------------Gui Initialization---------------------

    def setupUi(self, Eye):
        Eye.setObjectName("Eye")
        #Eye.resize(547, 370)
        Eye.setFixedSize(547, 370)
        self.centralwidget = QtWidgets.QWidget(Eye)
        self.centralwidget.setObjectName("centralwidget")

#--------------------Label-----------------------------------
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-4, -8, 561, 381))
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setPixmap(QtGui.QPixmap("bg.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        #--------
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 310, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        #---------
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #---------
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("sans seref")
        font.setPointSize(11)
        #font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #---------
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 30, 240, 51))
        font = QtGui.QFont()
        #font.setFamily("Forte")
        font.setFamily("sans seref")
        font.setPointSize(22)
        font.setWeight(75)
        self.label1.setFont(font)
        #self.label1.setAutoFillBackground(True)
        self.label1.setScaledContents(True)
        self.label1.setObjectName("label1")
        self.label1.setStyleSheet('color: white')
        #----------
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 190, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        #font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #------------
        self.label_2.setStyleSheet('color: white')
        self.label_3.setStyleSheet('color: white')
        self.label_4.setStyleSheet('color: white')
        self.label.setStyleSheet('color: white')
        

#--------------------Buttons---------------------------------
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(30, 110, 121, 41))
        self.button1.setMouseTracking(True)
        self.button1.setFlat(False)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.start_press)
        #-----
        self.button1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button1_2.setGeometry(QtCore.QRect(180, 110, 121, 41))
        self.button1_2.setMouseTracking(True)
        self.button1_2.setFlat(False)
        self.button1_2.clicked.connect(self.reset_Press)
        self.button1_2.setObjectName("button1_2")


#--------------------Radio Buttons---------------------------
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(390, 290, 141, 41))
        self.radioButton.setObjectName("radioButton")
        #self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.radioButton.setStyleSheet("QRadioButton {  color:white ; }")
        self.radioButton.toggled.connect(self.mode_)
        #----------
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(390, 250, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet("QRadioButton {  color:white ; }")
        self.radioButton_2.toggled.connect(self.mode_)
        #----------
       #self.radioButton_3{color: rgb(255, 255, 255);}
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget )
        self.radioButton_3.setGeometry(QtCore.QRect(390, 200, 111, 17))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setStyleSheet("QRadioButton {  color:white ; }")
        self.radioButton_3.toggled.connect(self.mode_)

#--------------------LCD Screen------------------------------
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(280, 20, 231, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(str(str(self.min_)+ ":" +str(self.sec_)))

#--------------------Horizontal Slider------------------------  
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 230, 161, 31))
        self.horizontalSlider.setMaximum(60)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setValue(self.txt_b1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setObjectName("horizontalSlider")
        #self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.valueChanged.connect(self.valuechange_1)
        self.horizontalSlider.setEnabled(False)
        
        #--------------
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(20, 300, 161, 31))
        self.horizontalSlider_2.setMaximum(60)
        self.horizontalSlider_2.setSingleStep(5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setValue(self.txt_b2)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.valuechange_2)
        self.horizontalSlider_2.setEnabled(False)


#--------------------Text Browser-----------------------------
        self.textBrowser1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser1.setGeometry(QtCore.QRect(190, 230, 51, 31))
        self.textBrowser1.setObjectName("textBrowser1")
        self.textBrowser1.setText(str(self.txt_b1))
        #----------------
        self.textBrowser2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser2.setGeometry(QtCore.QRect(190, 300, 51, 31))
        self.textBrowser2.setObjectName("textBrowser2")
        self.textBrowser2.setText(str(self.txt_b2))


#--------------------Line--------------------------------------    
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-3, 149, 551, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


#-----------------------EXPERIMENTAL AREA ---------------------------
        #This tab
        # Steps to add Timer  



#--------------------------------------------------------------------
        #Imp code parts
        #self.radioButton_1.toggled.connect(lambda:self.btnstate(self.b1))
        
        Eye.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(Eye)
        # self.statusbar.setObjectName("statusbar")
        # Eye.setStatusBar(self.statusbar)

        self.retranslateUi(Eye)
        QtCore.QMetaObject.connectSlotsByName(Eye)

    def retranslateUi(self, Eye):
        _translate = QtCore.QCoreApplication.translate
        Eye.setWindowTitle(_translate("Eye", "Eye Protector"))
        self.button1.setText(_translate("Eye", "Start"))
        self.radioButton.setText(_translate("Eye", "Mute","color: white"))
        self.label1.setText(_translate("Eye", "Time Remaining"))
        self.label.setText(_translate("Eye", "Working Timer"))
        self.label_2.setText(_translate("Eye", "Rest Timer"))
        self.button1_2.setText(_translate("Eye", "Reset"))
        self.radioButton_2.setText(_translate("Eye", "Custom Timer"))
        self.radioButton_3.setText(_translate("Eye", "Eye Protection"))
        self.label_3.setText(_translate("Eye", "Min"))
        self.label_4.setText(_translate("Eye", "Sec"))
#import abc_rc

#--------------None of your business---------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Eye = QtWidgets.QMainWindow()
    ui = Ui_Eye()
    ui.setupUi(Eye)
    Eye.show()
    sys.exit(app.exec_())

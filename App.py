from scipy.signal import freqz, zpk2tf
from numpy import log10
from matplotlib.pyplot import axvline, axhline
from scipy.signal import freqz, lfilter
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5agg
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import csv
import time
import numpy as np
import json
from scipy import signal
from PyQt5.QtWidgets import QSlider
def create_widget(parent_widget, x, y, width, height):
    widget = QtWidgets.QWidget(parent_widget)
    widget.setGeometry(x, y, width, height)
    layout = QtWidgets.QVBoxLayout(widget)
    layout.setSizeConstraint(QtWidgets.QVBoxLayout.SetMinAndMaxSize)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(2)
    return widget, layout

def create_plot_widget(parent_layout, plot_title):
    figure = Figure()
    drawing = figure.add_subplot(111)
    figure.suptitle(plot_title)
    drawing.plot()
    drawing.set_xlabel('Normalized frequency', fontsize=11)
    drawing.set_ylabel('Amplitude', fontsize=9)
    canvas = matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg(figure)
    parent_layout.addWidget(canvas)
    canvas.draw()

    text_label = QtWidgets.QLabel("Phase response")
    text_label.setAlignment(Qt.AlignCenter)

    font = QFont()
    font.setPointSize(12)
    text_label.setFont(font)
    parent_layout.addWidget(text_label)

    apply_button = QtWidgets.QPushButton("Apply")
    parent_layout.addWidget(apply_button)

    return drawing,canvas, apply_button

class DataReaderThread(QtCore.QThread):
    data_ready = QtCore.pyqtSignal(list)

    def __init__(self, file_path):
        super(DataReaderThread, self).__init__()
        self.file_path = file_path
        self.running = True

    def run(self):
        with open(self.file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if not self.running:
                    break
                data_row = list(map(float, row))
                self.data_ready.emit(data_row)
                time.sleep(0.1)


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 10, 500, 500))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(600, 10, 570, 250))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.widget_6= QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(600, 260, 570, 250))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.widget_7, self.verticalLayout_7 = create_widget(self.centralwidget, 20, 600, 400, 300)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.widget_8, self.verticalLayout_8 = create_widget(self.centralwidget, 500, 600, 400, 300)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.widget_9, self.verticalLayout_9 = create_widget(self.centralwidget, 1000, 600, 400, 300)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.widget_10, self.verticalLayout_10 = create_widget(self.centralwidget, 1500, 600, 400, 300)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.textbox_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.verticalLayout_10.addWidget(self.textbox_10)

        self.view_button_10 = QtWidgets.QPushButton("View", self.centralwidget)
        self.verticalLayout_10.addWidget(self.view_button_10)

        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(1150, 10, 550, 231))
        self.widget3.setObjectName("widget_3")
        self.verticalLayout3 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout3.setObjectName("verticalLayou_3t")

        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(1150, 250, 550, 231))
        self.widget4.setObjectName("widget_4")
        self.verticalLayout4 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout4.setObjectName("verticalLayou_4t")


    #    self.widget5 = QtWidgets.QWidget(self.centralwidget)
    #    self.widget5.setGeometry(QtCore.QRect(900, 620, 471, 231))
    #    self.widget5.setObjectName("widget_5")
    #    self.verticalLayout5 = QtWidgets.QVBoxLayout(self.widget5)
    #    self.verticalLayout5.setContentsMargins(0, 0, 0, 0)
    #    self.verticalLayout5.setObjectName("verticalLayou_5t")



        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(0, 550, 2000, 50))
        self.layoutWidget4.setObjectName("layoutWidget")
        self.lay4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.lay4.setContentsMargins(0, 0, 0, 0)
        self.lay4.setObjectName("lay3")
        line_label = QtWidgets.QLabel()
        line_label.setFrameShape(QtWidgets.QFrame.HLine)  # Set frame shape to horizontal line
        line_label.setFrameShadow(QtWidgets.QFrame.Sunken)  # Set frame shadow
        self.lay4.addWidget(line_label)

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 50, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.lay2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.lay2.setContentsMargins(0, 0, 0, 0)
        self.lay2.setObjectName("lay2")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.lay2.addWidget(self.radioButton)

        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 100, 80, 80))
        self.layoutWidget2.setObjectName("layoutWidget")
        self.lay3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.lay3.setContentsMargins(0, 0, 0, 0)
        self.lay3.setObjectName("lay3")
        self.save_button = QtWidgets.QPushButton("Save")
        self.lay3.addWidget(self.save_button)
        self.load_button = QtWidgets.QPushButton("Load")
        self.lay3.addWidget(self.load_button)
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.lay3.addWidget(self.clear_button)
        self.checkbox = QtWidgets.QCheckBox("Conjugate", self)
        self.lay3.addWidget(self.checkbox)


        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.lay2.addWidget(self.radioButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

    #    self.zero_layout = QtWidgets.QVBoxLayout()
    #    self.verticalLayout5.addLayout(self.zero_layout)


    #    self.slider = QSlider(QtCore.Qt.Horizontal)
    #    self.slider.setMinimum(0)
    #    self.slider.setMaximum(100)
    #    self.verticalLayout5.addWidget(self.slider)




        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My_Zero_poles"))
        self.radioButton.setText(_translate("MainWindow", "Zeros"))
        self.radioButton_2.setText(_translate("MainWindow", "Poles"))


class Main(QtWidgets.QMainWindow, Ui_MainWindow2):

    # def add_zero_box(self):
    #     zero_box = QtWidgets.QLineEdit()
    #     self.zero_layout.addWidget(zero_box)


    # def submitButton(self):
    #     zeroes = []
    #     for i in range(self.zero_layout.count()):
    #         zero_box = self.zero_layout.itemAt(i).widget()
    #         zero_value = float(zero_box.text())
    #         zeroes.append(zero_value)

    #     b = [1, 0, 0]
    #     transfere = signal.TransferFunction(zeroes, b)
    #     zeros = transfere.zeros

    #     self.x = np.real(zeros[0])
    #     self.y = np.imag(zeros[0])
    #     self.add_point()

    #     self.x = np.real(zeros[1])
    #     self.y = np.imag(zeros[1])
    #     self.add_point()

    def pause_plotting(self):
        if self.reader_thread and self.reader_thread.isRunning():
            self.reader_thread.running = False
            self.pause_button.setText("Resume")
        else:
            self.data = []
            self.figure3.clear
            self.figure4.clear
            self.reader_thread.running = True
            self.pause_button.setText("Pause")
            self.reader_thread.start()


    def __init__(self):
        super(Main, self).__init__()
        self.libzeros = []
        self.libpoles = []
        self.setupUi(self)
        self.clear =False
        pixmap = QPixmap('x.jpg')
        self.fig = plt.figure()
        # plt.axis('scaled')
        # plt.axis([-1, 1, -1, 1])
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.circle = plt.Circle((0, 0), 1, fill=False)
        self.ax.add_patch(self.circle)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        axvline(0, color='0.3')
        axhline(0, color='0.3')
        self.ax.plot()
        self.canvas = matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg(self.fig)
        self.verticalLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.ax.set_title('Left click to add/drag a point\nRight-click to delete')
        self.toolbar = NavigationToolbar(self.canvas, self, coordinates=True)
        self.addToolBar(self.toolbar)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)

        self.figure2 = Figure()
        self.drawing2 = self.figure2.add_subplot(111)
        self.figure2.suptitle('Magnitude Response')
        self.drawing2.plot()
        self.drawing2.set_xlabel('Normalized frequency',fontsize =11)
        self.drawing2.set_ylabel('Amplitude[dB]', fontsize=9)
        self.canvas2 = matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg(self.figure2)
        self.verticalLayout_2.addWidget(self.canvas2)
        self.canvas2.draw()

        self.figure6 = Figure()
        self.drawing6 = self.figure6.add_subplot(111)
        self.figure6.suptitle('Phase Response')
        self.drawing6.plot()
        self.drawing6.set_xlabel('Normalized frequency',fontsize =11)
        self.drawing6.set_ylabel('Amplitude', fontsize=9)
        self.canvas6 = matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg(self.figure6)
        self.verticalLayout_6.addWidget(self.canvas6)
        self.canvas6.draw()

        self.drawing7 , self.canvas7, self.applyButton7 = create_plot_widget(self.verticalLayout_7, 'a = j0.5')
        self.drawing8 , self.canvas8, self.applyButton8 =create_plot_widget(self.verticalLayout_8, 'a = -0.5 + j0.5')
        self.drawing9 , self.canvas9, self.applyButton9 =create_plot_widget(self.verticalLayout_9, 'a = 0.6')
        self.drawing10 , self.canvas10, self.applyButton10 =create_plot_widget(self.verticalLayout_10, 'Enter a value of "a"')

        self.view_button_10.clicked.connect(self.view_button_10_clicked)

        
        self.canvas_arr=[]
        self.canvas_arr=[self.canvas7,self.canvas8,self.canvas9]
        self.drawing_arr=[]
        self.drawing_arr=[self.drawing7,self.drawing8,self.drawing9]
        self.plotPhaseRespone()
        self.applyButton7.clicked.connect(self.applyButton_7)
        self.applyButton8.clicked.connect(self.applyButton_8)
        self.applyButton9.clicked.connect(self.applyButton_9)
        self.applyButton10.clicked.connect(self.applyButton_10)

        self.browse_button = QtWidgets.QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_csv)


        self.figure3 = Figure()
        self.figure3.suptitle('Frequency Response')
        self.canvas3 = matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg(self.figure3)
        self.verticalLayout3.addWidget(self.canvas3)
        self.verticalLayout3.addWidget(self.browse_button)

        self.figure4 = Figure()
        self.figure4.suptitle('Frequency Response')
        self.canvas4 = matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg(self.figure4)
        self.verticalLayout4.addWidget(self.canvas4)
        
    #    self.submit = QtWidgets.QPushButton("submit")
    #    self.submit.setGeometry(10,10, 10, 200)
    #    self.submit.clicked.connect(self.submitButton)
    #    self.verticalLayout5.addWidget(self.submit)

    #    self.add_zero_button = QtWidgets.QPushButton("Add Zero")
    #    self.add_zero_button.clicked.connect(self.add_zero_box)
    #    self.verticalLayout5.addWidget(self.add_zero_button)


        self.pause_button = QtWidgets.QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_plotting)
        self.verticalLayout3.addWidget(self.pause_button)

    #    self.slider


        self.data = []

        self.reader_thread = None

        self.data2 = []



        self.toolbar = NavigationToolbar(self.canvas2, self, coordinates=True)
        self.addToolBar(self.toolbar)
        self.xy = [] #for the circle
        self.xy2 = []
        self.zero = [] #for trans func
        self.poles = []
        self.tolerance = 10
        self.points = self.ax.scatter([], [], s=30, color='blue', picker=self.tolerance, animated=True) #for zeros
        self.points2 = self.ax.scatter([], [], s=30, marker='x', color='red', picker=self.tolerance, animated=True)

        connect = self.fig.canvas.mpl_connect
        connect('button_press_event', self.on_click)
        self.draw_cid = connect('draw_event', self.grab_background)

        self.save_button.clicked.connect(self.save_data)
        self.load_button.clicked.connect(self.load_data)
        self.clear_button.clicked.connect(self.clear_data)
        self.checkbox.stateChanged.connect(self.checkbox_state_changed)



    def view_button_10_clicked(self):
        self.libpoles = []
        self.libzeros = []
        self.drawing10.clear()
        text = self.textbox_10.text()
        # Do something with the text
        user_a = complex(text)
        self.calcPhaseRespones(user_a)
        num, den = zpk2tf(self.libzeros, self.libpoles, 1)
        w, h = freqz(num, den, worN=10000)
        self.drawing10.plot(w, np.angle(h))
        self.canvas10.draw()



    def checkbox_state_changed(self, state):
        # Slot function to handle checkbox state changes
        if state == 2:  # 2 corresponds to the Qt.Checked state
            print("Checkbox is checked")
        else:
            print("Checkbox is unchecked")


    def applyButton_7(self):
        self.applyButtonHelper(0)

    def applyButton_8(self):
        self.applyButtonHelper(1)

    def applyButton_9(self):
        self.applyButtonHelper(2)

    def applyButton_10(self):
        self.applyButtonHelper(3)


    def applyButtonHelper(self, index):
        if index == 0 or index == 1 or index == 2:
            if self.radioButton.isChecked() == True:
                self.x = np.real(self.libzeros[index])
                self.y = np.imag(self.libzeros[index])
                self.add_point()
                
            if self.radioButton_2.isChecked() == True:
                self.x2 = np.real(self.libpoles[index])
                self.y2 = np.imag(self.libpoles[index])
                self.add_point()
        else:
            if self.radioButton.isChecked() == True:
                self.x = np.real(self.libzeros[0])
                self.y = np.imag(self.libzeros[0])
                self.add_point()
                
            if self.radioButton_2.isChecked() == True:
                self.x2 = np.real(self.libpoles[0])
                self.y2 = np.imag(self.libpoles[0])
                self.add_point()


    def save_data(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Data", "", "Text Files (*.txt)")
        if filename:
            data = "abdullah"
            array_as_string = str(self.xy)

            with open(filename, 'w') as file:
                file.write(array_as_string)

    def load_data(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Load Data", "", "Text Files (*.txt)")
        import json
        if filename:
            with open(filename, 'r') as file:
                data = file.read()
            # self.xy=[]
            self.ayhaga = json.loads(data)
            for i in range (0,len(self.ayhaga)):
                self.x= self.ayhaga[i][0]
                self.y= self.ayhaga[i][1]
                # z = self.x + self.y * 1j
                
                # self.zero.append(z)
                self.add_point()
            
    def clear_data(self):
        self.xy=[[None,None]]
        self.xy2=[[None,None]]
        self.clear = True
        self.zero=[]
        self.poles=[]
        self.update()
        self.drawOn2()


    def browse_csv(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")

        if file_path:
            self.data = []
            self.start_reading(file_path)

    def start_reading(self, file_path):
        if self.reader_thread and self.reader_thread.isRunning():
            self.reader_thread.running = False
            # self.reader_thread.wait()

        self.reader_thread = DataReaderThread(file_path)
        self.reader_thread.data_ready.connect(self.update_plot)
        self.reader_thread.start()

    def update_plot(self, data_row):
        self.data.append(data_row)
        self.plot_data()
        self.plot_data2()




    def plot_data2(self):
        self.figure4.clear()
        self.drawing4 = self.figure4.add_subplot(111)

        if self.data:
            # Assume the CSV file has two columns: x and y
            x = [row[0] for row in self.data]
            y = [row[1] for row in self.data]

            xmin = x[0]
            xmax = xmin + 100
            self.drawing4.set_xlim(xmin, xmax)

            self.drawing4.plot(x, y)
            if len(x) > 100:
                xmin = x[-100]
                xmax = x[-1]
                self.drawing4.set_xlim(xmin, xmax)


        self.canvas4.draw()


    def plot_data(self):
        self.figure3.clear()
        self.drawing3 = self.figure3.add_subplot(111)
        if self.data:
            # Assume the CSV file has two columns: x and y
            x = [row[0] for row in self.data]
            y = [row[1] for row in self.data]
            zeros = self.zero
            if self.poles == []:
                poles = [0]
            else:
                poles = self.poles
            if self.zero == []:
                zeros = [0]
            else:
                zeros = self.zero
            
            numerator = np.poly(zeros) # Numerator coefficients
            denominator = np.poly(poles) # Denominator coefficients

            # Normalize the polynomials
            numerator /= numerator[0]
            denominator /= denominator[0]
    
            # Apply the filter to the input signal
            y5 = signal.TransferFunction(numerator, denominator)
            y5 = signal.lfilter(y5.num, y5.den, y)


            # Set the x-axis limits to keep the scale fixed
            xmin = x[0]
            xmax = xmin + 100  # Change this value to set the width of the x-axis window
            self.drawing3.set_xlim(xmin, xmax)

            # Plot the data and update the x-axis limits
            self.drawing3.plot(x, y5)
            if len(x) > 100:  # Change this value to set the width of the x-axis window
                xmin = x[-100]  # Change this value to set the width of the x-axis window
                xmax = x[-1]
                self.drawing3.set_xlim(xmin, xmax)

        self.canvas3.draw()





    def on_click(self, event):
        if self.radioButton.isChecked() == True:
            contains, info = self.points.contains(event)
            self.x=event.xdata
            self.y=event.ydata
            if contains:
                i = info['ind'][0]
                if event.button == 1:
                    self.start_drag(i)
                elif event.button == 3:
                    self.delete_point(i)
            else:
                self.add_point()
        if self.radioButton_2.isChecked() == True:
            contains2, info2 = self.points2.contains(event)
            self.x2 = event.xdata
            self.y2 = event.ydata
            if contains2:
                i = info2['ind'][0]
                if event.button == 1:
                    self.start_drag(i)
                elif event.button == 3:
                    self.delete_point(i)
            else:
                self.add_point()

    def update(self):
        """Update the artist for any changes to self.xy."""
        if self.clear == False:
            if self.radioButton.isChecked() == True:
                if self.xy ==[]:
                    self.xy=[[None,None]]
                self.points.set_offsets(self.xy)
                self.blit()
            if self.radioButton.isChecked() == False:
                if self.xy2 ==[]:
                    self.xy2=[[None,None]]
                self.points2.set_offsets(self.xy2)
                self.blit()
        else:
            self.xy=[[None,None]]
            self.points.set_offsets(self.xy)
            self.xy2=[[None,None]]
            self.points2.set_offsets(self.xy2)
            self.blit()
            self.clear = False



    def add_point(self):

        if self.radioButton.isChecked() == True:
            #limitation of circle
            if self.xy == [[None,None]]:
                self.xy=[]
            # if ((self.x) ** 2 + (self.y) ** 2) ** 0.5 < 1:
            z = self.x + self.y * 1j
            self.xy.append([self.x, self.y])
            self.zero.append(z)
            if self.checkbox.isChecked():
                self.xy.append([self.x, -self.y])
                z = self.x + -1*self.y * 1j
                self.zero.append(z)
            
            self.update()
            self.drawOn2()
        if self.radioButton_2.isChecked() == True:
            if self.xy2 == [[None,None]]:
                self.xy2=[]
            # if ((self.x2) ** 2 + (self.y2) ** 2) ** 0.5 < 1:
            z = self.x2 + self.y2 * 1j
            self.xy2.append([self.x2, self.y2])
            self.poles.append(z)
            if self.checkbox.isChecked():
                self.xy2.append([self.x2, -self.y2])
                z = self.x2 + -1*self.y2 * 1j
                self.poles.append(z)
            self.update()
            self.drawOn2()

    def delete_point(self, i):
        if self.radioButton.isChecked() == True:
            self.xy.pop(i)
            self.zero.pop()
            self.update()
            self.drawOn2()
        if self.radioButton.isChecked() == False:
            self.xy2.pop(i)
            self.poles.pop()
            self.update()
            self.drawOn2()


    def start_drag(self, i):
        if self.radioButton.isChecked() == True:
            self.drag_i = i
            connect = self.fig.canvas.mpl_connect
            cid1 = connect('motion_notify_event', self.drag_update)
            cid2 = connect('button_release_event', self.end_drag)
            self.drag_cids = [cid1, cid2 ]
        if self.radioButton.isChecked() == False:
            self.drag_i2 = i
            connect = self.fig.canvas.mpl_connect
            cid1 = connect('motion_notify_event', self.drag_update)
            cid2 = connect('button_release_event', self.end_drag)
            self.drag_cids2 = [cid1, cid2]

    def drag_update(self, event):
        """Update a point that's being moved interactively."""
        if self.radioButton.isChecked() == True:
            if event.ydata >=0:
                if len(self.xy)-1 != self.drag_i:
                    if self.xy[self.drag_i+1] == [self.xy[self.drag_i][0], -1*self.xy[self.drag_i][1]]:
                        self.xy[self.drag_i+1] = [event.xdata, -event.ydata]
                self.xy[self.drag_i] = [event.xdata, event.ydata]
                z = event.xdata + event.ydata * 1j
                self.zero[int(self.drag_i /2)] = z
                self.update()
                self.drawOn2()

        if self.radioButton.isChecked() == False:
            if event.ydata >=0:
                if len(self.xy2)-1 != self.drag_i2:
                    if self.xy2[self.drag_i2+1] == [self.xy2[self.drag_i2][0], -1*self.xy2[self.drag_i2][1]]:
                        self.xy2[self.drag_i2+1] = [event.xdata, -event.ydata]
                self.xy2[self.drag_i2] = [event.xdata, event.ydata]
                z = event.xdata + event.ydata * 1j
                self.poles[int(self.drag_i2/2)] = z
                self.update()
                self.drawOn2()



    def end_drag(self, event):
        if self.radioButton.isChecked() == True:
            for cid in self.drag_cids:
                self.fig.canvas.mpl_disconnect(cid)
        if self.radioButton.isChecked() == False:
            for cid in self.drag_cids2:
                self.fig.canvas.mpl_disconnect(cid)




    def grab_background(self, event=None):
        if self.radioButton.isChecked() == True:
            self.points.set_visible(False)
            self.background = self.fig.canvas.copy_from_bbox(self.fig.bbox)
            self.points.set_visible(True)
            self.blit()
        if self.radioButton_2.isChecked() == True    :
            self.points2.set_visible(False)
            self.background2 = self.fig.canvas.copy_from_bbox(self.fig.bbox)
            self.points2.set_visible(True)
            self.blit()


    def blit(self):
        self.fig.canvas.restore_region(self.background)
        self.ax.draw_artist(self.points)
        self.ax.draw_artist(self.points2)
        self.fig.canvas.blit(self.fig.bbox)



    def calcPhaseRespones(self, a):
        self.libzeros.append(1/np.conjugate(a))
        self.libpoles.append(a)



    
    def plotPhaseRespone(self):
            a_arr = [] 
            a_arr = [complex(0, 0.5),complex(-0.5, 0.5),complex(0.6)]
            for i in range(len(a_arr)):
                self.calcPhaseRespones(a_arr[i])
                num, den = zpk2tf([self.libzeros[i]], [self.libpoles[i]], 1)
                w, h = freqz(num, den, worN=10000)
                self.drawing_arr[i].plot(w, np.angle(h))
                self.canvas_arr[i].draw()

        
        

    def drawOn2(self):

        self.drawing2.clear()
        self.drawing6.clear()
        num, den = zpk2tf(self.zero, self.poles, 1)
        w, h = freqz(num, den,worN=10000)
        self.drawing2.plot(w, 10 * log10(abs(h)))
        self.drawing6.plot(w, np.angle(h))        
        self.drawing2.set_xlabel('Normalized frequency', fontsize=9)
        self.drawing2.set_ylabel('Amplitude[dB]', fontsize=9)
        self.canvas2.draw()
        self.canvas6.draw()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import pandas as pd
import pyqtgraph as pg
from PyQt5.QtCore import QTimer

import numpy as np
from scipy import stats
from fpdf import FPDF
from functools import partial

# import UI file
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))

# PDF template
class PDF(FPDF):
    def header(self):
        # Logo
        self.image('images\logo_left.png', 10, 8, 33, 25) 
        self.image('images\logo_right.png', 165, 8, 33, 20)
        # Set font
        self.set_font('helvetica', 'B', 28)
        # Move 15 units down from the top and 90 units right from the left
        self.set_xy(90, 15)
        # Framed title
        self.cell(30, 10, 'Biological Signals Report', 0, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page %s/{nb}' % self.page_no(), 0, 0, 'C')


# initiate IU file
class MainApp(QMainWindow, FORM_CLASS, ):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        # ui
        self.handle_ui()
        
        #pan
        self.widget_4.plotItem.setLimits(xMin=0)
        self.widget_5.plotItem.setLimits(xMin=0)
        
        # color
        self.color_button1.clicked.connect(self.select_color1)
        self.color_button2.clicked.connect(self.select_color2)
        self.selected_color1 = pg.mkPen(color=(255, 0, 0))
        self.selected_color2 = pg.mkPen(color=(255, 0, 0))
        
        # browse
        self.browse.clicked.connect(self.open_file)
        
        # graph1
        self.widget_4.setXRange(min=0, max=13)
        self.widget_4.showGrid(x=True, y=True)
        self.widget_4.addLegend()
        self.plot_window1 = self.widget_4.getPlotItem()
        self.first_file_selected = False
        self.x1 = None
        self.y1 = None
        self.data_lines = []
        self.data_x, self.data_y = [], []
        
        # graph2
        self.widget_5.setXRange(min=0, max=13)
        self.widget_5.showGrid(x=True, y=True)
        self.widget_5.addLegend()
        self.plot_window2 = self.widget_5.getPlotItem()
        self.second_file_selected = False
        self.x2 = None
        self.y2 = None
        self.data_x1, self.data_y1 = [], []
        
        # pause1
        self.play_pause.clicked.connect(self.play_1)
        self.play_pause = False
        self.last_pause_index = 0
        self.play_pause_timer = QTimer()
        self.play_pause_timer.timeout.connect(self.update_all_plots)
        
        # pause2
        self.play_pause_2.clicked.connect(self.play_2)
        self.play_pause_2 = False
        self.last_pause_index2 = 0
        self.play_pause_timer2 = QTimer()
        self.play_pause_timer2.timeout.connect(self.update_all_plots2)

        # pens
        self.pens = [pg.mkPen(color=(255, 0, 0)), pg.mkPen(color=(0, 0, 255)), pg.mkPen(color=(0, 255, 0))]

        # speed
        self.speed_slider1.valueChanged.connect(self.update_speed)
        self.speed_slider2.valueChanged.connect(self.update_speed2)

        # label  
        self.edit_label1.returnPressed.connect(self.edit_curve_label1)
        self.edit_label2.returnPressed.connect(self.edit_curve_label2)
        
        # Connect buttons to zoom functions
        self.zoom_in_1.clicked.connect(self.zoom_in_graph1)
        self.zoom_out_1.clicked.connect(self.zoom_out_graph1)
        self.zoom_in_2.clicked.connect(self.zoom_in_graph2)
        self.zoom_out_2.clicked.connect(self.zoom_out_graph2)

        # horizontal Scroll Bar1
        self.horizontalScrollBar1.valueChanged.connect(self.scroll_x_changed)

        # vertical Scroll Bar1
        self.verticalScrollBar1.valueChanged.connect(self.scroll_y_changed1)

        # horizontal Scroll Bar2
        self.horizontalScrollBar_2.valueChanged.connect(self.scroll_x_changed2)

        # vertical Scroll Bar1
        self.verticalScrollBar_2.valueChanged.connect(self.scroll_y_changed2)

        # hide
        self.hide_checkbox1.stateChanged.connect(self.hide1)
        self.hide_checkbox2.stateChanged.connect(self.hide2)
         
        # channels
        self.current_index = self.channels1.currentIndex() + 2
        self.current_index_2 = self.channels_2.currentIndex() + 2


        self.signal_counter1 = 1
        self.signal_counter2 = 1

        self.idx1 = 50
        self.idx2 = 50
        
        # reset_graph1
        self.reset.clicked.connect(self.reset_graph1)
        self.data_lines2=[]

        # reset_graph1
        self.reset_2.clicked.connect(self.reset_graphs2)

        #link
        self.link_graphs_checkbox.stateChanged.connect(self.link_graphs)
        self.linked=False
        
        #move
        self.move1.clicked.connect(self.move_signal_to_graph5)
        self.move2.clicked.connect(self.move_signal_to_graph4)
          
        # export
        self.export_button.clicked.connect(self.export_report)
        self.stats_list = []
        
        # snapshots
        self.snapshots = []
        self.snapshot_button1.clicked.connect(partial(self.snapshot, self.widget_4, "graph1", "snapshot_button1"))
        self.snapshot_button2.clicked.connect(partial(self.snapshot, self.widget_5, "graph2", "snapshot_button2"))

        
    def handle_ui(self):
        self.setWindowTitle('Signal Viewer')
        self.setWindowIcon(QIcon('images\icon.jpg')) 

        # Set the range of the speed slider
        self.speed_slider1.setRange(0, 200)
        self.speed_slider2.setRange(0, 200)

        # Set the single step, which is the increment or decrement value when using the slider
        self.speed_slider1.setSingleStep(5)
        self.speed_slider2.setSingleStep(5)

        # Set the initial value
        self.speed_slider1.setValue(20)
        self.speed_slider2.setValue(20)

   
    def edit_curve_label1(self):
        # Retrieve the text from the edit_label1 input field
        label_text = self.edit_label1.text()

        # Get the selected channel index from the ComboBox
        selected_index = self.channels1.currentIndex()

        if self.data_lines[selected_index] is not None:
            # Remove the old label for the selected channel
            self.widget_4.removeItem(self.data_lines[selected_index])
            
        if label_text:
            # Create a new plot item with the current data and label for the selected channel
            new_data_line = self.widget_4.plot(self.x1, self.y1, pen=self.selected_color1, name=label_text)
            self.channels1.removeItem(selected_index)
            self.channels1.insertItem(selected_index, label_text)
            self.play_1()
            self.data_lines[selected_index] = new_data_line

        # Clear the input field
        self.edit_label1.clear()

    def edit_curve_label2(self):
        # Retrieve the text from the edit_label1 input field
        label_text = self.edit_label2.text()

        # Get the selected channel index from the ComboBox
        selected_index = self.channels_2.currentIndex()

        if self.data_lines2[selected_index] is not None:
            # Remove the old label
            self.widget_5.removeItem(self.data_lines2[selected_index])

        if label_text:
            # Create a new plot item with the current data and label for the selected channel
            new_data_line = self.widget_5.plot(self.x2, self.y2, pen=self.selected_color2, name=label_text)
            self.channels_2.removeItem(selected_index)
            self.channels_2.insertItem(selected_index, label_text)
            self.play_2()
            self.data_lines2[selected_index] = new_data_line

        # Clear the input field
        self.edit_label2.clear()

    def update_speed(self, value):
        # This method is called when the slider value changes
        print(f"Slider value changed to: {value}")

        # Calculate the interval based on the slider value
        interval = 1000 / value if value > 0 else 1000  

        # Adjust the timer interval for the selected channel
        self.play_pause_timer.setInterval(interval)
        if self.linked:
            self.update_speed2(value)
        
    def update_speed2(self, value):
        # This method is called when the slider value changes
        print(f"Slider value changed to: {value}")

        # Calculate the interval based on the slider value
        interval = 1000 / value if value > 0 else 1000  

        # Adjust the timer interval for the selected channel
        self.play_pause_timer2.setInterval(interval)

    def open_file(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', './', 'CSV Files (*.csv);;Text Files (*.txt)')
        if self.file_name:
            selected_plot_widget = self.choose_graph.currentText().strip()
            if selected_plot_widget == "Graph1":
                item_text = f"Channel {self.signal_counter1}"
                self.first_file_selected = True
                self.read_and_plot_file_graph1(self.file_name, self.selected_color1, item_text, self.widget_4)
                self.play_1()
                self.signal_counter1 += 1
            elif selected_plot_widget == "Graph2":
                item_text = f"Channel {self.signal_counter2}"
                self.second_file_selected = True
                self.read_and_plot_file_graph2(self.file_name, self.selected_color2, item_text, self.widget_5)
                self.play_2()
                self.signal_counter2 += 1

    def read_and_plot_file_graph1(self, file, pen, name, plot_widget):
        data = pd.read_csv(file)
        self.x1 = data.iloc[:, 0].values
        self.y1 = data.iloc[:, 1].values
        data_line = plot_widget.getPlotItem().plot(self.x1, self.y1, pen=pen, name=name)
        self.data_lines.append(data_line)
        self.data_x.append(self.x1)
        self.data_y.append(self.y1)
        item_text = f"Channel {self.current_index}"
        self.channels1.insertItem(self.current_index, item_text)
        self.current_index += 1
        selected_index = self.channels1.currentIndex()
        max_x = max(self.data_x[selected_index])
        min_x = min(self.data_x[selected_index])
        # Update the slider's range to match the X range
        self.horizontalScrollBar1.setMinimum(min_x)
        self.horizontalScrollBar1.setMaximum(max_x - 10)
        max_y = max(self.data_y[selected_index])  
        min_y = min(self.data_y[selected_index]) 
        if self.widget_4.plotItem.setLimits(yMax=max_y):
            self.widget_4.setMouseEnabled(False, False)
            
        if self.widget_4.plotItem.setLimits(yMin=min_y):
            self.widget_4.setMouseEnabled(False, False)

    def read_and_plot_file_graph2(self, file, pen, name, plot_widget):
        data = pd.read_csv(file)
        self.x2 = data.iloc[:, 0].values
        self.y2 = data.iloc[:, 1].values
        data_line = plot_widget.getPlotItem().plot(self.x2, self.y2, pen=pen, name=name)
        # .setxrange
        self.data_lines2.append(data_line)
        self.data_x1.append(self.x2)
        self.data_y1.append(self.y2)
        item_text = f"Channel {self.current_index_2}"
        self.channels_2.insertItem(self.current_index_2, item_text)
        self.current_index_2 += 1
        selected_index = self.channels_2.currentIndex()
        max_x = max(self.data_x1[selected_index])
        min_x = min(self.data_x1[selected_index])
        # Update the slider's range to match the X range
        self.horizontalScrollBar_2.setMinimum(min_x)
        self.horizontalScrollBar_2.setMaximum(max_x - 10)
        max_y = max(self.data_y1[selected_index])  
        min_y = min(self.data_y1[selected_index]) 
        if self.widget_5.plotItem.setLimits(yMax=max_y):
            self.widget_5.setMouseEnabled(False, False)
            
        if self.widget_5.plotItem.setLimits(yMin=min_y):
            self.widget_5.setMouseEnabled(False, False)

    def play_1(self):
        if self.play_pause:
            self.play_pause_timer.stop()
            self.last_pause_index = self.idx1
            self.play_pause = False
        else:
            self.idx1 = self.last_pause_index
            self.play_pause_timer.setInterval(80)
            self.play_pause_timer.start()
            self.play_pause = True

        if self.linked:
            if self.play_pause_2:
                self.play_pause_timer2.stop()
                self.last_pause_index2 = self.idx2
                self.play_pause_2 = False
            else:
                self.idx2 = self.last_pause_index2
                self.play_pause_timer2.setInterval(80)
                self.play_pause_timer2.start()
                self.play_pause_2 = True


    def play_2(self):
        if self.play_pause_2:
            self.play_pause_timer2.stop()
            self.last_pause_index2 = self.idx2
            self.play_pause_2 = False
        else:
            self.idx2 = self.last_pause_index2
            self.play_pause_timer2.setInterval(80)
            self.play_pause_timer2.start()
            self.play_pause_2 = True
            
        if self.linked:
            if self.play_pause:
                self.play_pause_timer.stop()
                self.last_pause_index = self.idx1
                self.play_pause = False
            else:
                self.idx1 = self.last_pause_index
                self.play_pause_timer.setInterval(80)
                self.play_pause_timer.start()
                self.play_pause = True
            
    def update_all_plots(self):
        if self.play_pause:
            for index in range(len(self.data_lines)):
                x = self.data_x[index][:self.idx1]
                y = self.data_y[index][:self.idx1]  
                self.data_lines[index].setData(x, y)
            self.idx1 += 500

    def update_all_plots2(self):
        if self.play_pause_2:
            for index in range(len(self.data_lines2)):
                x = self.data_x1[index][:self.idx2]
                y = self.data_y1[index][:self.idx2]         
                self.data_lines2[index].setData(x, y)
            self.idx2 += 500
            
    def scroll_x_changed(self, value):
        selected_index = self.channels1.currentIndex()
        if self.data_x[selected_index] is not None:
            max_x = max(self.data_x[selected_index])
            min_x = min(self.data_x[selected_index])
            valid_value = max(min(value, max_x - 10), min_x) 
            self.widget_4.setXRange(valid_value, valid_value + 10)
            if self.linked:
                self.widget_5.setXRange(valid_value, valid_value + 10)
    
    def scroll_y_changed1(self):
        selected_index = self.channels1.currentIndex()
        value_vertical = self.verticalScrollBar1.value()

        # Set the minimum and maximum values for the vertical scroll bar
        self.verticalScrollBar1.setMinimum(0)
        self.verticalScrollBar1.setMaximum(len(self.data_y[selected_index]))  

        # Set the single step value for the vertical scroll bar
        self.verticalScrollBar1.setSingleStep(20) 

        # Calculate the range of the Y-axis
        max_y = max(self.data_y[selected_index])  
        min_y = min(self.data_y[selected_index]) 
        my_range = (max_y - min_y) / 5

    
        if 0 <= value_vertical <= len(self.data_y[selected_index]) * (1/5):
            self.widget_4.getPlotItem().setYRange(max_y - my_range, max_y)
        elif len(self.data_y[selected_index]) * (1/5) < value_vertical <= len(self.data_y[selected_index]) * (2/5):
            self.widget_4.getPlotItem().setYRange(max_y - my_range * 2, max_y - my_range)
        elif len(self.data_y[selected_index]) * (2/5) < value_vertical <= len(self.data_y[selected_index]) * (3/5):
            self.widget_4.getPlotItem().setYRange(max_y - my_range * 3, max_y - my_range * 2)
        elif len(self.data_y[selected_index]) * (3/5) < value_vertical <= len(self.data_y[selected_index]) * (4/5):
            self.widget_4.getPlotItem().setYRange(max_y - my_range * 4, max_y - my_range * 3)
        else:
            self.widget_4.getPlotItem().setYRange(min_y, max_y - my_range * 4)

    def scroll_x_changed2(self, value):
        selected_index = self.channels_2.currentIndex()
        if self.data_x1[selected_index] is not None:
            max_x = max(self.data_x1[selected_index])
            min_x = min(self.data_x1[selected_index])
            valid_value = max(min(value, max_x - 10), min_x) 
            self.widget_5.setXRange(valid_value, valid_value + 10)
            if self.linked:
                self.widget_4.setXRange(valid_value, valid_value + 10)

    def scroll_y_changed2(self):
        selected_index = self.channels_2.currentIndex()
        value_vertical = self.verticalScrollBar_2.value()  

        # Set the minimum and maximum values for the vertical scrollbar
        self.verticalScrollBar_2.setMinimum(0)  
        self.verticalScrollBar_2.setMaximum(len(self.data_y1[selected_index]))  

        # Set the single step value for the vertical scrollbar
        self.verticalScrollBar_2.setSingleStep(20)  

        # Calculate the range of the Y-axis for Graph2
        max_y = max(self.data_y1[selected_index])  
        min_y = min(self.data_y1[selected_index])  
        my_range = (max_y - min_y) / 5

       
        if 0 <= value_vertical <= len(self.data_y1[selected_index]) * (1/5):
            self.widget_5.getPlotItem().setYRange(max_y - my_range, max_y)
        elif len(self.data_y1[selected_index]) * (1/5) < value_vertical <= len(self.data_y1[selected_index]) * (2/5):
            self.widget_5.getPlotItem().setYRange(max_y - my_range * 2, max_y - my_range)
        elif len(self.data_y1[selected_index]) * (2/5) < value_vertical <= len(self.data_y1[selected_index]) * (3/5):
            self.widget_5.getPlotItem().setYRange(max_y - my_range * 3, max_y - my_range * 2)
        elif len(self.data_y1[selected_index]) * (3/5) < value_vertical <= len(self.data_y1[selected_index]) * (4/5):
            self.widget_5.getPlotItem().setYRange(max_y - my_range * 4, max_y - my_range * 3)
        else:
            self.widget_5.getPlotItem().setYRange(min_y, max_y - my_range * 4)

    def zoom_in_graph1(self):
        self.widget_4.plotItem.getViewBox().scaleBy((0.5, 0.5))
        if self.linked:
            self.widget_5.plotItem.getViewBox().scaleBy((0.5, 0.5))

    def zoom_out_graph1(self):
        self.widget_4.plotItem.getViewBox().scaleBy((1.5, 1.5))
        if self.linked:
            self.widget_5.plotItem.getViewBox().scaleBy((1.5, 1.5))

    def zoom_in_graph2(self):
        self.widget_5.plotItem.getViewBox().scaleBy((0.5, 0.5))
        if self.linked:
            self.widget_4.plotItem.getViewBox().scaleBy((0.5, 0.5))

    def zoom_out_graph2(self):
        self.widget_5.plotItem.getViewBox().scaleBy((1.5, 1.5))
        if self.linked:
            self.widget_4.plotItem.getViewBox().scaleBy((1.5, 1.5))

    def select_color1(self):
        # creating a QColorDialog object
        dialog = QColorDialog(self)

        # setting current color
        dialog.setCurrentColor(Qt.green)

        # Get the selected color
        self.selected_color1 = dialog.getColor()

        selected_index = self.channels1.currentIndex()
        self.data_lines[selected_index].setPen(self.selected_color1)

    def select_color2(self):  # need edit
        # creating a QColorDialog object
        dialog = QColorDialog(self)

        # setting current color
        dialog.setCurrentColor(Qt.green)

        # Get the selected color
        self.selected_color2 = dialog.getColor()

        selected_index = self.channels_2.currentIndex()
        self.data_lines2[selected_index].setPen(self.selected_color2)

    def hide1(self, state):
        # Get the index of the selected item in the ComboBox
        selected_index = self.channels1.currentIndex()

        if state == Qt.Checked:
            # Hide the selected channel
            self.data_lines[selected_index].setVisible(False)
        else:
            # Show the selected channel
            self.data_lines[selected_index].setVisible(True)
        if self.linked:
            self.hide2(state)

    def hide2(self, state):
        # Get the index of the selected item in the ComboBox
        selected_index = self.channels_2.currentIndex()

        if state == Qt.Checked:
            # Hide the selected channel
            self.data_lines2[selected_index].setVisible(False)
        else:
            # Show the selected channel
            self.data_lines2[selected_index].setVisible(True)

    def reset_graph1(self):
        selected_index = self.channels1.currentIndex()
        # Reset the graphs to their initial state
        self.idx1 = 50  
        # Reset the horizontal scroll bar
        self.horizontalScrollBar1.setValue(0)
        # Clear the data and hide the channels if necessary
        self.data_lines[selected_index].setData([], [])  # Clear the data
        self.data_lines[selected_index].setVisible(True)  # Show the channel
        if self.linked:
            self.reset_graphs2()

    def reset_graphs2(self):
        selected_index = self.channels_2.currentIndex()
        # Reset the graphs to their initial state
        self.idx2 = 50  
        self.horizontalScrollBar1.setValue(0)  
        self.widget_5.setXRange(min=0, max=13)  

        # Clear the data and hide the channels if necessary
        self.data_lines2[selected_index].setData([], [])  # Clear the data
        self.data_lines2[selected_index].setVisible(True)  # Show the channel

    def move_signal_to_graph4(self):
        selected_index = self.channels_2.currentIndex()
        
        x_data = self.data_x1[selected_index]
        y_data = self.data_y1[selected_index]         #+ selected_index * 1.5

        # Remove the signal from Widget 5
        self.widget_5.removeItem(self.data_lines2[selected_index])
        self.data_lines2[selected_index] = None
        self.data_x1[selected_index] = None
        self.data_y1[selected_index] = None

        # Remove the channel from the list and the combo box in Widget 5
        self.data_lines2.pop(selected_index)
        self.data_x1.pop(selected_index)
        self.data_y1.pop(selected_index)
        self.channels_2.removeItem(selected_index)

        item_text = f"Channel_{self.current_index}"
        # Add the signal to Widget 4
        data_line = self.widget_4.plot(x_data, y_data, pen=self.selected_color1, name=item_text)
        self.play_pause = False
        self.play_1()
        self.data_lines.append(data_line)
        self.data_x.append(x_data)
        self.data_y.append(y_data)
        
        self.channels1.insertItem(self.current_index, item_text)
        self.current_index += 1

    def move_signal_to_graph5(self):
        selected_index = self.channels1.currentIndex()
        
        x_data = self.data_x[selected_index]
        y_data = self.data_y[selected_index] #selected_index * 1.5
        
        # Remove the signal from Widget 4
        self.widget_4.removeItem(self.data_lines[selected_index])
        self.data_lines[selected_index] = None
        self.data_x[selected_index] = None
        self.data_y[selected_index] = None

        # Remove the channel from the list and the combo box in Widget 4
        self.data_lines.pop(selected_index)
        self.data_x.pop(selected_index)
        self.data_y.pop(selected_index)
        self.channels1.removeItem(selected_index)
        
        item_text = f"Channel_{self.current_index_2}"
        # Add the signal to Widget 5
        data_line = self.widget_5.plot(x_data, y_data, pen=self.selected_color2, name=item_text)
        self.play_pause_2 = False
        self.play_2()
        self.data_lines2.append(data_line)
        self.data_x1.append(x_data)
        self.data_y1.append(y_data)
    
        self.channels_2.insertItem(self.current_index_2, item_text)
        self.current_index_2 += 1
        item_2 = self.channels_2.currentIndex()
        print(item_2)
            
    def link_graphs(self, state):
        if state == Qt.Checked:
            # Enable linking
            self.linked = True
        else:
            # Disable linking
            self.linked = False
    
    def export_report(self):
        print("Export report function called")  # Debugging
        # Check if a file has been imported for each widget
        if not self.first_file_selected and not self.second_file_selected:
            # Show an error message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please import a graph first to export a report!")
            msg.setWindowTitle("Error: No Graphs Imported")
            # Adjust the width of the message box to fit the text
            msg.layout().setSizeConstraint(QLayout.SetFixedSize)
            msg.exec_()
            
            print("No file has been imported.")
            return
        
        # Create a PDF object
        pdf = PDF()
        # Set the y position to below the header
        y = 40
        # Calculate the width and height of the image based on the page size and margins
        margin = 10  # Set the margin size
        page_width = pdf.w - 2 * margin
        
        # Iterate over all snapshots and their corresponding statistics
        for snapshot, stats_list in zip(self.snapshots, self.stats_list):
            # Set the y position to below the header
            y = 40
            pdf.add_page()
            image = QImage(snapshot)
            image_height = image.height() * page_width / image.width()
            if y + image_height + 10 > pdf.h - pdf.b_margin:
                pdf.add_page()
                y = 40
            pdf.image(snapshot, x = margin, y = y, w = page_width)
            y += image_height + 5

            # Add statistics for this snapshot
            pdf.set_y(y + 5)
            for i, stats_dict in enumerate(stats_list):
                pdf.set_font('helvetica', 'B', 16)
                pdf.cell(0, 10, f"Channel {i+1}", ln=True)
                pdf.set_font('helvetica', 'B', 12)
                pdf.cell(40, 10, "Statistic", 1)
                pdf.cell(0, 10, "Value", 1, ln=True)  
                pdf.set_font('helvetica', '', 12)
                for stat_name in stats_dict:
                    stat_value = stats_dict[stat_name]
                    pdf.cell(40, 10, stat_name.capitalize(), 1)  
                    pdf.cell(0, 10, f"{stat_value:.5f}", 1, ln=True)
                    y= pdf.get_y() # Get the current y position after adding the table
                pdf.ln(5)
                y +=5 # Update y after adding each set of statistics
        # Save the report
        report_folder = "./reports/"
        os.makedirs(report_folder, exist_ok=True)  # Create the folder if it doesn't exist
        # Get the current date and time
        now = QDateTime.currentDateTime()
        timestamp_str = now.toString("yyyy-MM-dd_HH-mm-ss_AP")
        # Open a QFileDialog to name the snapshot
        default_name = f"{report_folder}report_{timestamp_str}.pdf"
        report_filename, _ = QFileDialog.getSaveFileName(self, f'Save Report', default_name, 'PDF Files (*.pdf)')

        if report_filename:  # If a file name was provided
            pdf.output(report_filename)

            # Show a success message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Success: the report has been exported successfully!")
            msg.setWindowTitle("Success")
            # Adjust the width of the message box to fit the text
            msg.layout().setSizeConstraint(QLayout.SetFixedSize)
            msg.exec_()
            
            print("Report exported successfully.")
        
    def snapshot(self, widget, graph_id, button_clicked):
        # Check if there are any plots in the widget
        if not widget.getPlotItem().items:
            # If not, show an error message and return
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please plot a signal first to take a snapshot!")
            msg.setWindowTitle("Error: Cannot Take Snapshot")
            # Adjust the width of the message box to fit the text
            msg.layout().setSizeConstraint(QLayout.SetFixedSize)
            msg.exec_()
            return
        
        # Check if the graphs are paused
        if (button_clicked == "snapshot_button1" and self.play_pause) or (button_clicked == "snapshot_button2" and self.play_pause_2):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Please pause the graph before taking a snapshot.")
            msg.setWindowTitle("Snapshot Pause")
            # Adjust the width of the message box to fit the text
            msg.layout().setSizeConstraint(QLayout.SetFixedSize)
            msg.exec_()
            return
        
        # Set a variable to indicate which button was clicked
        self.last_clicked = button_clicked
        
        image = QImage(widget.viewport().size(), QImage.Format_ARGB32)
        painter = QPainter(image)
        widget.render(painter, source=widget.viewport().rect())
        painter.end()
        
        now = QDateTime.currentDateTime()
        timestamp_str = now.toString("yyyy-MM-dd_HH-mm-ss_AP")
        
        # Save the current view of the plot as an image
        image_folder = f"./snapshots/{graph_id}_plots/"
        os.makedirs(image_folder, exist_ok=True)  # Create the folder if it doesn't exist
        
        # Open a QFileDialog to name the snapshot
        default_name = f"{image_folder}plot_{graph_id}_{timestamp_str}.png"
        image_filename, _ = QFileDialog.getSaveFileName(self, f'Save Snapshot for {graph_id}', default_name, 'Images (*.png *.jpg *.jpeg)')

        if image_filename:  # If a file name was provided
            image.save(image_filename)
            
            # Save the snapshot path and folder names
            self.snapshots.append(image_filename)
            if self.last_clicked == "snapshot_button1":
                stats_list = []
                # Calculate and store statistics of the displayed y-values
                for index in range(len(self.data_lines)):
                    y = self.data_y[index][:self.idx1]
                    y_min, y_max = self.widget_4.getPlotItem().getViewBox().viewRange()[1]
                    y_displayed = [value for value in y if y_min <= value <= y_max]
                    if y_displayed:
                        mean = stats.tmean(y_displayed)
                        median = np.median(y_displayed)
                        std_dev = stats.tstd(y_displayed)
                        min_val = min(y_displayed)
                        max_val = max(y_displayed)
                        stats_dict = {
                            'mean': mean,
                            'median': median,
                            'std_dev': std_dev,
                            'min': min_val,
                            'max': max_val
                        }
                    stats_list.append(stats_dict)
                self.stats_list.append(stats_list)
            elif self.last_clicked == "snapshot_button2":
                stats_list = []
                # Calculate and store statistics of the displayed y-values
                for index in range(len(self.data_lines2)):
                    y = self.data_y1[index][:self.idx2]
                    y_min, y_max = self.widget_5.getPlotItem().getViewBox().viewRange()[1]
                    y_displayed = [value for value in y if y_min <= value <= y_max]
                    if y_displayed:
                        mean = stats.tmean(y_displayed)
                        median = np.median(y_displayed)
                        std_dev = stats.tstd(y_displayed)
                        min_val = min(y_displayed)
                        max_val = max(y_displayed)
                        stats_dict = {
                            'mean': mean,
                            'median': median,
                            'std_dev': std_dev,
                            'min': min_val,
                            'max': max_val
                        }
                    stats_list.append(stats_dict)
                self.stats_list.append(stats_list)

            # Show a success message
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Success")
            msgBox.setText("Snapshot saved successfully!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            # Adjust the width of the message box to fit the text
            msgBox.layout().setSizeConstraint(QLayout.SetFixedSize)


            # Use a QTimer to automatically close the message box after 1 second
            QTimer.singleShot(1000, lambda: msgBox.close())

            # Show the message box
            msgBox.exec_()
            
            print(f"Snapshot saved in {image_folder}") # Debugging
        

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
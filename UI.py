import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QLabel, QSizePolicy, QHeaderView,QLineEdit
from PyQt5.QtCore import Qt 
import pandas as pd
from sortingAlgos import bubbleSort,selectionSort,mergeSort,sortQuick,insertionSort,countingSort,radixS,bucket_sort
import time


data_list=[]
df=pd.read_csv("data1.csv")
data_list=df.values.tolist()



# This is main class (App) and this class inherits from QMainWindwo ,set up the main window and widgets
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Data Sorting Projects')
        self.setGeometry(450,200,1100,700)

        central_widget=QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout=QVBoxLayout(central_widget)

        # creata a label to display sorting time
        self.time_Label=QLabel("Sorting Time: not sorted yet")
        self.time_Label.setStyleSheet("font-size:20px;"
                                      "color:gray;"
                                      "font-weight:bold;"
                                      "padding-left:200;"
                                      "padding-top:20;")
                                      
        main_layout.addWidget(self.time_Label)

        # create a table to display data
        self.table=QTableWidget()
        self.table.setRowCount(len(data_list))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['Title',"Price","Discounted Price","Off","Rating","Sold","Image URL"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setFixedWidth(100)
        for row_index in range(len(data_list)):
           self.table.setRowHeight(row_index, 40)  
         
        main_layout.addWidget(self.table)
        self.load_data()

        self.table.setStyleSheet("""
                                QTableWidget{
                                 font-size:16px;
                                 border:1px solid brown;
                                 background-color:#e8f4ff;
                                 
                                            }
                                 QHeaderView::section{
                                 background-color: #787a80;
                                 padding: 12px;
                                 font-size: 20px;
                                 font-family: Arial, Helvetica, sans-serif;
                                 width:20px;
                                 border: 1px solid black;
                                 }
                                   QTableWidget QTableCornerButton::section {
                                       background-color: #404040;
                                       border: 1px solid black;
                                 }
                                
                              
                          """)
        
        # Enter Column Name here:
        self.column_input = QLineEdit()
        self.column_input.setPlaceholderText("Enter column name to sort by")
        self.column_input.setStyleSheet("""
                  QLineEdit{
                                        font-size:16px;
                                        color:black;
                                        padding:10px;
                                        width:50%;
                                        }
                                        QLineEdit::placeholder{
                                        color:black;}""")
        
        main_layout.addWidget(self.column_input)

        # Sorting ALgorithms eight button
        button_layout=QHBoxLayout()
        self.add_sorting_button(button_layout,"Insertion Sort",self.insertion_sort)
        self.add_sorting_button(button_layout,"Selection Sort",self.selection_sort)
        self.add_sorting_button(button_layout,"Bubble Sort",self.bubble_sort)
        self.add_sorting_button(button_layout,"Merge Sort",self.Merge_sort)
        self.add_sorting_button(button_layout,"Quick Sort ",self.Quick_sort)
        self.add_sorting_button(button_layout,"Counting Sort",self.counting_sort)
        self.add_sorting_button(button_layout,"Radix Sort",self.radix_sort)
        self.add_sorting_button(button_layout,"Bucket Sort",self.bucket_sort)
        main_layout.addLayout(button_layout)

        self.Button_reset=QPushButton("Reset")
        self.Button_reset.clicked.connect(self.reset)
        self.Button_reset.setFixedSize(100,40)
        self.Button_reset.setStyleSheet("""
                            QPushButton{
                                        font-size:23px;
                                        background-color:lightblue;
                                        border-radius:5px;
                                        }
                            QPushButton:hover{
                             background-color:#227ba8;
                             }
            """)
        main_layout.addWidget(self.Button_reset,alignment=Qt.AlignCenter)
     

        


    def add_sorting_button(self,layout,name,func):
        button=QPushButton(name)
        button.clicked.connect(func)
        button.setStyleSheet("""
                             QPushButton{
                              font-size: 18px;  
                              background-color:#5c5e5c;
                              border-radius:8px; 
                              color:white;  
                              padding:10px; 
                              margin:5px;
                             }
                             QPushButton:hover{
                             background-color:#3b3f4e;
                             }
        """)
        layout.addWidget(button)

    def load_data(self):
       
        for row_index,row_data in enumerate(data_list):
            for col_index,item in enumerate(row_data):
                self.table.setItem(row_index,col_index,QTableWidgetItem(str(item)))

      
            
    # When Insertion Button clicks ,Insertion Sorting Apply
    def insertion_sort(self):
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        insertionSort(data_list,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    # When selection Button clicks ,selection Sorting Apply
    def selection_sort(self):
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        selectionSort(data_list,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")
    
    # When bubble Button clicks ,bubble Sorting Apply
    def bubble_sort(self):

        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        bubbleSort(data_list,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def Merge_sort(self):
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        mergeSort(data_list,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def Quick_sort(self):
        global data_list
        column_Name=self.column_input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        data_list=sortQuick(data_list,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def counting_sort(self):
        column_Name=self.column_input.text().strip()
        if column_Name=="Title" or column_Name=="Image URL":
            self.time_Label.setText(f"* Counting Sort is not applicable for {column_Name} column *")
            self.time_Label.setStyleSheet("color:red;"
                                          "font-size:20px;"
                                          "font-weight:bold;"
                                      "padding-left:200;"
                                      "padding-top:20;")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        countingSort(data_list,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def radix_sort(self):
       
        column_Name=self.column_input.text().strip()
        if column_Name=="Title" or column_Name=="Image URL":
            self.time_Label.setText(f"* Radix Sort is not applicable for {column_Name} column *")
            self.time_Label.setStyleSheet("color:red;"
                                          "font-size:20px;"
                                          "font-weight:bold;"
                                      "padding-left:200;"
                                      "padding-top:20;")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        radixS(data_list,column_index)
      
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")

    def bucket_sort(self):
        global data_list
        column_Name=self.column_input.text().strip()
        if column_Name=="Title" or column_Name=="Image URL":
            self.time_Label.setText(f"* Bucket Sort is not applicable for {column_Name} column *")
            self.time_Label.setStyleSheet("color:red;"
                                          "font-size:20px;"
                                          "font-weight:bold;"
                                      "padding-left:200;"
                                      "padding-top:20;")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name")
            return
        start_time = time.time()
        data_list=bucket_sort(data_list,column_index)
        end_time=time.time()
        self.load_data()
        self.time_Label.setText(f"Sorting Time: {end_time-start_time}")
    
    def reset(self):
        global data_list
        df=pd.read_csv("data1.csv")
        data_list=df.values.tolist()
        self.load_data()
        self.time_Label.setText("Sorting Time: Not sorted yet")
        self.time_Label.setStyleSheet("color:gray;"
                                          "font-size:20px;"
                                          "font-weight:bold;"
                                      "padding-left:200;"
                                      "padding-top:20;")

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe=App()
    exe.show()
    sys.exit(app.exec_())
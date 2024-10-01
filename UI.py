import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QLabel, QSizePolicy, QHeaderView
from PyQt5.QtCore import Qt 
import pandas as pd



data_list=[]
df=pd.read_csv("Data.csv")
data_list=df.values.tolist()



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
                                      )
        main_layout.addWidget(self.time_Label)

        # create a table to display data
        self.table=QTableWidget()
        self.table.setRowCount(len(data_list))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['Brand',"Model","Price","Rating","Storage (GB)","Camera (MP)","Battery (mAh)"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
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
        # Sorting ALgorithms button
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
            
    
    def insertion_sort(self):
        pass
    def selection_sort(self):
        pass
    def bubble_sort(self):
        pass
    def Merge_sort(self):
        pass
    def Quick_sort(self):
        pass
    def counting_sort(self):
        pass
    def radix_sort(self):
        pass
    def bucket_sort(self):
        pass
    def reset():
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe=App()
    exe.show()
    sys.exit(app.exec_())
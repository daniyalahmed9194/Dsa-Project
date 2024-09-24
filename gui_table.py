import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QScrollBar
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
import csv

class SortingGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create heading label
        heading_label = QLabel("DSA")
        heading_label.setAlignment(Qt.AlignCenter)

        # Create buttons
        buttons_layout = QHBoxLayout()
        for i in range(8):
            button = QPushButton("Sort")
            buttons_layout.addWidget(button)

        # Create table widget to display CSV content
        self.table_widget = QTableWidget()

        # Load CSV file content and display it in the table
        self.load_csv_file("lp.csv")

        # Create scroll bar
        scroll_bar = QScrollBar(Qt.Vertical)

        # Create reset button
        reset_button = QPushButton("Reset")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(heading_label)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.table_widget)
        layout.addWidget(scroll_bar)
        layout.addWidget(reset_button)

        self.setLayout(layout)

    def load_csv_file(self, filename):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                csv_data = list(reader)  # Convert CSV reader object to a list

                # Set the number of rows and columns in the table widget
                self.table_widget.setRowCount(len(csv_data))
                self.table_widget.setColumnCount(len(csv_data[0]))

                # Loop through the data and set each cell in the table
                for row_idx, row_data in enumerate(csv_data):
                    for col_idx, col_data in enumerate(row_data):
                        self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(col_data))
        except FileNotFoundError:
            print("CSV file not found.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SortingGUI()
    gui.show()
    sys.exit(app.exec_())

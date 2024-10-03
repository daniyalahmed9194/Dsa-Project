
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
        self.sort_button = QPushButton("Sort")
        main_layout.addWidget(self.sort_button)
        main_layout.addWidget(self.column_input)

        # Sorting ALgorithms button
        button_layout=QHBoxLayout()
        self.add_sorting_button(button_layout,"Insertion Sort",self.insertion_sort)
        self.add_sorting_button(button_layout,"Selection Sort",self.selection_sort)
        self.add_sorting_button(button_layout,"Bubble Sort",self.bubble_sort)
        self.add_sorting_button(button_layout,"Merge Sort",self.Merge_sort)
        self.add_sorting_button(button_layout,"Quick Sort ",self.Quick_sort)
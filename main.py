import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel

class ListViewExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List View Example")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Select an item:")
        layout.addWidget(label)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Add items to the list widget
        for i in range(1, 11):
            self.list_widget.addItem(f"Item {i}")

        # Change the size of the list widget
        self.list_widget.setFixedSize(200, 150)  # Set fixed size
        # OR
        # self.list_widget.resize(200, 150)  # Explicitly resize

        # Connect item selection signal to slot
        self.list_widget.itemClicked.connect(self.on_item_selected)

    def on_item_selected(self, item):
        selected_item_text = item.text()
        print("Selected Item:", selected_item_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListViewExample()
    window.show()
    sys.exit(app.exec_())

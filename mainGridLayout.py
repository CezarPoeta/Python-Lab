import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from PySide6.QtGui import QColor

app = QApplication(sys.argv)
window = QMainWindow()

# Create a widget to hold the grid layout
grid_widget = QWidget()
grid = QGridLayout()
grid_widget.setLayout(grid)

# Create and add buttons to the grid
colors = [QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255), QColor(255, 255, 0),          QColor(0, 255, 255), QColor(255, 0, 255), QColor(255, 255, 255), QColor(0, 0, 0)]

for row in range(4):
    for col in range(4):
        button = QPushButton()
        button.setStyleSheet(f"background-color: {colors[row + col].name()};")
        grid.addWidget(button, row, col)

# Set the central widget of the main window to the grid widget
window.setCentralWidget(grid_widget)

# Show the main window
window.show()

sys.exit(app.exec_())

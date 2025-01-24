import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QHBoxLayout

class ImageGallery(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Gallery Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Initialize variables
        self.image_folder = None
        self.image_files = []
        self.current_index = 0

        # Set up GUI layout
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a layout
        layout = QVBoxLayout()

        # Create an image display label
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Updated for PyQt6
        layout.addWidget(self.image_label)

        # Create navigation buttons
        navigation_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous", self)
        self.next_button = QPushButton("Next", self)

        navigation_layout.addWidget(self.prev_button)
        navigation_layout.addWidget(self.next_button)

        layout.addLayout(navigation_layout)

        # Connect buttons to functions
        self.prev_button.clicked.connect(self.show_prev_image)
        self.next_button.clicked.connect(self.show_next_image)

        # Add "Open Folder" button
        self.open_button = QPushButton("Open Folder", self)
        self.open_button.clicked.connect(self.open_folder)
        layout.addWidget(self.open_button)

        self.central_widget.setLayout(layout)

    def open_folder(self):
        # Open folder and get list of image files
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.image_folder = folder
            self.image_files = [f for f in os.listdir(folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
            self.current_index = 0
            self.show_image()

    def show_image(self):
        if self.image_files:
            # Load and display the current image
            image_path = os.path.join(self.image_folder, self.image_files[self.current_index])
            pixmap = QPixmap(image_path)

            # Resize to fit in the window
            pixmap = pixmap.scaled(600, 400, Qt.AspectRatioMode.KeepAspectRatio)

            self.image_label.setPixmap(pixmap)

    def show_next_image(self):
        if self.image_files and self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            self.show_image()

    def show_prev_image(self):
        if self.image_files and self.current_index > 0:
            self.current_index -= 1
            self.show_image()


if __name__ == '__main__':
    app = QApplication([])
    gallery = ImageGallery()
    gallery.show()
    app.exec()

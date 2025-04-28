import sys
import pymysql
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from com.yootk import mysql_connection


class BookApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.books = self.load_books()  # 先加载图书信息
        self.initUI()

    def initUI(self):
        self.setWindowTitle('图书信息展示')
        self.setGeometry(100, 100, 1200, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # 创建QTableWidget
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # 设置表头
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['书名', '作者', '出版机构', '资源下载', '图书照片'])

        # 设置行数
        self.table_widget.setRowCount(len(self.books))

        # 填充数据
        for row, book in enumerate(self.books):
            self.table_widget.setItem(row, 0, QTableWidgetItem(book['name']))
            self.table_widget.setItem(row, 1, QTableWidgetItem(book['author']))
            self.table_widget.setItem(row, 2, QTableWidgetItem(book['agency']))
            self.table_widget.setItem(row, 3, QTableWidgetItem(book['resource']))

            # 添加图书图片
            self.table_widget.setCellWidget(row, 4, self.create_label_with_pixmap(book['img']))

    def create_label_with_pixmap(self, img_name):
        label = QLabel()
        img_path = f"book_images/{img_name}"
        pixmap = QPixmap(img_path)
        label.setPixmap(pixmap.scaled(100, 150, Qt.KeepAspectRatio))  # 调整图片大小
        return label

    def load_books(self):
        conn = mysql_connection.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM book")
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return books


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BookApp()
    ex.show()
    sys.exit(app.exec_())

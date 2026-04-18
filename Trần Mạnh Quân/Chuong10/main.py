import re
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load trực tiếp file .ui
        uic.loadUi("main.ui", self)

        self.populateDateFields()
        self.btnRegister.clicked.connect(self.handleRegister)

    def populateDateFields(self):
        self.cbDay.addItem("Ngày")
        for d in range(1, 32):
            self.cbDay.addItem(str(d))

        self.cbMonth.addItem("Tháng")
        for m in range(1, 13):
            self.cbMonth.addItem(str(m))

        self.cbYear.addItem("Năm")
        for y in range(2026, 1899, -1):
            self.cbYear.addItem(str(y))

    def handleRegister(self):
        ho = self.txtHo.toPlainText().strip()
        ten = self.txtTen.toPlainText().strip()
        contact = self.txtContact.toPlainText().strip()
        password = self.txtPassword.toPlainText()
        ngay = self.cbDay.currentText().strip()
        thang = self.cbMonth.currentText().strip()
        nam = self.cbYear.currentText().strip()
        gender = "Nam" if self.rdNam.isChecked() else "Nữ" if self.rdNu.isChecked() else ""
        agreed = self.chkAgree.isChecked()

        if not ho:
            return self.showMessage("Vui lòng nhập Họ.")
        if not ten:
            return self.showMessage("Vui lòng nhập Tên.")
        if not contact:
            return self.showMessage("Vui lòng nhập Email hoặc Số điện thoại.")
        if not password:
            return self.showMessage("Vui lòng nhập Mật khẩu.")
        if not gender:
            return self.showMessage("Vui lòng chọn Giới tính.")
        if not agreed:
            return self.showMessage("Vui lòng tích vào 'Tôi đồng ý với các điều khoản'.")

        if not self.validatePassword(password):
            return self.showMessage(
                "Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ thường, chữ hoa, số và ký tự đặc biệt."
            )

        if self.cbDay.currentIndex() <= 0 or self.cbMonth.currentIndex() <= 0 or self.cbYear.currentIndex() <= 0:
            return self.showMessage("Vui lòng chọn đầy đủ Ngày sinh.")

        self.showMessage(
            f"Đăng ký thành công!\n\nHọ: {ho}\nTên: {ten}\nLiên hệ: {contact}\nGiới tính: {gender}\nNgày sinh: {ngay}/{thang}/{nam}",
            info=True,
        )

    def validatePassword(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[^A-Za-z0-9]", password):
            return False
        return True

    def showMessage(self, message: str, info: bool = False):
        title = "Thành công" if info else "Lỗi"
        if info:
            QMessageBox.information(self, title, message)
        else:
            QMessageBox.warning(self, title, message)

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())
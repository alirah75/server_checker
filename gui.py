import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import uuid

from PyQt5.QtWidgets import QMessageBox

from multithreading import main_loop
from worker_thread import WorkerThread


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(782, 350)

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 284))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.serverAdDressLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.serverAdDressLabel.setObjectName("serverAdDressLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.serverAdDressLabel)
        self.serverAdDressLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.serverAdDressLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.serverAdDressLineEdit.setMaximumSize(QtCore.QSize(600, 16777215))
        self.serverAdDressLineEdit.setObjectName("serverAdDressLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.serverAdDressLineEdit)
        self.startDateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.startDateLabel.setObjectName("startDateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.startDateLabel)
        self.startDateEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.startDateEdit.setMaximumSize(QtCore.QSize(167, 16777215))
        self.startDateEdit.setDate(QtCore.QDate(2024, 9, 14))
        self.startDateEdit.setMinimumDate(QtCore.QDate(2024, 1, 1))
        self.startDateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setObjectName("startDateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startDateEdit)
        self.endDateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.endDateLabel.setObjectName("endDateLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.endDateLabel)
        self.endDateEdit = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.endDateEdit.setMaximumSize(QtCore.QSize(167, 16777215))
        self.endDateEdit.setDate(QtCore.QDate(2024, 9, 14))
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setObjectName("endDateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.endDateEdit)
        self.intervalMinutesLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.intervalMinutesLabel.setObjectName("intervalMinutesLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.intervalMinutesLabel)
        self.intervalMinutesLineEdit = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.intervalMinutesLineEdit.setMaximumSize(QtCore.QSize(167, 16777215))
        self.intervalMinutesLineEdit.setProperty("value", 5)
        self.intervalMinutesLineEdit.setObjectName("intervalMinutesLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.intervalMinutesLineEdit)
        self.secondIntervalMinutesLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.secondIntervalMinutesLabel.setObjectName("secondIntervalMinutesLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.secondIntervalMinutesLabel)
        self.secondIntervalMinutesLineEdit = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.secondIntervalMinutesLineEdit.setMaximumSize(QtCore.QSize(167, 16777215))
        self.secondIntervalMinutesLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.secondIntervalMinutesLineEdit.setProperty("value", 2)
        self.secondIntervalMinutesLineEdit.setObjectName("secondIntervalMinutesLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.secondIntervalMinutesLineEdit)
        self.optionsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.optionsLabel.setObjectName("optionsLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.optionsLabel)
        self.optionsLayout = QtWidgets.QHBoxLayout()
        self.optionsLayout.setObjectName("optionsLayout")
        self.optionCheckBox1 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.optionCheckBox1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.optionCheckBox1.setObjectName("optionCheckBox1")
        self.optionsLayout.addWidget(self.optionCheckBox1)
        self.optionCheckBox2 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.optionCheckBox2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.optionCheckBox2.setObjectName("optionCheckBox2")
        self.optionsLayout.addWidget(self.optionCheckBox2)
        self.optionCheckBox3 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.optionCheckBox3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.optionCheckBox3.setObjectName("optionCheckBox3")
        self.optionsLayout.addWidget(self.optionCheckBox3)
        self.optionCheckBox4 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.optionCheckBox4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.optionCheckBox4.setObjectName("optionCheckBox4")
        self.optionsLayout.addWidget(self.optionCheckBox4)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.optionsLayout)
        self.formLayout_2 = QtWidgets.QHBoxLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_2.addWidget(self.pushButton_3)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.formLayout_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 300, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Server Checker"))
        self.serverAdDressLabel.setText(_translate("Dialog", "Server Address"))
        self.startDateLabel.setText(_translate("Dialog", "Start Date"))
        self.startDateEdit.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd h:mm AP"))
        self.endDateLabel.setText(_translate("Dialog", "End Date"))
        self.endDateEdit.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd h:mm AP"))
        self.intervalMinutesLabel.setText(_translate("Dialog", "Interval Minutes"))
        self.secondIntervalMinutesLabel.setText(_translate("Dialog", "Second Interval Minutes"))
        self.optionsLabel.setText(_translate("Dialog", "Options"))
        self.optionCheckBox1.setText(_translate("Dialog", "GetPing"))
        self.optionCheckBox2.setText(_translate("Dialog", "GetStatus"))
        self.optionCheckBox3.setText(_translate("Dialog", "GetLoadTime"))
        self.optionCheckBox4.setText(_translate("Dialog", "All"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "Stop"))
        self.pushButton_3.setText(_translate("Dialog", "NewProject"))
        self.label.setText(_translate("Dialog", "Server Checker"))


class MainApp(QtWidgets.QDialog, Ui_Dialog):
    open_forms = 0
    max_forms = 10
    form_list = []

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        self.worker_thread = None
        self.pushButton.clicked.connect(self.start_thread)
        self.pushButton_2.clicked.connect(self.stop_thread)

        # self.pushButton.clicked.connect(self.sendData)
        # self.pushButton_2.clicked.connect(self.sendFormID)
        self.pushButton_3.clicked.connect(self.create_new_project)

        self.form_id = str(uuid.uuid4())
        self.setWindowTitle(f"Server Checker - {self.form_id}")

    def start_thread(self):
        start_date = self.startDateEdit.dateTime().date().toString("yyyy-MM-dd")
        start_time = self.startDateEdit.dateTime().time().toString("HH:mm")
        end_date = self.endDateEdit.dateTime().date().toString("yyyy-MM-dd")
        end_time = self.endDateEdit.dateTime().time().toString("HH:mm")

        interval_minutes = self.intervalMinutesLineEdit.value()

        second_interval_minutes = self.secondIntervalMinutesLineEdit.value()

        target_address = self.serverAdDressLineEdit.text()

        selected_functions = []
        if self.optionCheckBox1.isChecked():
            selected_functions.append("GetPing")
        if self.optionCheckBox2.isChecked():
            selected_functions.append("GetStatus")
        if self.optionCheckBox3.isChecked():
            selected_functions.append("GetLoadTime")
        if self.optionCheckBox4.isChecked():
            selected_functions.append("All")

        if not selected_functions:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select at least one option.")
            return

        self.worker_thread = WorkerThread(start_date, end_date, start_time, end_time, interval_minutes, second_interval_minutes,
                                          target_address, selected_functions)
        self.worker_thread.log_signal.connect(self.update_log)
        self.worker_thread.start()

    def stop_thread(self):
        if self.worker_thread:
            self.worker_thread.stop()
            self.worker_thread.wait()

    def create_new_project(self):
        if MainApp.open_forms < MainApp.max_forms:
            new_form = MainApp()
            MainApp.form_list.append(new_form)
            MainApp.open_forms += 1
            new_form.show()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Maximum number of forms already open.")

    def update_log(self, message):
        QMessageBox.information(self, "Log", message)

    # def sendData(self):
    #     server_address = self.serverAdDressLineEdit.text()
    #     start_date = self.startDateEdit.dateTime().toString(QtCore.Qt.ISODate)
    #     end_date = self.endDateEdit.dateTime().toString(QtCore.Qt.ISODate)
    #     interval_minutes = self.intervalMinutesLineEdit.value()
    #     second_interval_minutes = self.secondIntervalMinutesLineEdit.value()
    #
    #     options = []
    #     for i in range(self.optionsLayout.count()):
    #         checkbox = self.optionsLayout.itemAt(i).widget()
    #         if isinstance(checkbox, QtWidgets.QCheckBox) and checkbox.isChecked():
    #             options.append(checkbox.text())
    #
    #     if not options:
    #         QtWidgets.QMessageBox.warning(self, "Warning", "Please select at least one option.")
    #         return
    #
    #     print("Form ID:", self.form_id)
    #     print("Server Address:", server_address)
    #     print("Start Date:", start_date)
    #     print("End Date:", end_date)
    #     print("Interval Minutes:", interval_minutes)
    #     print("Second Interval Minutes:", second_interval_minutes)
    #     print("Options:", options)

    # def sendFormID(self):
    #     print("Form ID:", self.form_id)
    #     self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MeterDialog.ui'
#
# Created: Thu Oct 13 07:00:50 2016
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MeterDialog(object):
    def setupUi(self, MeterDialog):
        MeterDialog.setObjectName(_fromUtf8("MeterDialog"))
        MeterDialog.resize(588, 575)
        MeterDialog.setMinimumSize(QtCore.QSize(588, 450))
        MeterDialog.setMaximumSize(QtCore.QSize(588, 640))
        self.buttonBox = QtGui.QDialogButtonBox(MeterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(405, 540, 166, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(MeterDialog)
        self.tabWidget.setGeometry(QtCore.QRect(15, 10, 556, 521))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.meter_number_edit = QtGui.QLineEdit(self.tab)
        self.meter_number_edit.setGeometry(QtCore.QRect(27, 30, 196, 20))
        self.meter_number_edit.setObjectName(_fromUtf8("meter_number_edit"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(27, 15, 126, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(265, 135, 126, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.inspection_intervall_unit_cbox = QtGui.QComboBox(self.tab)
        self.inspection_intervall_unit_cbox.setGeometry(QtCore.QRect(265, 70, 196, 22))
        self.inspection_intervall_unit_cbox.setObjectName(_fromUtf8("inspection_intervall_unit_cbox"))
        self.plot_no_edit = QtGui.QLineEdit(self.tab)
        self.plot_no_edit.setGeometry(QtCore.QRect(25, 150, 196, 20))
        self.plot_no_edit.setObjectName(_fromUtf8("plot_no_edit"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(265, 335, 126, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.district_edit = QtGui.QLineEdit(self.tab)
        self.district_edit.setGeometry(QtCore.QRect(25, 190, 196, 20))
        self.district_edit.setObjectName(_fromUtf8("district_edit"))
        self.street_edit = QtGui.QLineEdit(self.tab)
        self.street_edit.setGeometry(QtCore.QRect(25, 310, 196, 20))
        self.street_edit.setText(_fromUtf8(""))
        self.street_edit.setObjectName(_fromUtf8("street_edit"))
        self.label_21 = QtGui.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(265, 175, 126, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.ward_edit = QtGui.QLineEdit(self.tab)
        self.ward_edit.setGeometry(QtCore.QRect(25, 270, 196, 20))
        self.ward_edit.setText(_fromUtf8(""))
        self.ward_edit.setObjectName(_fromUtf8("ward_edit"))
        self.label_14 = QtGui.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(265, 295, 126, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.installation_date_chbox = QtGui.QCheckBox(self.tab)
        self.installation_date_chbox.setGeometry(QtCore.QRect(25, 355, 26, 17))
        self.installation_date_chbox.setText(_fromUtf8(""))
        self.installation_date_chbox.setObjectName(_fromUtf8("installation_date_chbox"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(25, 335, 126, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.date_of_first_use_chbox = QtGui.QCheckBox(self.tab)
        self.date_of_first_use_chbox.setGeometry(QtCore.QRect(25, 405, 26, 17))
        self.date_of_first_use_chbox.setText(_fromUtf8(""))
        self.date_of_first_use_chbox.setObjectName(_fromUtf8("date_of_first_use_chbox"))
        self.network_cbox = QtGui.QComboBox(self.tab)
        self.network_cbox.setGeometry(QtCore.QRect(265, 350, 196, 22))
        self.network_cbox.setObjectName(_fromUtf8("network_cbox"))
        self.label_22 = QtGui.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(25, 385, 126, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.date_of_last_inspection_chbox = QtGui.QCheckBox(self.tab)
        self.date_of_last_inspection_chbox.setGeometry(QtCore.QRect(265, 115, 26, 17))
        self.date_of_last_inspection_chbox.setText(_fromUtf8(""))
        self.date_of_last_inspection_chbox.setObjectName(_fromUtf8("date_of_last_inspection_chbox"))
        self.inspection_intervall_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.inspection_intervall_sbox.setGeometry(QtCore.QRect(265, 30, 196, 22))
        self.inspection_intervall_sbox.setObjectName(_fromUtf8("inspection_intervall_sbox"))
        self.date_of_last_inspection_edit = QtGui.QDateEdit(self.tab)
        self.date_of_last_inspection_edit.setEnabled(False)
        self.date_of_last_inspection_edit.setGeometry(QtCore.QRect(290, 110, 171, 22))
        self.date_of_last_inspection_edit.setCalendarPopup(True)
        self.date_of_last_inspection_edit.setObjectName(_fromUtf8("date_of_last_inspection_edit"))
        self.label_13 = QtGui.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(265, 95, 126, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.status_change_date_edit = QtGui.QDateEdit(self.tab)
        self.status_change_date_edit.setEnabled(False)
        self.status_change_date_edit.setGeometry(QtCore.QRect(290, 190, 171, 22))
        self.status_change_date_edit.setCalendarPopup(True)
        self.status_change_date_edit.setObjectName(_fromUtf8("status_change_date_edit"))
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(25, 255, 141, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.operating_state_cbox = QtGui.QComboBox(self.tab)
        self.operating_state_cbox.setGeometry(QtCore.QRect(265, 150, 196, 22))
        self.operating_state_cbox.setObjectName(_fromUtf8("operating_state_cbox"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(25, 55, 216, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.installation_date_edit = QtGui.QDateEdit(self.tab)
        self.installation_date_edit.setEnabled(False)
        self.installation_date_edit.setGeometry(QtCore.QRect(50, 350, 171, 22))
        self.installation_date_edit.setCalendarPopup(True)
        self.installation_date_edit.setObjectName(_fromUtf8("installation_date_edit"))
        self.height_sbox = QtGui.QDoubleSpinBox(self.tab)
        self.height_sbox.setGeometry(QtCore.QRect(265, 310, 196, 22))
        self.height_sbox.setMinimum(-100.0)
        self.height_sbox.setMaximum(2000.0)
        self.height_sbox.setObjectName(_fromUtf8("height_sbox"))
        self.label_20 = QtGui.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(25, 295, 141, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(25, 135, 141, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(265, 15, 126, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(25, 175, 141, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.status_change_date_chbox = QtGui.QCheckBox(self.tab)
        self.status_change_date_chbox.setGeometry(QtCore.QRect(265, 195, 26, 17))
        self.status_change_date_chbox.setText(_fromUtf8(""))
        self.status_change_date_chbox.setObjectName(_fromUtf8("status_change_date_chbox"))
        self.date_of_first_use_edit = QtGui.QDateEdit(self.tab)
        self.date_of_first_use_edit.setEnabled(False)
        self.date_of_first_use_edit.setGeometry(QtCore.QRect(50, 400, 171, 22))
        self.date_of_first_use_edit.setCalendarPopup(True)
        self.date_of_first_use_edit.setObjectName(_fromUtf8("date_of_first_use_edit"))
        self.label_18 = QtGui.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(25, 215, 141, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(265, 55, 126, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.meter_class_cbox = QtGui.QComboBox(self.tab)
        self.meter_class_cbox.setGeometry(QtCore.QRect(265, 230, 196, 22))
        self.meter_class_cbox.setObjectName(_fromUtf8("meter_class_cbox"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(265, 215, 126, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.meter_type_cbox = QtGui.QComboBox(self.tab)
        self.meter_type_cbox.setGeometry(QtCore.QRect(265, 270, 196, 22))
        self.meter_type_cbox.setObjectName(_fromUtf8("meter_type_cbox"))
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(265, 255, 126, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.zone_edit = QtGui.QLineEdit(self.tab)
        self.zone_edit.setGeometry(QtCore.QRect(25, 230, 196, 20))
        self.zone_edit.setObjectName(_fromUtf8("zone_edit"))
        self.view_maxcom_button = QtGui.QPushButton(self.tab)
        self.view_maxcom_button.setGeometry(QtCore.QRect(195, 100, 25, 25))
        self.view_maxcom_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_maxcom_button.setIcon(icon)
        self.view_maxcom_button.setObjectName(_fromUtf8("view_maxcom_button"))
        self.verify_button = QtGui.QPushButton(self.tab)
        self.verify_button.setGeometry(QtCore.QRect(160, 100, 25, 25))
        self.verify_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/wnt/verify.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.verify_button.setIcon(icon1)
        self.verify_button.setObjectName(_fromUtf8("verify_button"))
        self.control_no_sbox = QtGui.QSpinBox(self.tab)
        self.control_no_sbox.setGeometry(QtCore.QRect(25, 70, 196, 22))
        self.control_no_sbox.setMinimum(-1)
        self.control_no_sbox.setMaximum(8000000)
        self.control_no_sbox.setProperty("value", -1)
        self.control_no_sbox.setObjectName(_fromUtf8("control_no_sbox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(MeterDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MeterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MeterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MeterDialog)
        MeterDialog.setTabOrder(self.tabWidget, self.meter_number_edit)
        MeterDialog.setTabOrder(self.meter_number_edit, self.control_no_sbox)
        MeterDialog.setTabOrder(self.control_no_sbox, self.verify_button)
        MeterDialog.setTabOrder(self.verify_button, self.view_maxcom_button)
        MeterDialog.setTabOrder(self.view_maxcom_button, self.plot_no_edit)
        MeterDialog.setTabOrder(self.plot_no_edit, self.district_edit)
        MeterDialog.setTabOrder(self.district_edit, self.zone_edit)
        MeterDialog.setTabOrder(self.zone_edit, self.ward_edit)
        MeterDialog.setTabOrder(self.ward_edit, self.street_edit)
        MeterDialog.setTabOrder(self.street_edit, self.installation_date_chbox)
        MeterDialog.setTabOrder(self.installation_date_chbox, self.installation_date_edit)
        MeterDialog.setTabOrder(self.installation_date_edit, self.date_of_first_use_chbox)
        MeterDialog.setTabOrder(self.date_of_first_use_chbox, self.date_of_first_use_edit)
        MeterDialog.setTabOrder(self.date_of_first_use_edit, self.inspection_intervall_sbox)
        MeterDialog.setTabOrder(self.inspection_intervall_sbox, self.inspection_intervall_unit_cbox)
        MeterDialog.setTabOrder(self.inspection_intervall_unit_cbox, self.date_of_last_inspection_chbox)
        MeterDialog.setTabOrder(self.date_of_last_inspection_chbox, self.date_of_last_inspection_edit)
        MeterDialog.setTabOrder(self.date_of_last_inspection_edit, self.operating_state_cbox)
        MeterDialog.setTabOrder(self.operating_state_cbox, self.status_change_date_chbox)
        MeterDialog.setTabOrder(self.status_change_date_chbox, self.status_change_date_edit)
        MeterDialog.setTabOrder(self.status_change_date_edit, self.meter_class_cbox)
        MeterDialog.setTabOrder(self.meter_class_cbox, self.meter_type_cbox)
        MeterDialog.setTabOrder(self.meter_type_cbox, self.height_sbox)
        MeterDialog.setTabOrder(self.height_sbox, self.network_cbox)
        MeterDialog.setTabOrder(self.network_cbox, self.buttonBox)

    def retranslateUi(self, MeterDialog):
        MeterDialog.setWindowTitle(_translate("MeterDialog", "Add / Edit Meter", None))
        self.label.setText(_translate("MeterDialog", "Meter Number", None))
        self.label_7.setText(_translate("MeterDialog", "Operating State", None))
        self.label_15.setText(_translate("MeterDialog", "Network", None))
        self.label_21.setText(_translate("MeterDialog", "Date of Status Change", None))
        self.label_14.setText(_translate("MeterDialog", "Height [m]", None))
        self.label_3.setText(_translate("MeterDialog", "Installation Date", None))
        self.label_22.setText(_translate("MeterDialog", "Date of First Use", None))
        self.date_of_last_inspection_edit.setDisplayFormat(_translate("MeterDialog", "yyyy-MM-dd", None))
        self.label_13.setText(_translate("MeterDialog", "Date of Last Inspection", None))
        self.status_change_date_edit.setDisplayFormat(_translate("MeterDialog", "yyyy-MM-dd", None))
        self.label_19.setText(_translate("MeterDialog", "Ward", None))
        self.label_2.setText(_translate("MeterDialog", "Application Control No. (from MAXCOM)", None))
        self.installation_date_edit.setDisplayFormat(_translate("MeterDialog", "yyyy-MM-dd", None))
        self.label_20.setText(_translate("MeterDialog", "Street", None))
        self.label_16.setText(_translate("MeterDialog", "Plot Number", None))
        self.label_5.setText(_translate("MeterDialog", "Inspection Interval", None))
        self.label_17.setText(_translate("MeterDialog", "District", None))
        self.date_of_first_use_edit.setDisplayFormat(_translate("MeterDialog", "yyyy-MM-dd", None))
        self.label_18.setText(_translate("MeterDialog", "Zone", None))
        self.label_6.setText(_translate("MeterDialog", "Inspection Interval Unit", None))
        self.label_9.setText(_translate("MeterDialog", "Meter Class", None))
        self.label_10.setText(_translate("MeterDialog", "Meter Type", None))
        self.view_maxcom_button.setToolTip(_translate("MeterDialog", "View Application Details at MAXCOM", None))
        self.verify_button.setToolTip(_translate("MeterDialog", "Verify Control Number", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MeterDialog", "Description", None))

import resources_rc

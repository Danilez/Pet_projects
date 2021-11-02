################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 600)
        MainWindow.setMinimumSize(QSize(300, 600))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Zen Kaku Gothic New Light;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"color: #888;")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"color: #888;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"color: #888;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"color: #888;")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setStyleSheet(u"color: #888;")
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.lineEdit.setMaxLength(24)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.grid_options = QGridLayout()
        self.grid_options.setObjectName(u"grid_options")
        self.btn_circle_r = QPushButton(self.centralwidget)
        self.btn_circle_r.setObjectName(u"btn_circle_r")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_circle_r.sizePolicy().hasHeightForWidth())
        self.btn_circle_r.setSizePolicy(sizePolicy2)
        self.btn_circle_r.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_circle_r.setStyleSheet(u"font-size: 12pt;")
        self.btn_circle_r.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_circle_r, 1, 1, 1, 1)

        self.btn_e2 = QPushButton(self.centralwidget)
        self.btn_e2.setObjectName(u"btn_e2")
        sizePolicy2.setHeightForWidth(self.btn_e2.sizePolicy().hasHeightForWidth())
        self.btn_e2.setSizePolicy(sizePolicy2)
        self.btn_e2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_e2.setStyleSheet(u"font-size: 12pt;")
        self.btn_e2.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_e2, 3, 3, 1, 1)

        self.btn_es3 = QPushButton(self.centralwidget)
        self.btn_es3.setObjectName(u"btn_es3")
        sizePolicy2.setHeightForWidth(self.btn_es3.sizePolicy().hasHeightForWidth())
        self.btn_es3.setSizePolicy(sizePolicy2)
        self.btn_es3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_es3.setStyleSheet(u"font-size: 12pt;")
        self.btn_es3.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_es3, 3, 1, 1, 1)

        self.btn_ln = QPushButton(self.centralwidget)
        self.btn_ln.setObjectName(u"btn_ln")
        sizePolicy2.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy2)
        self.btn_ln.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ln.setStyleSheet(u"font-size: 12pt;")
        self.btn_ln.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_ln, 2, 0, 1, 1)

        self.btn_es2 = QPushButton(self.centralwidget)
        self.btn_es2.setObjectName(u"btn_es2")
        sizePolicy2.setHeightForWidth(self.btn_es2.sizePolicy().hasHeightForWidth())
        self.btn_es2.setSizePolicy(sizePolicy2)
        self.btn_es2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_es2.setStyleSheet(u"font-size: 12pt;")
        self.btn_es2.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_es2, 3, 0, 1, 1)

        self.btn_circle_d = QPushButton(self.centralwidget)
        self.btn_circle_d.setObjectName(u"btn_circle_d")
        sizePolicy2.setHeightForWidth(self.btn_circle_d.sizePolicy().hasHeightForWidth())
        self.btn_circle_d.setSizePolicy(sizePolicy2)
        self.btn_circle_d.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_circle_d.setStyleSheet(u"font-size: 12pt;")
        self.btn_circle_d.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_circle_d, 1, 0, 1, 1)

        self.btn_mean = QPushButton(self.centralwidget)
        self.btn_mean.setObjectName(u"btn_mean")
        sizePolicy2.setHeightForWidth(self.btn_mean.sizePolicy().hasHeightForWidth())
        self.btn_mean.setSizePolicy(sizePolicy2)
        self.btn_mean.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_mean.setStyleSheet(u"font-size: 12pt;")
        self.btn_mean.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_mean, 1, 4, 1, 1)

        self.btn_abs = QPushButton(self.centralwidget)
        self.btn_abs.setObjectName(u"btn_abs")
        sizePolicy2.setHeightForWidth(self.btn_abs.sizePolicy().hasHeightForWidth())
        self.btn_abs.setSizePolicy(sizePolicy2)
        self.btn_abs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_abs.setStyleSheet(u"font-size: 12pt;")
        self.btn_abs.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_abs, 4, 1, 1, 1)

        self.btn_median = QPushButton(self.centralwidget)
        self.btn_median.setObjectName(u"btn_median")
        sizePolicy2.setHeightForWidth(self.btn_median.sizePolicy().hasHeightForWidth())
        self.btn_median.setSizePolicy(sizePolicy2)
        self.btn_median.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_median.setStyleSheet(u"font-size: 12pt;")
        self.btn_median.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_median, 1, 5, 1, 1)

        self.btn_e1 = QPushButton(self.centralwidget)
        self.btn_e1.setObjectName(u"btn_e1")
        sizePolicy2.setHeightForWidth(self.btn_e1.sizePolicy().hasHeightForWidth())
        self.btn_e1.setSizePolicy(sizePolicy2)
        self.btn_e1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_e1.setStyleSheet(u"font-size: 12pt;")
        self.btn_e1.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_e1, 4, 0, 1, 1)

        self.btn_asin = QPushButton(self.centralwidget)
        self.btn_asin.setObjectName(u"btn_asin")
        sizePolicy2.setHeightForWidth(self.btn_asin.sizePolicy().hasHeightForWidth())
        self.btn_asin.setSizePolicy(sizePolicy2)
        self.btn_asin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_asin.setStyleSheet(u"font-size: 12pt;")
        self.btn_asin.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_asin, 4, 2, 1, 1)

        self.btn_atan = QPushButton(self.centralwidget)
        self.btn_atan.setObjectName(u"btn_atan")
        sizePolicy2.setHeightForWidth(self.btn_atan.sizePolicy().hasHeightForWidth())
        self.btn_atan.setSizePolicy(sizePolicy2)
        self.btn_atan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_atan.setStyleSheet(u"font-size: 12pt;")
        self.btn_atan.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_atan, 4, 4, 1, 1)

        self.btn_tan = QPushButton(self.centralwidget)
        self.btn_tan.setObjectName(u"btn_tan")
        sizePolicy2.setHeightForWidth(self.btn_tan.sizePolicy().hasHeightForWidth())
        self.btn_tan.setSizePolicy(sizePolicy2)
        self.btn_tan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tan.setStyleSheet(u"font-size: 12pt;")
        self.btn_tan.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_tan, 5, 4, 1, 1)

        self.btn_acos = QPushButton(self.centralwidget)
        self.btn_acos.setObjectName(u"btn_acos")
        sizePolicy2.setHeightForWidth(self.btn_acos.sizePolicy().hasHeightForWidth())
        self.btn_acos.setSizePolicy(sizePolicy2)
        self.btn_acos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_acos.setStyleSheet(u"font-size: 12pt;")
        self.btn_acos.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_acos, 4, 3, 1, 1)

        self.btn_bracket_close = QPushButton(self.centralwidget)
        self.btn_bracket_close.setObjectName(u"btn_bracket_close")
        sizePolicy2.setHeightForWidth(self.btn_bracket_close.sizePolicy().hasHeightForWidth())
        self.btn_bracket_close.setSizePolicy(sizePolicy2)
        self.btn_bracket_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bracket_close.setStyleSheet(u"font-size: 12pt;")
        self.btn_bracket_close.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_bracket_close, 5, 1, 1, 1)

        self.btn_log = QPushButton(self.centralwidget)
        self.btn_log.setObjectName(u"btn_log")
        sizePolicy2.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy2)
        self.btn_log.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_log.setStyleSheet(u"font-size: 12pt;")
        self.btn_log.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_log, 2, 2, 1, 1)

        self.btn_min = QPushButton(self.centralwidget)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy2.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy2)
        self.btn_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_min.setStyleSheet(u"font-size: 12pt;")
        self.btn_min.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_min, 1, 2, 1, 1)

        self.btn_esy = QPushButton(self.centralwidget)
        self.btn_esy.setObjectName(u"btn_esy")
        sizePolicy2.setHeightForWidth(self.btn_esy.sizePolicy().hasHeightForWidth())
        self.btn_esy.setSizePolicy(sizePolicy2)
        self.btn_esy.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_esy.setStyleSheet(u"font-size: 12pt;")
        self.btn_esy.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_esy, 3, 2, 1, 1)

        self.btn_pi = QPushButton(self.centralwidget)
        self.btn_pi.setObjectName(u"btn_pi")
        sizePolicy2.setHeightForWidth(self.btn_pi.sizePolicy().hasHeightForWidth())
        self.btn_pi.setSizePolicy(sizePolicy2)
        self.btn_pi.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pi.setStyleSheet(u"font-size: 12pt;")
        self.btn_pi.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_pi, 2, 5, 1, 1)

        self.btn_lg = QPushButton(self.centralwidget)
        self.btn_lg.setObjectName(u"btn_lg")
        sizePolicy2.setHeightForWidth(self.btn_lg.sizePolicy().hasHeightForWidth())
        self.btn_lg.setSizePolicy(sizePolicy2)
        self.btn_lg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lg.setStyleSheet(u"font-size: 12pt;")
        self.btn_lg.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_lg, 2, 1, 1, 1)

        self.btn_max = QPushButton(self.centralwidget)
        self.btn_max.setObjectName(u"btn_max")
        sizePolicy2.setHeightForWidth(self.btn_max.sizePolicy().hasHeightForWidth())
        self.btn_max.setSizePolicy(sizePolicy2)
        self.btn_max.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_max.setStyleSheet(u"font-size: 12pt;")
        self.btn_max.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_max, 1, 3, 1, 1)

        self.btn_cos = QPushButton(self.centralwidget)
        self.btn_cos.setObjectName(u"btn_cos")
        sizePolicy2.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy2)
        self.btn_cos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cos.setStyleSheet(u"font-size: 12pt;")
        self.btn_cos.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_cos, 5, 3, 1, 1)

        self.btn_actan = QPushButton(self.centralwidget)
        self.btn_actan.setObjectName(u"btn_actan")
        sizePolicy2.setHeightForWidth(self.btn_actan.sizePolicy().hasHeightForWidth())
        self.btn_actan.setSizePolicy(sizePolicy2)
        self.btn_actan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_actan.setStyleSheet(u"font-size: 12pt;")
        self.btn_actan.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_actan, 4, 5, 1, 1)

        self.btn_exp_x = QPushButton(self.centralwidget)
        self.btn_exp_x.setObjectName(u"btn_exp_x")
        sizePolicy2.setHeightForWidth(self.btn_exp_x.sizePolicy().hasHeightForWidth())
        self.btn_exp_x.setSizePolicy(sizePolicy2)
        self.btn_exp_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exp_x.setStyleSheet(u"font-size: 12pt;")
        self.btn_exp_x.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_exp_x, 2, 3, 1, 1)

        self.btn_e3 = QPushButton(self.centralwidget)
        self.btn_e3.setObjectName(u"btn_e3")
        sizePolicy2.setHeightForWidth(self.btn_e3.sizePolicy().hasHeightForWidth())
        self.btn_e3.setSizePolicy(sizePolicy2)
        self.btn_e3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_e3.setStyleSheet(u"font-size: 12pt;")
        self.btn_e3.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_e3, 3, 4, 1, 1)

        self.btn_ctan = QPushButton(self.centralwidget)
        self.btn_ctan.setObjectName(u"btn_ctan")
        sizePolicy2.setHeightForWidth(self.btn_ctan.sizePolicy().hasHeightForWidth())
        self.btn_ctan.setSizePolicy(sizePolicy2)
        self.btn_ctan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ctan.setStyleSheet(u"font-size: 12pt;")
        self.btn_ctan.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_ctan, 5, 5, 1, 1)

        self.btn_sin = QPushButton(self.centralwidget)
        self.btn_sin.setObjectName(u"btn_sin")
        sizePolicy2.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy2)
        self.btn_sin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sin.setStyleSheet(u"font-size: 12pt;")
        self.btn_sin.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_sin, 5, 2, 1, 1)

        self.btn_bracket_open = QPushButton(self.centralwidget)
        self.btn_bracket_open.setObjectName(u"btn_bracket_open")
        sizePolicy2.setHeightForWidth(self.btn_bracket_open.sizePolicy().hasHeightForWidth())
        self.btn_bracket_open.setSizePolicy(sizePolicy2)
        self.btn_bracket_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bracket_open.setStyleSheet(u"font-size: 12pt;")
        self.btn_bracket_open.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_bracket_open, 5, 0, 1, 1)

        self.btn_ey = QPushButton(self.centralwidget)
        self.btn_ey.setObjectName(u"btn_ey")
        sizePolicy2.setHeightForWidth(self.btn_ey.sizePolicy().hasHeightForWidth())
        self.btn_ey.setSizePolicy(sizePolicy2)
        self.btn_ey.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ey.setStyleSheet(u"font-size: 12pt;")
        self.btn_ey.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_ey, 3, 5, 1, 1)

        self.btn_exp = QPushButton(self.centralwidget)
        self.btn_exp.setObjectName(u"btn_exp")
        sizePolicy2.setHeightForWidth(self.btn_exp.sizePolicy().hasHeightForWidth())
        self.btn_exp.setSizePolicy(sizePolicy2)
        self.btn_exp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exp.setStyleSheet(u"font-size: 12pt;")
        self.btn_exp.setIconSize(QSize(10, 10))

        self.grid_options.addWidget(self.btn_exp, 2, 4, 1, 1)

        self.btn_loc_1 = QPushButton(self.centralwidget)
        self.btn_loc_1.setObjectName(u"btn_loc_1")
        sizePolicy2.setHeightForWidth(self.btn_loc_1.sizePolicy().hasHeightForWidth())
        self.btn_loc_1.setSizePolicy(sizePolicy2)
        self.btn_loc_1.setStyleSheet(u"font-size: 12pt;")

        self.grid_options.addWidget(self.btn_loc_1, 0, 0, 1, 1)

        self.btn_loc_2 = QPushButton(self.centralwidget)
        self.btn_loc_2.setObjectName(u"btn_loc_2")
        sizePolicy2.setHeightForWidth(self.btn_loc_2.sizePolicy().hasHeightForWidth())
        self.btn_loc_2.setSizePolicy(sizePolicy2)
        self.btn_loc_2.setStyleSheet(u"font-size: 12pt;")

        self.grid_options.addWidget(self.btn_loc_2, 0, 1, 1, 1)

        self.btn_loc_3 = QPushButton(self.centralwidget)
        self.btn_loc_3.setObjectName(u"btn_loc_3")
        sizePolicy2.setHeightForWidth(self.btn_loc_3.sizePolicy().hasHeightForWidth())
        self.btn_loc_3.setSizePolicy(sizePolicy2)
        self.btn_loc_3.setStyleSheet(u"font-size: 12pt;")

        self.grid_options.addWidget(self.btn_loc_3, 0, 2, 1, 1)

        self.btn_loc_4 = QPushButton(self.centralwidget)
        self.btn_loc_4.setObjectName(u"btn_loc_4")
        sizePolicy2.setHeightForWidth(self.btn_loc_4.sizePolicy().hasHeightForWidth())
        self.btn_loc_4.setSizePolicy(sizePolicy2)
        self.btn_loc_4.setStyleSheet(u"font-size: 12pt;")

        self.grid_options.addWidget(self.btn_loc_4, 0, 3, 1, 1)

        self.btn_loc_5 = QPushButton(self.centralwidget)
        self.btn_loc_5.setObjectName(u"btn_loc_5")
        sizePolicy2.setHeightForWidth(self.btn_loc_5.sizePolicy().hasHeightForWidth())
        self.btn_loc_5.setSizePolicy(sizePolicy2)
        self.btn_loc_5.setStyleSheet(u"font-size: 12pt;")

        self.grid_options.addWidget(self.btn_loc_5, 0, 4, 1, 1)

        self.btn_loc_6 = QPushButton(self.centralwidget)
        self.btn_loc_6.setObjectName(u"btn_loc_6")
        sizePolicy2.setHeightForWidth(self.btn_loc_6.sizePolicy().hasHeightForWidth())
        self.btn_loc_6.setSizePolicy(sizePolicy2)
        self.btn_loc_6.setStyleSheet(u"font-size: 12pt;")

        self.grid_options.addWidget(self.btn_loc_6, 0, 5, 1, 1)


        self.verticalLayout.addLayout(self.grid_options)

        self.grid_main = QGridLayout()
        self.grid_main.setObjectName(u"grid_main")
        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/files/sharp_backspace_white_36dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon)
        self.btn_backspace.setIconSize(QSize(24, 24))

        self.grid_main.addWidget(self.btn_backspace, 0, 3, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_0, 3, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_sub, 2, 4, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy2.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy2)
        self.btn_dot.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_dot, 3, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6.setStyleSheet(u"")

        self.grid_main.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_div.setIconSize(QSize(24, 24))

        self.grid_main.addWidget(self.btn_div, 1, 4, 1, 1)

        self.btn_C = QPushButton(self.centralwidget)
        self.btn_C.setObjectName(u"btn_C")
        sizePolicy2.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy2)
        self.btn_C.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_C, 0, 4, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_add, 2, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_answer = QPushButton(self.centralwidget)
        self.btn_answer.setObjectName(u"btn_answer")
        sizePolicy2.setHeightForWidth(self.btn_answer.sizePolicy().hasHeightForWidth())
        self.btn_answer.setSizePolicy(sizePolicy2)

        self.grid_main.addWidget(self.btn_answer, 3, 3, 1, 1)

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_neg, 3, 2, 1, 1)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/files/sharp_calculate_white_36dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_calc.setIcon(icon1)
        self.btn_calc.setIconSize(QSize(30, 30))

        self.grid_main.addWidget(self.btn_calc, 3, 4, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid_main.addWidget(self.btn_8, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.grid_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Engineering Calculator", None))
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_3.setText("")
        self.label_2.setText("")
        self.label_1.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_circle_r.setText(QCoreApplication.translate("MainWindow", u"Or", None))
        self.btn_e2.setText(QCoreApplication.translate("MainWindow", u"^2", None))
        self.btn_es3.setText(QCoreApplication.translate("MainWindow", u"^s3", None))
        self.btn_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.btn_es2.setText(QCoreApplication.translate("MainWindow", u"^s2", None))
        self.btn_circle_d.setText(QCoreApplication.translate("MainWindow", u"Od", None))
        self.btn_mean.setText(QCoreApplication.translate("MainWindow", u"mean", None))
        self.btn_abs.setText(QCoreApplication.translate("MainWindow", u"abs", None))
        self.btn_median.setText(QCoreApplication.translate("MainWindow", u"med", None))
        self.btn_e1.setText(QCoreApplication.translate("MainWindow", u"^-1", None))
        self.btn_asin.setText(QCoreApplication.translate("MainWindow", u"asin", None))
        self.btn_atan.setText(QCoreApplication.translate("MainWindow", u"atan", None))
        self.btn_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.btn_acos.setText(QCoreApplication.translate("MainWindow", u"acos", None))
        self.btn_bracket_close.setText(QCoreApplication.translate("MainWindow", u")", None))
#if QT_CONFIG(shortcut)
        self.btn_bracket_close.setShortcut(QCoreApplication.translate("MainWindow", u")", None))
#endif // QT_CONFIG(shortcut)
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.btn_min.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.btn_esy.setText(QCoreApplication.translate("MainWindow", u"^sy", None))
        self.btn_pi.setText(QCoreApplication.translate("MainWindow", u"pi", None))
        self.btn_lg.setText(QCoreApplication.translate("MainWindow", u"lg", None))
        self.btn_max.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.btn_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.btn_actan.setText(QCoreApplication.translate("MainWindow", u"actan", None))
        self.btn_exp_x.setText(QCoreApplication.translate("MainWindow", u"e^x", None))
        self.btn_e3.setText(QCoreApplication.translate("MainWindow", u"^3", None))
        self.btn_ctan.setText(QCoreApplication.translate("MainWindow", u"ctan", None))
        self.btn_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.btn_bracket_open.setText(QCoreApplication.translate("MainWindow", u"(", None))
#if QT_CONFIG(shortcut)
        self.btn_bracket_open.setShortcut(QCoreApplication.translate("MainWindow", u"(", None))
#endif // QT_CONFIG(shortcut)
        self.btn_ey.setText(QCoreApplication.translate("MainWindow", u"^y", None))
        self.btn_exp.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.btn_loc_1.setText("")
        self.btn_loc_2.setText("")
        self.btn_loc_3.setText("")
        self.btn_loc_4.setText("")
        self.btn_loc_5.setText("")
        self.btn_loc_6.setText("")
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspace.setText("")
#if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_dot.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"AC", None))
#if QT_CONFIG(shortcut)
        self.btn_C.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_answer.setText(QCoreApplication.translate("MainWindow", u"Ans", None))
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_calc.setText("")
#if QT_CONFIG(shortcut)
        self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi


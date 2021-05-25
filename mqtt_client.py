from PyQt5 import QtCore, QtGui, QtWidgets
import paho.mqtt.client as mqtt
import json
import time
import random
import re
import sys
import resource

class Worker(QtCore.QThread):
    updated = QtCore.pyqtSignal(str)
    status = False
    flag = False

    def changeStatus(self, status):
        self.status = status

    def setText(self, text, flag):
        self.text = text
        self.flag = flag

    def run(self):
        if(self.status or self.flag):
            self.updated.emit(self.text)
        else:
            self.updated.emit("Please connect first!")

class Ui_MQTT(object):
    def __init__(self):
        self.client = mqtt.Client()
        self._thread = Worker()
        self._thread.updated.connect(self.appendText)

    def setupUi(self, MQTT):
        MQTT.setObjectName("MQTT")
        MQTT.resize(670, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MQTT.sizePolicy().hasHeightForWidth())
        MQTT.setSizePolicy(sizePolicy)
        MQTT.setMinimumSize(QtCore.QSize(670, 430))
        MQTT.setMaximumSize(QtCore.QSize(670, 430))
        self.centralwidget = QtWidgets.QWidget(MQTT)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 606, 376))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.sub_topic = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sub_topic.sizePolicy().hasHeightForWidth())
        self.sub_topic.setSizePolicy(sizePolicy)
        self.sub_topic.setEditable(True)
        self.sub_topic.setObjectName("sub_topic")
        self.sub_topic.addItem("")
        self.sub_topic.addItem("")
        self.sub_topic.addItem("")
        self.gridLayout.addWidget(self.sub_topic, 2, 7, 1, 1)
        self.subMessage = QtWidgets.QTextBrowser(self.layoutWidget)
        self.subMessage.setObjectName("subMessage")
        self.gridLayout.addWidget(self.subMessage, 4, 4, 2, 4)
        self.publishButton = QtWidgets.QPushButton(self.layoutWidget)
        self.publishButton.setObjectName("publishButton")
        self.gridLayout.addWidget(self.publishButton, 4, 0, 1, 4)
        self.port = QtWidgets.QLineEdit(self.layoutWidget)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 1, 1, 1, 3)
        self.subscribeButton = QtWidgets.QPushButton(self.layoutWidget)
        self.subscribeButton.setObjectName("subscribeButton")
        self.gridLayout.addWidget(self.subscribeButton, 3, 4, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.username = QtWidgets.QLineEdit(self.layoutWidget)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 5, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.interval = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interval.sizePolicy().hasHeightForWidth())
        self.interval.setSizePolicy(sizePolicy)
        self.interval.setDecimals(1)
        self.interval.setMinimum(0.0)
        self.interval.setSingleStep(0.1)
        self.interval.setObjectName("interval")
        self.gridLayout.addWidget(self.interval, 3, 3, 1, 1)
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 5, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.disconnectButton = QtWidgets.QPushButton(self.layoutWidget)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout.addWidget(self.disconnectButton, 1, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.pub_topic = QtWidgets.QComboBox(self.layoutWidget)
        self.pub_topic.setEditable(True)
        self.pub_topic.setObjectName("pub_topic")
        self.pub_topic.addItem("")
        self.pub_topic.addItem("")
        self.gridLayout.addWidget(self.pub_topic, 2, 1, 1, 3)
        self.host = QtWidgets.QComboBox(self.layoutWidget)
        self.host.setEditable(True)
        self.host.setObjectName("host")
        self.host.addItem("")
        self.host.addItem("")
        self.gridLayout.addWidget(self.host, 0, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.pubMessage = QtWidgets.QTextEdit(self.layoutWidget)
        self.pubMessage.setObjectName("pubMessage")
        self.gridLayout.addWidget(self.pubMessage, 5, 0, 1, 4)
        self.connectButton = QtWidgets.QPushButton(self.layoutWidget)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.times = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.times.sizePolicy().hasHeightForWidth())
        self.times.setSizePolicy(sizePolicy)
        self.times.setMinimum(1)
        self.times.setMaximum(99999)
        self.times.setObjectName("times")
        self.gridLayout.addWidget(self.times, 3, 1, 1, 1)
        self.qos = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qos.sizePolicy().hasHeightForWidth())
        self.qos.setSizePolicy(sizePolicy)
        self.qos.setEditable(False)
        self.qos.setMaxVisibleItems(1)
        self.qos.setMaxCount(3)
        self.qos.setObjectName("qos")
        self.qos.addItem("")
        self.qos.addItem("")
        self.qos.addItem("")
        self.gridLayout.addWidget(self.qos, 2, 5, 1, 1)
        MQTT.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MQTT)
        self.statusbar.setObjectName("statusbar")
        MQTT.setStatusBar(self.statusbar)

        self.retranslateUi(MQTT)
        QtCore.QMetaObject.connectSlotsByName(MQTT)

    def retranslateUi(self, MQTT):
        _translate = QtCore.QCoreApplication.translate
        MQTT.setWindowTitle(_translate("MQTT", "MQTT Client"))
        self.label_7.setText(_translate("MQTT", "Topic:"))
        self.sub_topic.setItemText(0, _translate("MQTT", "+/#"))
        self.sub_topic.setItemText(1, _translate("MQTT", "dev/"))
        self.sub_topic.setItemText(2, _translate("MQTT", "opendata/"))
        self.publishButton.setText(_translate("MQTT", "Publish"))
        self.subscribeButton.setText(_translate("MQTT", "Subscribe"))
        self.label_5.setText(_translate("MQTT", "Topic:"))
        self.label_4.setText(_translate("MQTT", "Password:"))
        self.label_6.setText(_translate("MQTT", "Times:"))
        self.label_2.setText(_translate("MQTT", "Port:"))
        self.disconnectButton.setText(_translate("MQTT", "Disconnect"))
        self.label_8.setText(_translate("MQTT", "Qos:"))
        self.pub_topic.setItemText(0, _translate("MQTT", "dev/"))
        self.pub_topic.setItemText(1, _translate("MQTT", "opendata/"))
        self.host.setItemText(0, _translate("MQTT", "192.168.1.41"))
        self.host.setItemText(1, _translate("MQTT", "192.168.1.29"))
        self.label_9.setText(_translate("MQTT", "Interval(s):"))
        self.pubMessage.setHtml(_translate("MQTT", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入mqtt发送数据json格式</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">随机数据:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">时间戳(int): &quot;<span style=\" color:#fc0107;\">*</span>&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">数据(str): &quot;<span style=\" color:#fc0107;\">#</span>&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">eg:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;device_id&quot;: 1,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;timestamp&quot;: &quot;*&quot;,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;values&quot;: {</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &quot;m.1339&quot;: &quot;#&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    }</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">}</p></body></html>"))
        self.connectButton.setText(_translate("MQTT", "Connect"))
        self.label_3.setText(_translate("MQTT", "Username:"))
        self.label.setText(_translate("MQTT", "Host:"))
        self.qos.setItemText(0, _translate("MQTT", "0"))
        self.qos.setItemText(1, _translate("MQTT", "1"))
        self.qos.setItemText(2, _translate("MQTT", "2"))

        self.host.setItemText(0, _translate("MQTT", "192.168.1.41"))
        self.host.setItemText(1, _translate("MQTT", "192.168.1.29"))
        self.sub_topic.setItemText(0, _translate("MQTT", "+/#"))
        self.sub_topic.setItemText(1, _translate("MQTT", "dev/"))
        self.sub_topic.setItemText(2, _translate("MQTT", "opendata/"))
        self.pub_topic.setItemText(0, _translate("MQTT", "dev/"))
        self.pub_topic.setItemText(1, _translate("MQTT", "opendata/"))

        self.port.setText(_translate("MQTT", "1883"))
        self.username.setText(_translate("MQTT", "k8s-docker"))
        self.password.setText(_translate("MQTT", "1234567"))

        self.publishButton.clicked.connect(self.onclick_publish)
        self.subscribeButton.clicked.connect(self.onclick_subscribe)

        self.connectButton.clicked.connect(self.onclick_connect)
        self.disconnectButton.clicked.connect(self.onclick_disconnect)

    def on_connect(self, client, userdata, flags, rc):
        if(rc == 0):
            self._thread.changeStatus(True)
            self._thread.setText("Connected with result code "+str(rc), False)
        else:
            self._thread.setText("Unexpected connection %s" % rc, True)
        
        self._thread.start()

    def on_message(self, client, userdata, msg):
        self._thread.setText(str(msg.payload.decode('utf-8')), False)
        self._thread.start()

    def on_subscribe(self, client, userdata, mid, granted_qos):
        self._thread.setText("On Subscribed: qos = %d" % granted_qos, False)
        self._thread.start()

    def on_disconnect(self, client, userdata, rc):
        if(rc == 0):
            if(self._thread.status):
                self._thread.changeStatus(False)
                self._thread.setText("Disconnect Successful!", True)
        else:
            self._thread.setText("Unexpected disconnection %s" % rc, True)
        
        self._thread.start()

    def loadDict(self, pubMessage):
        pubMessage = eval(pubMessage)

        for key in pubMessage.keys():
            if(str(type(pubMessage[key])) == "<class 'dict'>"):
               child_dict = pubMessage[key]
               child_dict_key = key
               for _key in child_dict.keys():
                if(child_dict[_key] == '#'):
                    pubMessage[child_dict_key][_key] = str(random.uniform(-100, 100))

            if(pubMessage[key] == '*'):
                pubMessage[key] = int(round(time.time() * 1000))

            if(pubMessage[key] == '#'):
                pubMessage[key] = str(random.uniform(-100, 100))
        
        return pubMessage

    def onclick_connect(self):
        host = self.host.currentText()#QCommoBox用currentText()获取text
        port = int(self.port.text())
        username = self.username.text()
        password = self.password.text()

        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        try:
            self.client.connect(host, port, 60)
            self.client.loop_start()
        except Exception as e:
            self._thread.setText(str(e), True)
            self._thread.start()

    def onclick_disconnect(self):
        self.client.on_disconnect = self.on_disconnect
        self.client.disconnect(self.client)
        self.client.loop_stop()

    def onclick_publish(self):
        topic = self.pub_topic.currentText()
        qos = int(self.qos.currentText())
        pubMessage = self.pubMessage.toPlainText()
        times = int(self.times.text())
        interval = float(self.interval.text())

        for i in range(times):
            try:
                load_dict = self.loadDict(pubMessage)
                self.client.publish(topic, payload=json.dumps(load_dict), qos=qos)# 发送消息
                if(i == (times-1)):
                    self._thread.setText("Publish Done!", False)
                    self._thread.start()

            except Exception as e:
                self._thread.setText(str(e), False)
                self._thread.start()
            time.sleep(interval)

    def onclick_subscribe(self):
        topic = self.sub_topic.currentText()
        qos = int(self.qos.currentText())

        self.client.on_message = self.on_message
        # self.client.on_subscribe = self.on_subscribe

        try:
            self.client.subscribe(topic, qos)
            self._thread.setText("On Subscribed: qos = %d" % qos, False)
            self._thread.start()
        except Exception as e:
            self._thread.setText(str(e), False)
            self._thread.start()

    def appendText(self,text):
        self.subMessage.append(text)
        self.subMessage.moveCursor(self.subMessage.textCursor().End)

if __name__ == '__main__':
    mqtt_client = QtWidgets.QApplication(sys.argv)
    myWindow = QtWidgets.QMainWindow()
    window = Ui_MQTT()
    window.setupUi(myWindow)
    myWindow.setWindowIcon(QtGui.QIcon(":/icon.ico"))
    myWindow.show()
    sys.exit(mqtt_client.exec_())
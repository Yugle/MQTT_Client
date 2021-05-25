# MQTT_Client
MQTT的客户端，支持批量发送随机数据、设置发送时间间隔、订阅

## UI文件转py
```
pyuic5 -o mqtt.py mqtt.ui 
```
后加入主函数
```
if __name__ == '__main__':
    mqtt_client = QtWidgets.QApplication(sys.argv)
    myWindow = QtWidgets.QMainWindow()
    window = Ui_MQTT()
    window.setupUi(myWindow)
    myWindow.setWindowIcon(QtGui.QIcon(":/icon.ico"))
    myWindow.show()
    sys.exit(mqtt_client.exec_())
```
## 添加图标
1. 软件图标  
生成rpc文件
转py
在主窗口程序导入

1. 软件小图标
```
myWindow.setWindowIcon(QtGui.QIcon(":/icon.ico"))
```
## 打包
1. MAC
```
pyinstaller --windowed --onefile --clean --noconfirm -i ./resource/icon.icns mqtt_client.py
```
2. Windows
```
pyinstaller -w -F -i .\resource\icon.ico --clean .\mqtt_client.py
```
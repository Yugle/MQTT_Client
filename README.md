# MQTT_Client
MQTT的客户端，支持批量发送随机数据、设置发送时间间隔、订阅。**练手项目**，未新建线程发送数据，**极其难用**

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
- 新建rpc文件
```
<!DOCTYPE RCC><RCC version="1.0">
<qresource prefix="/images">
<file alias="image.ico">images/image.ico</file>
</qresource>
</RCC>
```
- 转py
```
pyrcc5 -o resources_rc.py resources_rc.qrc
```
- 导入到主窗口程序
```
import resources_rc
```
2. 软件小图标
```
myWindow.setWindowIcon(QtGui.QIcon(":/icon.ico"))
```
## 带文件打包
1. 获取程序运行临时文件夹路径
```
def getResourcePath(self, relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
```
2. spec
```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['k8s_ui.py'],
             pathex=['/Users/phil/Desktop/k8s_client'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas

# append the 'config' dir
a.datas += extra_datas('config')    ###这里是自己的资源文件夹
       
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='k8s_ui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='resource/icon.icns')
app = BUNDLE(exe,
             name='k8s_ui.app',
             icon='./resource/icon.icns',
             bundle_identifier=None)
```
## 打包
1. MAC
```
pyinstaller --windowed --onefile --clean --noconfirm -i ./resource/icon.icns mqtt_client.py
pyinstaller --windowed --onefile --clean --noconfirm -i ./resource/icon.icns mqtt_client.spec
```
2. Windows
```
pyinstaller -w -F -i .\resource\icon.ico --clean .\mqtt_client.py
```

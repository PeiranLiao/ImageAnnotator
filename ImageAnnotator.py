from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage
import cv2
import matplotlib.pyplot as plt
import os
import json

class MainWindow:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi('ImageAnnotator.ui')

        self.ui.btnBrowseImagePath.clicked.connect(self.browsepath)
        self.ui.btnPreviousImage.clicked.connect(self.previousimage)
        self.ui.btnNextImage.clicked.connect(self.nextimage)
        self.ui.btnSaveCaptions.clicked.connect(self.savecaptions)
        self.imagepath = ''
        self.folderpath = ''
        self.imagelist = []
        self.captions_show = []
        self.caption_index = 0
        self.caption_index = int(self.caption_index)
        self.data = []

    def browsepath(self):
        self.imagepath, _ = QFileDialog.getOpenFileName(
            self.ui,
            "Please select the image to annotate",
            ".",
            "jpg(*.jpg)")
        self.folderpath = os.path.abspath(os.path.dirname(self.imagepath))
        self.json_path = os.path.join(self.folderpath, 'Annotations/caption.json')
        if os.path.exists(self.json_path):
            with open(self.json_path, 'r') as f:
                self.data = json.load(f)
        else:
            # 如果文件不存在，创建一个空的字典
            self.data = []
        if not os.path.exists(os.path.abspath(os.path.dirname(self.json_path))):
            os.mkdir(os.path.join(self.folderpath, 'Annotations'))
        self.imagelist = os.listdir(self.folderpath)
        self.ui.lineEditImagePath.setText(self.imagepath)
        # img = cv2.imread(self.imagepath)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = plt.imread(self.imagepath)
        x = img.shape[1]
        y = img.shape[0]
        self.zoomscale = 1
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.show()
        self.show_saved_caption()
        # try:
        #     self.imagepath, _ = QFileDialog.getOpenFileName(
        #         self.ui,
        #         "Please select the image to annotate",
        #         ".",
        #         "jpg(*.jpg)")
        #     self.folderpath = os.path.abspath(os.path.dirname(self.imagepath))
        #     self.imagelist = os.listdir(self.folderpath)
        #     self.ui.lineEditImagePath.setText(self.imagepath)
        #     # img = cv2.imread(self.imagepath)
        #     # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #     img = plt.imread(self.imagepath)
        #     x = img.shape[1]
        #     y = img.shape[0]
        #     self.zoomscale = 1
        #     frame = QImage(img, x, y, QImage.Format_RGB888)
        #     pix = QPixmap.fromImage(frame)
        #     self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        #     self.scene = QGraphicsScene()  # 创建场景
        #     self.scene.addItem(self.item)
        #     self.ui.graphicsView.setScene(self.scene)
        #     self.ui.graphicsView.show()
        #     self.show_saved_caption()
        # except Exception:
        #     QMessageBox.about(self.ui,
        #             'Error',
        #             f'''Image reading failed, check whether the image path is correct.'''
        #             )

    def previousimage(self):
        try:
            self.savecaptions()
            if(self.imagelist.index(os.path.basename(self.imagepath)) == 0):
                QMessageBox.about(self.ui,
                    'Error',
                    f'''This is the first image.'''
                    )
            else:    
                self.imagepath = os.path.join(self.folderpath, self.imagelist[self.imagelist.index(os.path.basename(self.imagepath)) - 1])
                # img = cv2.imread(self.imagepath)
                # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = plt.imread(self.imagepath)
                x = img.shape[1]
                y = img.shape[0]
                self.zoomscale = 1
                frame = QImage(img, x, y, QImage.Format_RGB888)
                pix = QPixmap.fromImage(frame)
                self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
                self.scene = QGraphicsScene()  # 创建场景
                self.scene.addItem(self.item)
                self.ui.graphicsView.setScene(self.scene)
                self.ui.graphicsView.show()
                self.ui.lineEditImagePath.setText(self.imagepath)
                # self.ui.lineEditCaption1.clear()
                # self.ui.lineEditCaption2.clear()
                # self.ui.lineEditCaption3.clear()
                # self.ui.lineEditCaption4.clear()
                # self.ui.lineEditCaption5.clear()
                self.show_saved_caption()
        except Exception:
            QMessageBox.about(self.ui,
                    'Error',
                    f'''This is the first image.'''
                    )


    def nextimage(self):
        try:
            self.savecaptions()
            self.imagepath = os.path.join(self.folderpath, self.imagelist[self.imagelist.index(os.path.basename(self.imagepath)) + 1])
            # img = cv2.imread(self.imagepath)
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = plt.imread(self.imagepath)
            x = img.shape[1]
            y = img.shape[0]
            self.zoomscale = 1
            frame = QImage(img, x, y, QImage.Format_RGB888)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.ui.graphicsView.setScene(self.scene)
            self.ui.graphicsView.show()
            self.ui.lineEditImagePath.setText(self.imagepath)
            # self.ui.lineEditCaption1.clear()
            # self.ui.lineEditCaption2.clear()
            # self.ui.lineEditCaption3.clear()
            # self.ui.lineEditCaption4.clear()
            # self.ui.lineEditCaption5.clear()
            self.show_saved_caption()
        except Exception:
            QMessageBox.about(self.ui,
                    'Error',
                    f'''This is the last image.'''
                    )

    def savecaptions(self):
        caption_1 = self.ui.lineEditCaption1.text()
        caption_2 = self.ui.lineEditCaption2.text()
        caption_3 = self.ui.lineEditCaption3.text()
        caption_4 = self.ui.lineEditCaption4.text()
        caption_5 = self.ui.lineEditCaption5.text()

        # QMessageBox.about(self.ui,
        #             'Test',
        #             f'''{self.captions_show}'''
        #             )
        # self.data[self.caption_index]["image_name"]
        data_current = [{"caption_id": 0, "caption": caption_1},
                {"caption_id": 1, "caption": caption_2},
                {"caption_id": 2, "caption": caption_3},
                {"caption_id": 3, "caption": caption_4},
                {"caption_id": 4, "caption": caption_5}]
        if(self.captions_show == []):
            self.data.append({"image_name": os.path.basename(self.imagepath), "captions": data_current})
        else:
            self.data[self.caption_index] = {"image_name": os.path.basename(self.imagepath), "captions": data_current}
        with open(self.json_path, 'w') as f:
            json.dump(self.data, f)
            
    def show_saved_caption(self):
        self.captions_show = []
        for i,d in enumerate(self.data):
            if(d["image_name"]==os.path.basename(self.imagepath)):
                self.captions_show = self.data[i]["captions"]
                self.caption_index = i
                break
                
        if(self.captions_show == []):
            self.ui.lineEditCaption1.clear()
            self.ui.lineEditCaption2.clear()
            self.ui.lineEditCaption3.clear()
            self.ui.lineEditCaption4.clear()
            self.ui.lineEditCaption5.clear()
        else:
            self.ui.lineEditCaption1.setText(self.captions_show[0]["caption"])
            self.ui.lineEditCaption2.setText(self.captions_show[1]["caption"])
            self.ui.lineEditCaption3.setText(self.captions_show[2]["caption"])
            self.ui.lineEditCaption4.setText(self.captions_show[3]["caption"])
            self.ui.lineEditCaption5.setText(self.captions_show[4]["caption"])


    
    def test(self):
        info = self.ui.lineEditCaption1.text()



        QMessageBox.about(self.ui,
                    'test',
                    f'''{info}'''
                    )


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    app.exec_()
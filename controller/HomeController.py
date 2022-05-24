# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 16:48
# @Author  : Zeeland
# @File    : HomeController.py
# @Software: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QBrush, QColor, QPalette, QPixmap, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QLineEdit, QAbstractItemView, QHeaderView, QTableWidget, \
    QTableWidgetItem, QMainWindow, QDesktopWidget, QAction
from views.home import Ui_MainWindow
from service.TodayEpiInfo import EpiService
import os
from pojo.epi_province import EpiProvince
from pojo.epi_area import EpiArea
from service.epi_province_service import EpiProvinceService
from service.epi_area_service import EpiAreaService


class HomeController(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,**kwargs):
        super().__init__()
        try:
            # registration config
            self.registration_list = kwargs['registration_list']
        except Exception as e:
            print('[error] HomeController init error:',e)

        # 往空的QWidget里面放置UI内容
        self.setupUi(self)
        self.initAttr()
        self.initFun()

    # 属性处理
    def initAttr(self):
        # init service
        self.epi_province_service = EpiProvinceService(pool=self.registration_list['pool_config'].pool)
        self.epi_area_service = EpiAreaService(pool=self.registration_list['pool_config'].pool)
        self.epi_service = EpiService()

        self.setWindowTitle("EpidemicInfoManagement")

        # 整行选中
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置表格不可编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnWidth(0,200)

        # 设置背景图片
        palette = QtGui.QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap(os.getcwd()+"\static\images\\bg1.jpg")))
        self.setPalette(palette)

        # 渲染省份疫情信息
        self.render_province()

        # 渲染今日数据
        self.render_today_info()

        # 当前页面 省份：0  地区：1 搜索：2
        self.current_page = 0

    # 信号与槽绑定
    def initFun(self):
        self.btn_change_area.clicked.connect(self.render_area)
        self.btn_change_provice.clicked.connect(self.render_province)

        self.btn_search.clicked.connect(self.search)
        self.lineEdit_search.textChanged.connect(self.search)

        self.btn_get_new_info.clicked.connect(self.get_new)
        self.btn_delete.clicked.connect(self.delete_item)

        # self.action1_exit.hovered.connect(self.exit)
        self.action1_exit.triggered.connect(self.exit)

        # 快捷键设置
        self.btn_search.setShortcut('enter')

    def delete_item(self):
        selectedItem = self.tableWidget.selectedItems()
        if len(selectedItem)==0:
            QMessageBox.about(self, "提示", "需要选中一项内容")
        else:
            reply = QMessageBox.information(self, '提示','是否删除当前选项',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                print('yes')
                if self.current_page ==0:
                    self.epi_province_service.delete(selectedItem[1].text(),selectedItem[0].text())
                    QMessageBox.about(self, "提示", "删除成功")

                    self.render_province()
                elif self.current_page ==1:
                    self.epi_area_service.delete(selectedItem[1].text(), selectedItem[0].text())
                    QMessageBox.about(self, "提示", "删除成功")
                    self.render_area()
                else:
                    self.epi_province_service.delete(selectedItem[1].text(), selectedItem[0].text())
                    self.epi_area_service.delete(selectedItem[1].text(), selectedItem[0].text())
                    self.render_province()
            else:
                print('no')

    def exit(self):
        app = QApplication.instance()
        app.quit()

    def clear_tablewidget(self):
            count = self.tableWidget.rowCount()
            while count!=0:
                self.tableWidget.removeRow(count-1)
                count = self.tableWidget.rowCount()

    def search(self):
        self.current_page = 2
        print('[info] searching ...')
        self.clear_tablewidget()
        search_word = self.lineEdit_search.text()
        if search_word=='':
            self.render_province()
        area_res = self.epi_area_service.get_by_name(search_word)
        print(area_res)
        province_res = self.epi_province_service.get_by_name(search_word)
        print(province_res)
        current_row = self.tableWidget.rowCount()
        if area_res is not None:
            for row in range(len(area_res)):
                temp = area_res[row]
                self.tableWidget.insertRow(row+current_row)
                epi_area = EpiArea(temp)
                # print(epi_area)

                gridItem = QTableWidgetItem(str(epi_area.area_total_update_time))
                self.tableWidget.setItem(row+current_row,0, gridItem)
                gridItem = QTableWidgetItem(epi_area.area_name)
                self.tableWidget.setItem(row+current_row,1, gridItem)
                gridItem = QTableWidgetItem(str(epi_area.area_total_confirm))
                self.tableWidget.setItem(row+current_row,2, gridItem)
                gridItem = QTableWidgetItem(str(epi_area.area_total_heal))
                self.tableWidget.setItem(row+current_row,3, gridItem)
                gridItem = QTableWidgetItem(str(epi_area.area_total_dead))
                self.tableWidget.setItem(row+current_row,4, gridItem)
                gridItem = QTableWidgetItem(str(epi_area.area_today_confirm))
                self.tableWidget.setItem(row+current_row,5, gridItem)
        current_row = self.tableWidget.rowCount()
        if province_res is not None:
            for row in range(len(province_res)):
                temp = province_res[row]
                self.tableWidget.insertRow(row+current_row)
                epi_province = EpiProvince(temp)

                gridItem = QTableWidgetItem(str(epi_province.province_total_update_time))
                self.tableWidget.setItem(row+current_row,0, gridItem)
                gridItem = QTableWidgetItem(epi_province.province_name)
                self.tableWidget.setItem(row+current_row,1, gridItem)
                gridItem = QTableWidgetItem(str(epi_province.province_total_confirm))
                self.tableWidget.setItem(row+current_row,2, gridItem)
                gridItem = QTableWidgetItem(str(epi_province.province_total_heal))
                self.tableWidget.setItem(row+current_row,3, gridItem)
                gridItem = QTableWidgetItem(str(epi_province.province_total_dead))
                self.tableWidget.setItem(row+current_row,4, gridItem)
                gridItem = QTableWidgetItem(str(epi_province.province_today_confirm))
                self.tableWidget.setItem(row+current_row,5, gridItem)

    def render_today_info(self):
        # 渲染今日数据
        self.epi_service.get_today_info_by_jsonfile(os.getcwd()+'\service\\today_epi_info.json')
        self.label_now_confirm.setText(str(self.epi_service.epi_data['chinaTotal']['nowConfirm']))
        self.label_confirm.setText(str(self.epi_service.epi_data['chinaTotal']['confirm']))
        self.label_no_infectH5.setText(str(self.epi_service.epi_data['chinaTotal']['noInfectH5']))
        self.label_imported_case.setText(str(self.epi_service.epi_data['chinaTotal']['importedCase']))
        self.label_dead.setText(str(self.epi_service.epi_data['chinaTotal']['dead']))

        self.label_new_now_confirm.setText(str(self.epi_service.epi_data['chinaAdd']['nowConfirm']))
        self.label_new_confirm.setText(str(self.epi_service.epi_data['chinaAdd']['confirm']))
        self.label_new_no_infectH5.setText(str(self.epi_service.epi_data['chinaAdd']['noInfectH5']))
        self.label_new_imported_case.setText(str(self.epi_service.epi_data['chinaAdd']['importedCase']))
        self.label_new_dead.setText(str(self.epi_service.epi_data['chinaAdd']['dead']))

        self.lineEdit_rencent_update.setText(self.epi_service.lastUpdateTime)

    # 查询新的信息
    def get_new(self):
        print('[info] find new info')
        self.epi_service.get_today_info()
        self.epi_service.save_today_data_to_db()
        self.clear_tablewidget()
        self.render_province()

        self.label_now_confirm.setText(str(self.epi_service.epi_data['chinaTotal']['nowConfirm']))
        self.label_confirm.setText(str(self.epi_service.epi_data['chinaTotal']['confirm']))
        self.label_no_infectH5.setText(str(self.epi_service.epi_data['chinaTotal']['noInfectH5']))
        self.label_imported_case.setText(str(self.epi_service.epi_data['chinaTotal']['importedCase']))
        self.label_dead.setText(str(self.epi_service.epi_data['chinaTotal']['dead']))

        self.label_new_now_confirm.setText(str(self.epi_service.epi_data['chinaAdd']['nowConfirm']))
        self.label_new_confirm.setText(str(self.epi_service.epi_data['chinaAdd']['confirm']))
        self.label_new_no_infectH5.setText(str(self.epi_service.epi_data['chinaAdd']['noInfectH5']))
        self.label_new_imported_case.setText(str(self.epi_service.epi_data['chinaAdd']['importedCase']))
        self.label_new_dead.setText(str(self.epi_service.epi_data['chinaAdd']['dead']))

        self.lineEdit_rencent_update.setText(self.epi_service.lastUpdateTime)
        self.lineEdit_count_of_data.setText(str(self.epi_province_service.get_count()))

    def render_area(self):
        self.current_page = 1
        self.lineEdit_count_of_data.setText(str(self.epi_area_service.get_count()))
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "城市"))
        print('[info] render_area')
        self.clear_tablewidget()
        self.tableWidget.scrollToTop()
        res = self.epi_area_service.get_all()
        current_row = self.tableWidget.rowCount()
        for row in range(len(res)):
            temp = res[row]
            self.tableWidget.insertRow(row+current_row)
            epi_area = EpiArea(temp)
            # print(epi_area)

            gridItem = QTableWidgetItem(str(epi_area.area_total_update_time))
            self.tableWidget.setItem(row+current_row,0, gridItem)
            gridItem = QTableWidgetItem(epi_area.area_name)
            self.tableWidget.setItem(row+current_row,1, gridItem)
            gridItem = QTableWidgetItem(str(epi_area.area_total_confirm))
            self.tableWidget.setItem(row+current_row,2, gridItem)
            gridItem = QTableWidgetItem(str(epi_area.area_total_heal))
            self.tableWidget.setItem(row+current_row,3, gridItem)
            gridItem = QTableWidgetItem(str(epi_area.area_total_dead))
            self.tableWidget.setItem(row+current_row,4, gridItem)
            gridItem = QTableWidgetItem(str(epi_area.area_today_confirm))
            self.tableWidget.setItem(row+current_row,5, gridItem)

    def render_province(self):
        self.current_page = 0
        self.lineEdit_count_of_data.setText(str(self.epi_province_service.get_count()))
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "省份"))
        print('[info] render_province')
        self.clear_tablewidget()
        self.tableWidget.scrollToTop()
        res = self.epi_province_service.get_all()
        current_row = self.tableWidget.rowCount()

        for row in range(len(res)):
            temp = res[row]
            self.tableWidget.insertRow(row+current_row)
            epi_province = EpiProvince(temp)
            print(epi_province)

            gridItem = QTableWidgetItem(str(epi_province.province_total_update_time))
            self.tableWidget.setItem(row+current_row,0, gridItem)
            gridItem = QTableWidgetItem(epi_province.province_name)
            self.tableWidget.setItem(row+current_row,1, gridItem)
            gridItem = QTableWidgetItem(str(epi_province.province_total_confirm))
            self.tableWidget.setItem(row+current_row,2, gridItem)
            gridItem = QTableWidgetItem(str(epi_province.province_total_heal))
            self.tableWidget.setItem(row+current_row,3, gridItem)
            gridItem = QTableWidgetItem(str(epi_province.province_total_dead))
            self.tableWidget.setItem(row+current_row,4, gridItem)
            gridItem = QTableWidgetItem(str(epi_province.province_today_confirm))
            self.tableWidget.setItem(row+current_row,5, gridItem)
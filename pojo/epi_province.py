# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 21:08
# @Author  : Zeeland
# @File    : epi_province_service.py
# @Software: PyCharm
import datetime

class EpiProvince:
    def __init__(self,*args,**kwargs):
        # 地区名称
        self.province_name = None
        # 日期
        self.province_today_date = None
        # 更新时间
        self.province_total_update_time = None
        # 死亡人数
        self.province_total_dead = None
        # 治愈人数
        self.province_total_heal = None
        # 现有确诊
        self.province_total_now_confirm = None
        # 累积确诊
        self.province_total_confirm = None
        # 今日新增
        self.province_today_confirm = None
        # 逻辑删除
        self.is_delete = None
        # judge if the args is empty
        try:
            if len(args) == 0:
                self.province_name = kwargs['data']['province_name']
                self.province_today_date = kwargs['data']['province_today_date']
                self.province_total_update_time = kwargs['data']['province_total_update_time']
                self.province_total_dead = kwargs['data']['province_total_dead']
                self.province_total_heal = kwargs['data']['province_total_heal']
                self.province_total_now_confirm = kwargs['data']['province_total_now_confirm']
                self.province_total_confirm = kwargs['data']['province_total_confirm']
                self.province_today_confirm = kwargs['data']['province_today_confirm']
                self.is_delete = kwargs['data']['is_delete']
            else:
                args = args[0]
                self.province_name = args[1]
                self.province_today_date = args[2]
                self.province_total_update_time = args[3]
                self.province_total_dead = args[4]
                self.province_total_heal = args[5]
                self.province_total_now_confirm = args[6]
                self.province_total_confirm = args[7]
                self.province_today_confirm = args[8]
                self.is_delete = args[9]
        except Exception as e:
            print('[error]',e)

    def __str__(self):
        # print all info
        return 'province_name:%s,province_today_date:%s,province_total_update_time:%s,' \
               'province_total_dead:%s,province_total_heal:%s,province_total_now_confirm:%s,province_total_confirm:' \
               '%s,province_today_confirm:%s,is_delete:%s' % (self.province_name, self.province_today_date,
                self.province_total_update_time, self.province_total_dead,self.province_total_heal,
                self.province_total_now_confirm, self.province_total_confirm,
                self.province_today_confirm, self.is_delete)

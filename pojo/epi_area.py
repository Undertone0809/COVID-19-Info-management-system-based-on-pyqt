# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 21:08
# @Author  : Zeeland
# @File    : epi_area.py
# @Software: PyCharm

class EpiArea:
    def __init__(self,*args,**kwargs):
        # 省份id
        self.province_id = None
        # 地区名称
        self.area_name = None
        # 日期
        self.area_today_date = None
        # 更新时间
        self.area_total_update_time = None
        # 累积确诊
        self.area_total_confirm = None
        # 累积治疗
        self.area_total_heal = None
        # 累积死亡
        self.area_total_dead = None
        # 今日新增
        self.area_today_confirm = None
        # 逻辑删除
        self.is_delete = None
        try:
            if len(args) == 0:
                self.province_id = kwargs['data']['province_id']
                self.area_name = kwargs['data']['area_name']
                self.area_today_date = kwargs['data']['area_today_date']
                self.area_total_update_time = kwargs['data']['area_total_update_time']
                self.area_total_confirm = kwargs['data']['area_total_confirm']
                self.area_total_heal = kwargs['data']['area_total_heal']
                self.area_total_dead = kwargs['data']['area_total_dead']
                self.area_today_confirm = kwargs['data']['area_today_confirm']
                self.is_delete = kwargs['data']['is_delete']
            else:
                args = args[0]
                self.province_id = args[1]
                self.area_name = args[2]
                self.area_today_date = args[3]
                self.area_total_update_time = args[4]
                self.area_total_confirm = args[5]
                self.area_total_heal = args[6]
                self.area_total_dead = args[7]
                self.area_today_confirm = args[8]
                self.is_delete = args[9]
        except Exception as e:
            print('[error] EpiArea init error:', e)

    def __str__(self):
        # print all info
        return 'province_id: %s, area_name: %s, area_today_date: %s, area_total_update_time: %s,' \
               ' area_total_confirm: %s, area_total_heal: %s, area_total_dead: %s, area_today_confirm: %s,' \
               ' id_delete: %s' % (self.province_id, self.area_name, self.area_today_date,
                                   self.area_total_update_time, self.area_total_confirm, self.area_total_heal,
                                   self.area_total_dead, self.area_today_confirm, self.is_delete)
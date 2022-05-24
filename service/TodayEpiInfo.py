from email import header


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description: 爬取疫情相关的信息
@Date       : 2022/05/14 01:38:43
@Author     : Zeeland
@version    : 1.0
'''
import requests      # 发送网络请求模块
import json
from pojo.epi_province import EpiProvince
from pojo.epi_area import EpiArea
from service.epi_province_service import EpiProvinceService
from service.epi_area_service import EpiAreaService

class EpiService:
    def __init__(self):
        self.url='https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
        self.epi_data = {}         # 总数据
        self.chinaTotal = {}       # 累计
        self.chinaAdd = {}         # 今日新增
        self.provinces = {}        # 各省份信息
        self.lastUpdateTime = ''   # 最近更新时间

        # service init
        from config.PoolConfig import PoolConfig
        self.pool_config = PoolConfig()
        self.epi_province_service = EpiProvinceService(pool=self.pool_config.pool)
        self.epi_area_service = EpiAreaService(pool=self.pool_config.pool)

    """
    @description: 获取最新的疫情数据,并赋值给self.epi_data
    @param      : null
    @Returns    : null
    """
    def get_today_info(self):
        requests.packages.urllib3.disable_warnings()
        response = requests.get(self.url, verify=False)
        self.epi_data = response.json()['data']['diseaseh5Shelf']
        self.lastUpdateTime = self.epi_data['lastUpdateTime']
        print(self.epi_data)


    """
    @description: 用jsonfile文件加载今日数据（一般用于测试）
    @param      : file_dir为文件路径
    @Returns    : null
    """
    def get_today_info_by_jsonfile(self,file_dir='today_epi_info.json'):
        with open(file_dir, "r", encoding='utf-8') as f:
            self.epi_data = json.loads(f.read())  # load的传入参数为字符串类型
            # print(self.epi_data)
            self.lastUpdateTime = self.epi_data['lastUpdateTime']

    """
    @description: 将self.epi_data的数据存到数据库中,需要注意的是,调用此函数之前,需要先调用get_today_info()
                  或者get_today_info_by_jsonfile()获取到self.epi_data对应的值
    @param      : null
    @Returns    : null
    """
    def save_today_data_to_db(self):
        china_data = self.epi_data['areaTree'][0]['children']  # 列表
        # iterate every province of China
        for province in china_data:
            province_info = {}
            # 地区名称
            province_info['province_name'] = province['name']
            # 日期
            province_info['province_today_date'] = province['date']
            # 更新时间
            province_info['province_total_update_time'] = province['total']['mtime']
            # 死亡人数
            province_info['province_total_dead'] = province['total']['dead']
            # 治愈人数
            province_info['province_total_heal'] = province['total']['heal']
            # 现存确诊人数
            province_info['province_total_now_confirm'] = province['total']['nowConfirm']
            # 累积确诊人数
            province_info['province_total_confirm'] = province['total']['confirm']
            # 新增确诊人数
            province_info['province_today_confirm'] = province['today']['confirm']
            # 逻辑删除
            province_info['is_delete'] = 0

            # insert to db
            epi_province = EpiProvince(data=province_info)
            self.epi_province_service.insert(epi_province)
            print(epi_province)

            for area in province['children']:
                # print(area)
                area_info = {}
                # 地区名称
                area_info['area_name'] = area['name']
                # 日期
                area_info['area_today_date'] = area['date']
                # 更新时间
                area_info['area_total_update_time'] = area['total']['mtime']
                # 累积确诊
                area_info['area_total_confirm'] = area['total']['confirm']
                # 累积治疗
                area_info['area_total_heal'] = area['total']['heal']
                # 累积死亡
                area_info['area_total_dead'] = area['total']['dead']
                # 今日新增
                area_info['area_today_confirm'] = area['today']['confirm']
                # 逻辑删除
                area_info['is_delete'] = 0

                res = self.epi_province_service.get_key_by_name_and_time(province_info['province_name'],province_info['province_today_date'])
                if res is not None:
                    area_info['province_id'] = res[0]
                    epi_area = EpiArea(data=area_info)
                    # print(epi_area)
                    self.epi_area_service.insert(epi_area)

    """
    @description: 将self.epi_data的数据存到数据库中,需要注意的是,调用此函数之前,需要先调用get_today_info()
                  或者get_today_info_by_jsonfile()获取到self.epi_data对应的值
    @param      : null
    @Returns    : null
    """
    def save_today_data_to_jsonfile(self):
        with open("today_epi_info.json", "w", encoding='utf-8') as f:
            f.write(json.dumps(self.epi_data, indent=4))

if __name__ == '__main__':
    epi_service = EpiService()
    epi_service.get_today_info()
    epi_service.save_today_data_to_jsonfile()


    # epi_service.get_today_info_by_jsonfile()
    epi_service.save_today_data_to_db()

# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 11:18
# @Author  : Zeeland
# @File    : epi_province_service.py
# @Software: PyCharm
from config.MysqlConfig import MysqlConfig

class EpiProvinceService(MysqlConfig):
    def __init__(self,pool=None):
        super().__init__(pool=pool)

    def get_all(self):
        try:
            self.cursor.execute('select * from epi_province order by province_total_update_time desc')
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('[error]',e)
            return None

    def get_count(self):
        try:
            self.cursor.execute('select count(*) from epi_province')
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print('[error] EpiProvinceService get_count:',e)
            return None

    def get_by_id(self,key_id):
        try:
            self.cursor.execute('select * from epi_province where id = %s',(key_id,))
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('[error] EpiProvinceService get_by_id err:',e)
            return None

    def get_by_name(self,province_name):
        try:
            # 查找里面含有有该字符串的数据
            self.cursor.execute('select * from epi_province where province_name like %s',(province_name+"%",))
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('[error] EpiProvinceService get_by_name err:',e)
            return None

    def get_key_by_name_and_time(self,province_name,province_today_time):
        # print('[pro] name:'+province_name+' time: '+province_today_time)
        try:
            self.cursor.execute('select * from epi_province where province_name = %s and province_today_date = %s',
                                (province_name,province_today_time))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print('[error] EpiProvinceService get_key_by_name_and_time err:',e)
            return None

    def insert(self,epi_province):
        try:
            # find if has the same update time info, if has, then insert new one, if not, then do nothing
            self.cursor.execute('select * from epi_province where province_total_update_time = %s',
                                (epi_province.province_total_update_time,))
            result = self.cursor.fetchone()
            if result:
                # do nothing
                print('[info] EpiProvinceService insert: has the same data')
            else:
                # insert
                self.cursor.execute('insert into epi_province (province_name,province_today_date,'
                                    'province_total_update_time,province_total_dead,province_total_heal,'
                                    'province_total_now_confirm,province_total_confirm,province_today_confirm,'
                                    'is_delete) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(epi_province.province_name,
                                        epi_province.province_today_date, epi_province.province_total_update_time,
                                        epi_province.province_total_dead, epi_province.province_total_heal,
                                        epi_province.province_total_now_confirm, epi_province.province_total_confirm,
                                        epi_province.province_today_confirm, epi_province.is_delete))
                self.conn.commit()
                print('[info] insert successfully')
        except Exception as e:
            print('[error] EpiProvinceService insert err:',e)
            self.conn.rollback()

    def delete(self,province_name,update_time):
        try:
            self.cursor.execute('delete from epi_province where province_name = %s and province_total_update_time = %s',
                                (province_name,update_time))
            self.conn.commit()
        except Exception as e:
            print('[error] EpiProvinceService delete err:',e)
            self.conn.rollback()

    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print('[error] db close',e)

if __name__ == '__main__':
    from pojo.epi_province import EpiProvince
    epi_service = EpiProvinceService()
    res = epi_service.get_by_name("台湾")
    for item in res:
        print(item)
        epi_province = EpiProvince(item)
        # epi_service.delete(epi_province.province_name,epi_province.province_total_update_time)
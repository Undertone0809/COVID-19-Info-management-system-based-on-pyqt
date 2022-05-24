# -*- coding: utf-8 -*-
# @Time    : 2022/5/13 11:18
# @Author  : Zeeland
# @File    : epi_province_service.py
# @Software: PyCharm

from config.MysqlConfig import MysqlConfig

class EpiAreaService(MysqlConfig):
    def __init__(self,pool=None):
        super().__init__(pool=pool)

    def get_all(self):
        try:
            self.cursor.execute('select * from epi_area order by area_total_update_time desc')
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('[error] EpiAreaService get all error:',e)
            return None

    def get_count(self):
        try:
            self.cursor.execute('select count(*) from epi_area')
            result = self.cursor.fetchone()
            return result[0]
        except Exception as e:
            print('[error] EpiProvinceService get_count:',e)
            return None

    def get_by_name(self,area_name):
        try:
            self.cursor.execute('select * from epi_area where area_name like %s',(area_name+"%",))
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('[error] EpiAreaService get by name error:',e)
            return None        

    def insert(self,epi_area):
        try:
            # find if has the same area_total_update_time and area_name, if has, then insert new one, if not, then do nothing
            self.cursor.execute('select * from epi_area where area_total_update_time = %s and area_name = %s',
                                (epi_area.area_total_update_time, epi_area.area_name))
                                
            result = self.cursor.fetchone()
            if result:
                # do nothing
                print('[info] EpiAreaService insert: has the same data')
            else:
                # insert
                self.cursor.execute('insert into epi_area (province_id,area_name,area_today_date,'
                                    'area_total_update_time,area_total_confirm,area_total_heal,area_total_dead,'
                                    'area_today_confirm,is_delete) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                    (epi_area.province_id,epi_area.area_name,epi_area.area_today_date,
                                     epi_area.area_total_update_time,epi_area.area_total_confirm,epi_area.area_total_heal,
                                    epi_area.area_total_dead,epi_area.area_today_confirm,epi_area.is_delete))
                self.conn.commit()
                print('[info] insert successfully')
        except Exception as e:
            print('[error] EpiAreaService insert error:,',e)
            self.conn.rollback()

    def delete(self, province_name, update_time):
        try:
            self.cursor.execute('delete from epi_area where area_name = %s and area_total_update_time = %s',
                                (province_name, update_time))
            self.conn.commit()
            print('[info] delete successfully') 
        except Exception as e:
            print('[error] EpiAreaService delete error:',e)
            self.conn.rollback()

    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print('[error] db close',e)

if __name__ == '__main__':
    epi_service = EpiAreaService()
    print(epi_service.get_count())
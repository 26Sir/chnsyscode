#!/usr/bin/env python
# -*- coding: utf-8 -*-

from eleac.eleac_api.eleac import BaseApi


class Index_sjtj(BaseApi):

    def sjtj(self,ip,startDate,endDate,lookDept,statisticalUnitId,statisticalUnitLevel,unitId):
        '''
        @param ip: ip地址
        @param startDate: 开始时间
        @param endDate: 结束时间
        @param lookDept:是否需要查看部门
        @param statisticalUnitId:统计单元id
        @param statisticalUnitLevel: 统计单元级别 1、最高院级别 2、高院 3、中院 4、基层院 5、部门 6、个人
        @param unitId:单位id:仅查询人员列表时有用
        @return:
        '''
        data = {
            "method" :"post",
            "url" : f"http://{ip}//eleac/statis/statis",
            "json" :{
                "endDate": endDate,
                "startDate": startDate,
                "lookDept": lookDept,
                "statisticalUnitId": statisticalUnitId,
                "statisticalUnitLevel": statisticalUnitLevel,
                "unitId": unitId
            }
        }
        return self.send(**data)
    
    def syym(self,ip):
        '''
        @param ip:
        @return:
        '''
        data = {
            "method": "get",
            "url": f"http://{ip}/eleac/#/basicData",
        }
        return  self.send(**data)
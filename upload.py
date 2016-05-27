#!/usr/bin/python
# coding:utf-8

import os
import sys
import getpass
from archiveiOS import Item
import readyUploadData


def upload(item):
    # 检验包是否有效
    validateCmd = r'%s -m verify -u %s -p %s -f %s' % (item.iTMSTransporter, distribute_account, distribute_pwd, itmsp_path)
    os.system(validateCmd)

    # 上传
    uploadCmd = r'%s -m upload -u %s -p %s -f %s' % (item.iTMSTransporter, distribute_account, distribute_pwd, itmsp_path)
    os.system(uploadCmd)     


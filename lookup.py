#!/usr/bin/python
# coding:utf-8

import os
import sys
import getpass
from archive import Item

def lookup(item):
	# 获取metadata
    lookupMetadataCmd = r'%s -m lookupMetadata -u %s -p %s -vendor_id %s -destination %s' % (item.iTMSTransporter, item.distribute_account, item.distribute_pwd, item.vendor_id, item.out_path)
    #print lookupMetadataCmd
    os.system(lookupMetadataCmd)

    itmsp_path = r'%s/%s.itmsp' % (item.out_path, item.vendor_id)
    item.itmsp_path = itmsp_path
    print 'itmsp:' + itmsp_path
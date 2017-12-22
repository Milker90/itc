#!/usr/bin/python
# coding:utf-8

import metaxml
import conf
import os
import sys
import upload
import conf
import lookup
from archive import Item
import archive
import getpass
import assembly

if __name__ == '__main__':	
    item = Item(conf.iTMSTransporter, conf.distribute_account, conf.distribute_pwd, conf.bundle_short_version_string, conf.bundle_version, conf.project_path, conf.scheme, conf.configuration, conf.provisioning_profile_name, conf.vendor_id)

    # 开始打包
    archive.archive(item)

    # 获取itmsp
    lookup.lookup(item)

    # 准备上传
    assembly.assembly(item)

    # 开始上传
    upload.upload(item)


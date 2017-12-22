#!/usr/bin/python
# coding:utf-8

import os
import sys
import time

class Item:
    def __init__(self, iTMSTransporter, distribute_account, distribute_pwd, bundle_short_version_string, bundle_version, project_path, scheme, configuration, provisioning_profile_name, vendor_id):
        self.bundle_short_version_string = bundle_short_version_string
        self.bundle_version = bundle_version
        self.project_path = project_path
        self.scheme = scheme
        self.configuration = configuration
        self.provisioning_profile_name = provisioning_profile_name
        self.workspace_path = project_path + '/' + scheme + '.xcworkspace'
        self.vendor_id = vendor_id
        self.itmsp_path = ''
        self.iTMSTransporter = iTMSTransporter
        self.distribute_account = distribute_account
        self.distribute_pwd = distribute_pwd

        # 创建输出路径
        nowDate = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))                
        out_scheme_path = os.getcwd() + '/' + scheme
        if not os.path.exists(out_scheme_path):
            os.mkdir(out_scheme_path)

        out_data_path = out_scheme_path + '/' + nowDate
        if not os.path.exists(out_data_path):            
            os.mkdir(out_data_path)

        self.out_path = out_data_path
        self.ipa_path = out_data_path + '/' + scheme + '_' + nowDate
        self.archive_path = out_data_path + '/' + scheme + '_' + nowDate + '.xcarchive'

# 手动输入版本信息
def generateItem():
    # 当前路径
    cur_path = os.getcwd()

    # 账号
    distribute_account = raw_input('请输入发布账号：')
    if not distribute_account:
        print '请输入发布账号!!!'
        return

    # 密码
    distribute_pwd = getpass.getpass('请输入密码：')
    if not distribute_pwd:
        print '请输入密码!!!'
        return

    # 发布版本号
    bundle_short_version_string = raw_input('请输入发布版本号：')
    if not bundle_short_version_string:
        print '发布版本号不能为空!!!'
        return

    # 开发版本号
    bundle_version = raw_input('请输入开发版本号：')
    if not bundle_version:
        print '开发版本号不能为空!!!'
        return

    # 工程路径
    project_path = raw_input('请输入工程路径：')
    if not project_path:
        print '工程路径不能为空!!!'
        return

    # scheme
    scheme = raw_input('请输入App Scheme：')
    if not scheme:
        print 'App Scheme 不能为空!!!'
        return

    # 指定证书类型
    configuration = raw_input('请输入打包类型：')
    if not configuration:
        configuration = 'AdHoc'

    # 证书名字
    provisioning_profile_name = raw_input('请输入证书名字：')
    if not provisioning_profile_name:
        print '证书名字不能为空!!!'
        return

    # vendor_id App SKU
    vendor_id = raw_input('请输入App SKU：')
    if not vendor_id:
        print 'App SKU不能为空!!!'
        return    

    # 生成打包item
    item = Item(distribute_account, distribute_pwd, bundle_short_version_string, bundle_version, project_path, scheme, configuration, provisioning_profile_name, vendor_id)

    return item
  

def archive(item):
    # 清除上一次build记录
    cleanCmd = r'xcodebuild clean -workspace %s -scheme %s -configuration %s' % (
        item.workspace_path, item.scheme, item.configuration)
    os.system(cleanCmd)
    print 'clean finished...\n'

    # 生成archive文件
    garchiveFileCmd = r'xcodebuild -workspace %s -scheme %s -configuration %s archive -archivePath %s' % (
        item.workspace_path, item.scheme, item.configuration, item.archive_path)
    os.system(garchiveFileCmd)
    print 'archive finished...\n'

    # 导出ipa
    print 'ipa_path: ' +  item.ipa_path
    # exportIPACmd = r'xcodebuild -exportArchive -archivePath %s -exportPath %s -exportProvisioningProfile %s' % (
    #     item.archive_path, item.ipa_path, item.provisioning_profile_name)
    export_options_plist_path = os.getcwd() + '/exportOptions.plist '
    exportIPACmd = r'xcodebuild -exportArchive -archivePath %s -exportPath %s -exportOptionsPlist %s' % (
        item.archive_path, item.ipa_path, export_options_plist_path)
    os.system(exportIPACmd)
    print exportIPACmd
    print 'export ipa finished...\n'

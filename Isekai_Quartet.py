#!/usr/bin/python
# coding=utf-8
from __future__ import print_function, unicode_literals

import datetime, re, os, imp
from bgmi.config import SCRIPT_PATH
from bgmi.lib.fetch import DATA_SOURCE_MAP
file, pathname, desc = imp.find_module('script_extend', [os.path.join(SCRIPT_PATH)])
imp.load_module('script_extend', file, pathname, desc)
from script_extend.script import SearchScriptBase


class Script(SearchScriptBase):
    class Model(SearchScriptBase.Model):
        bangumi_name = '异世界四重奏[简中]'
        cover = 'http://lain.bgm.tv/pic/cover/l/c0/e9/262865_HzIiM.jpg'
        update_time = 'Tue'
        due_date = datetime.datetime(2019, 7, 1)
        source = 'dmhy'
        keyword = '异世界四重奏'

        include_regex_filters = [
            r'(简体中文字幕)',
        ];

        exclude_regex_filters = [
            r'(HEVC|MKV|H265)',
        ];
    

if __name__ == '__main__':
    os.environ["TEST_RUN"] = '1'
    s = Script()
    print(s.get_download_url())

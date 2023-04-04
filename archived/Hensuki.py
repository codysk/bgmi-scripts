#!/usr/bin/python
# coding=utf-8
from __future__ import print_function, unicode_literals

import datetime, re, os, imp
from bgmi.config import cfg
from bgmi.lib.fetch import DATA_SOURCE_MAP
file, pathname, desc = imp.find_module('script_extend', [os.path.join(cfg.script_path)])
imp.load_module('script_extend', file, pathname, desc)
from script_extend.script import SearchScriptBase


class Script(SearchScriptBase):
    class Model(SearchScriptBase.Model):
        bangumi_name = '只要長得可愛，即使是變態你也喜歡嗎？'
        cover = 'http://lain.bgm.tv/pic/cover/l/54/bb/275371_hYbB6.jpg'
        update_time = 'Tue'
        # due_date = datetime.datetime(2019, 10, 1)
        source = 'dmhy'
        keyword = '可爱 变态'

        include_regex_filters = [
            r'(BIG5|繁体|繁體|\[繁\])',
        ];

        exclude_regex_filters = [
            r'(HEVC|MKV|H265)',
        ];
    

if __name__ == '__main__':
    os.environ["TEST_RUN"] = '1'
    s = Script()
    print(s.get_download_url())

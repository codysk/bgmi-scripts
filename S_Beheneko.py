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
        bangumi_name = 'S 級怪獸《貝希摩斯》被誤認成小貓，成為精靈女孩的騎士（寵物）一起生活'
        cover = 'https://lain.bgm.tv/pic/cover/l/0e/9b/485469_qv0QM.jpg'
        update_time = 'Sat'
        # due_date = datetime.datetime(2025, 4, 1)
        source = 'dmhy'
        keyword = 'S级怪兽'

        include_regex_filters = [
            r'(BIG5|繁体|繁體|\[繁\]|繁日|寵物)',
        ];

        exclude_regex_filters = [
            r'(MKV)',
        ];
    

if __name__ == '__main__':
    os.environ["TEST_RUN"] = '1'
    s = Script()
    print(s.get_download_url())

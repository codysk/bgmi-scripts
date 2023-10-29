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
        bangumi_name = '聖女魔力無所不能 S2'
        cover = 'https://lain.bgm.tv/pic/cover/l/44/67/373787_uI776.jpg'
        update_time = 'Tue'
        # due_date = datetime.datetime(2024, 1, 1)
        source = 'dmhy'
        keyword = '圣女 魔力 S2'

        include_regex_filters = [
            r'(BIG5|繁体|繁體|\[繁\]|繁日雙語|繁日)',
        ];

        exclude_regex_filters = [
            r'(HEVC|MKV|H265)',
        ];
    

if __name__ == '__main__':
    os.environ["TEST_RUN"] = '1'
    s = Script()
    print(s.get_download_url())

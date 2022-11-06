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
        bangumi_name = '菜鳥鍊金術師開店營業中'
        cover = 'https://lain.bgm.tv/pic/cover/l/46/88/349317_JKzh6.jpg'
        update_time = 'Mon'
        # due_date = datetime.datetime(2023, 1, 1)
        source = 'dmhy'
        keyword = '新人炼金术'

        include_regex_filters = [
            r'(BIG5|繁体|繁體|\[CHT\])',
        ];

        exclude_regex_filters = [
            r'(HEVC|MKV|H265)',
        ];
    

if __name__ == '__main__':
    os.environ["TEST_RUN"] = '1'
    s = Script()
    print(s.get_download_url())

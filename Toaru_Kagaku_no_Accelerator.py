#!/usr/bin/python
# coding=utf-8
from __future__ import print_function, unicode_literals

import datetime, re, os, imp
from bgmi.config import SCRIPT_PATH
from bgmi.lib.fetch import DATA_SOURCE_MAP
file, pathname, desc = imp.find_module('script_extend', [os.path.join(SCRIPT_PATH)])
imp.load_module('script_extend', file, pathname, desc)
from bgmi.utils import parse_episode
from script_extend.script import SearchScriptBase


class Script(SearchScriptBase):
    class Model(SearchScriptBase.Model):
        bangumi_name = '某科學的一方通行'
        cover = 'http://lain.bgm.tv/pic/cover/l/3f/11/262939_ZhtWQ.jpg'
        update_time = 'Fri'
        # due_date = datetime.datetime(2019, 10, 1)
        source = 'dmhy'
        keyword = '科学 一方通行'

        include_regex_filters = [
            r'(BIG5|繁体|繁體|\[繁\])',
        ];

        exclude_regex_filters = [
            r'(HEVC|MKV|H265|内封)',
        ];

        post_fetch_hooks = [
            "post_fetch",
        ]
        
        @classmethod
        def post_fetch(cls, target, data):
            for i in data:
                title = i['title']
                if i['episode'] != 2019:
                    continue
                title = title.replace('2019', '')
                episode = parse_episode(title)
                i['episode'] = episode
            pass
    

if __name__ == '__main__':
    os.environ["TEST_RUN"] = '1'
    s = Script()
    print(s.get_download_url())

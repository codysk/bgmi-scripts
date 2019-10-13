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
        bangumi_name = '為了女兒，我說不定連魔王都能幹掉'
        cover = 'http://lain.bgm.tv/pic/cover/l/97/29/275352_9TstA.jpg'
        update_time = 'Thu'
        # due_date = datetime.datetime(2019, 10, 1)
        source = 'dmhy'
        keyword = '為了女兒 魔王 幹掉'

        include_regex_filters = [
            r'(BIG5|繁体|繁體|\[繁\])',
            r'1080p'
        ];

        exclude_regex_filters = [
            r'(HEVC|MKV|H265)',
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

#!/usr/bin/python
# coding=utf-8
from __future__ import print_function, unicode_literals

import datetime, re, os, imp
from bgmi.config import cfg
from bgmi.lib.fetch import DATA_SOURCE_MAP
file, pathname, desc = imp.find_module('script_extend', [os.path.join(cfg.script_path)])
imp.load_module('script_extend', file, pathname, desc)
from bgmi.utils import parse_episode
from script_extend.script import SearchScriptBase


class Script(SearchScriptBase):
    class Model(SearchScriptBase.Model):
        bangumi_name = '怕痛的我，把防禦力點滿就對了'
        cover = 'http://lain.bgm.tv/pic/cover/l/c7/35/268545_de5v6.jpg'
        update_time = 'Wed'
        # due_date = datetime.datetime(2020, 4, 1)
        source = 'dmhy'
        keyword = '痛 防御'

        include_regex_filters = [
            r'(BIG5|繁体|繁體|繁)',
        ];

        exclude_regex_filters = [
            r'(HEVC|MKV|H265)',
            r'外挂',
        ];

        post_fetch_hooks = [
            "post_fetch",
        ]
        
        @classmethod
        def post_fetch(cls, target, data):
            for i in data:
                title = i['title']
                if i['episode'] != 0:
                    continue
                matchs = re.findall(r'\.([\d]+)~', title)
                if not matchs:
                    continue
                for match in matchs:
                    index = title.index(match)
                    if index == 0:
                        continue
                    title_list = list(title)
                    title_list[index-1] = ' [%s] ' % match
                    title = ''.join(title_list)
                    pass
                pass
                episode = parse_episode(title)
                i['episode'] = episode
            pass
    

if __name__ == '__main__':
    os.environ["TEST_RUN"] = '1'
    s = Script()
    print(s.get_download_url())

#!/usr/bin/python
# coding=utf-8
from __future__ import print_function, unicode_literals

import datetime, re
from bgmi.script import ScriptBase
from bgmi.lib.fetch import DATA_SOURCE_MAP

TEST_RUN = False

class Script(ScriptBase):
    class Model(ScriptBase.Model):
        bangumi_name = '魔法禁書目錄Ⅲ'
        cover = 'http://lain.bgm.tv/pic/cover/l/be/35/226540_664yS.jpg'
        update_time = 'Fri'
        due_date = datetime.datetime(2019, 4, 1)
        source = 'dmhy'
        _bangumi_id = '魔法禁書目錄第三季 桜都'
    
    def get_download_url(self):
        """Get the download url, and return a dict of episode and the url.
        Download url also can be magnet link.
        For example:
        ```
            {
                1: 'http://example.com/Bangumi/1/1.mp4'
                2: 'http://example.com/Bangumi/1/2.mp4'
                3: 'http://example.com/Bangumi/1/3.mp4'
            }
        ```
        The keys `1`, `2`, `3` is the episode, the value is the url of bangumi.
        :return: dict
        """
        if self.source is not None:
            source = DATA_SOURCE_MAP.get(self.source, None)()
            if source is None:
                raise Exception('Script data source is invalid, usable sources: {}'
                               .format(', '.join(DATA_SOURCE_MAP.keys())))
            ret = {}
            data = source.fetch_episode_of_bangumi(**self._data)
            if TEST_RUN:
                print(data)
            for i in data:
                if TEST_RUN:
                    print(i['title'])
                if not re.search(r'(BIG5|繁体|繁體)', i['title']):
                    if TEST_RUN:
                        print('filter by cond.1')
                    continue;
                if re.search(r'(HEVC|MKV|H265)', i['title']):
                    if TEST_RUN:
                        print('filter by cond.2')
                    continue;
                if int(i['episode']) not in data:
                    if TEST_RUN:
                        print('pass all cond.')
                    ret[int(i['episode'])] = i['download']
            return ret
        else:
            return {}

if __name__ == '__main__':
    TEST_RUN = True
    s = Script()
    print(s.get_download_url())

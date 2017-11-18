# coding: utf-8
from __future__ import unicode_literals

import re
from bs4 import BeautifulSoup

from .common import InfoExtractor
from ..compat import compat_chr
from ..utils import (
    decode_packed_codes,
    ExtractorError,
)


class YourPornIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?yourporn\.sexy/post/(?P<id>[A-Za-z0-9]+)\.html'
    _TESTS = {
        'url': 'https://yourporn.sexy/post/5a0cf9df20c21.html',
        'md5': '17b39f55b5497ae8b59f5fbce8e35886',
        'info_dict': {
            'id': '0f64ce6',
            'title': 'vl14062007715967',
            'ext': 'mp4',
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        print("Working")    

        webpage = self._download_webpage(url, video_id)
        title = self._og_search_title(webpage)
        print(title)
        soup = BeautifulSoup(webpage)
        video_frame = soup.find('div',attrs={'itemprop':'video'})
        video_url = video_frame.find('video',attrs={'id':'player_el'})['src']
        description = video_frame.find('meta',attrs={'itemprop':'description'})['content']
        

        formats = [{
            'format_id': 'sd',
            'url': video_url,
        }]

        return {
            'id': video_id,
            'title': title,
            'formats': formats,
            'description': description,
        }

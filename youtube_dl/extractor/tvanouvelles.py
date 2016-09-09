from __future__ import unicode_literals

from .common import InfoExtractor


class TVANouvellesIE(InfoExtractor):
    _VALID_URL = r'https?://www\.tvanouvelles\.com/.*?'

    _TEST = {
        'url': 'http://www.tvanouvelles.ca/videos/5117035533001',
        'info_dict': {
            'id': '3792260579001',
            'ext': 'mp4',
            'title': 'title',
            'description': 'description',
            'uploader_id': '1741764581',
            'timestamp': 1411116829,
            'upload_date': '20140919',
        },
        'add_ie': ['BrightcoveNew'],
        'skip': 'Not accessible from Travis CI server',
    }
    BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1741764581/default_default/index.html?videoId=%s'

    def _real_extract(self, url):
        program_name = self._match_id(url)
        webpage = self._download_webpage(url, program_name)
        brightcove_id = self._search_regex(
            r'RenderPagesVideo\(\'(.+?)\'', webpage, 'brightcove id')
        return self.url_result(self.BRIGHTCOVE_URL_TEMPLATE % brightcove_id, 'BrightcoveNew', brightcove_id)

from ..schema.site_base import SiteBase
from ..schema.nexusphp import NexusPHP

# auto_sign_in
URL = 'https://hdfans.org/'
SUCCEED_REGEX = '欢迎回来'


class MainClass(NexusPHP):
    @staticmethod
    def build_sign_in(entry, config):
        SiteBase.build_sign_in_entry(entry, config, URL, SUCCEED_REGEX)

    def build_selector(self):
        selector = super(MainClass, self).build_selector()
        self.dict_merge(selector, {
            'details': {
                'hr': None
            }
        })
        return selector

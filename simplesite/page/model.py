from ..model import *

class Page(Content):
    using_options(inheritance='multi')

    path = Field(Unicode, unique=True)
    source = Field(UnicodeText)

class PageProxy(object):

    def __init__(self, ref):
        object.__setattr__(self, 'ref', ref)
        object.__setattr__(self, '__alter__',{})

    def __getattr__(self, key):
        try:
            return self.__alter__['key']
        except KeyError, e:
            return getattr(self.ref, key)

    def __setattr__(self, key, value):
        self.__alter__['key'] = value

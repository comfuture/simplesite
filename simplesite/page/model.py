from ..model import *

## page

class Page(Content):
    using_options(inheritance='multi')

    path = Field(Unicode)



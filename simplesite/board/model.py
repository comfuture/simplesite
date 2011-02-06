from ..model import *

class Board(ContentGroup):
    using_options(inheritance='multi')

    title = Field(Unicode)

class BoardArticle(ListContent):
    using_options(inheritance='multi')



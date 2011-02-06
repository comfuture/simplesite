from ..model import *

class Comment(ListContent):
    using_options(inheritance='multi')

    content = ManyToOne('Content')

Content.comments = OneToMany('Comment', cascade='all')

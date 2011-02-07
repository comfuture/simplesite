from elixir import *
from datetime import datetime

class User(Entity):
    using_options(inheritance='multi')

    email = Field(String)
    name = Field(Unicode)

class Contributer(User):
    using_options(inheritance='multi')

    role = Field(String, default='read')    # read,write,delete
    content = ManyToOne('Content')

class Content(Entity):
    using_options(inheritance='multi')

    id = Field(Integer, primary_key=True)
    author = Field(Unicode)
    contributers = OneToMany('Contributer', cascade='all')
    subject = Field(Unicode)
    content = Field(UnicodeText)
    created_at = Field(DateTime, default=datetime.now)
    updated_at = Field(DateTime, default=datetime.now)

class ContentGroup(Entity):
    using_options(inheritance='multi')

    name = Field(String)
    contents = OneToMany('ListContent', cascade='all')

class ListContent(Content):
    using_options(inheritance='multi')

    group = ManyToOne('ContentGroup')

class Comment(ListContent):
    using_options(inheritance='multi')


from werkzeug.contrib.cache import MemcachedCache
from flask import current_app as app

@app.before_request
def on_before_request():
    # print cached page if exists
    pass

@app.after_request
def on_after_request():
    # do cache this page
    pass

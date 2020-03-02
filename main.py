from flask import Flask
import random
import lorem
import dominate
import datetime
from dominate.tags import *

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    if path == "robots.txt":
        return ""
    has_keyword = random.random() < 0.1
    return gen_page(has_keyword)


def gen_page(has_keyword):
    doc = dominate.document(title="fakenet")
    with doc:
        with div(id='menu').add(ul(id='links')):
            for link in gen_links():
                li(a(link, href=link))

        with div(id='content'):
            with div():
                attr(cls='article')
                span(datetime.datetime.now().date().isoformat(), cls='date')
                if has_keyword:
                    p("attack")
                [p(lorem.paragraph()) for i in range(10)]


    return doc.__str__()

def gen_links():
    links = []
    for i in range(random.randint(0,100)):
        links.append("/%d.html" % i)
    return links


if __name__ == '__main__':
    app.run()

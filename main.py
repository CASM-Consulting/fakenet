from flask import Flask
from flask import request
from flask import Response
import random
import lorem
import dominate
import datetime
from dominate.tags import *

app = Flask(__name__)


link_min=0
link_max=50
keyword_prob=0.6

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    host = request.headers.get("Host")
    print(host)
    if path == "robots.txt":
        return ""
    if path.startswith("sitemap"):
        return sitemap(host)
    has_keyword = random.random() < keyword_prob

    page = gen_page(host, path, has_keyword)
    return Response(page, mimetype='text/html')


def sitemap(host):
    sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://%s/123.html</loc>
      <lastmod>2005-01-01</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
   </url>
</urlset> """ % host
    return sitemap
    
def gen_page(host, path, has_keyword):
    doc = dominate.document(title="fakenet")

    #with doc.head:
    #    link(rel="canonical", href="http://"+host+"/real_"+path)

    with doc:
        with div(id='menu').add(ul(id='links')):
            for l in gen_links():
                li(a(l, href=l))

        with div(id='content'):
            with div():

                attr(cls='article')
                delta = random.randint(0, 10) * -1
                now = datetime.datetime.now().date()
                d = now + datetime.timedelta(delta)

                span(d.isoformat(), cls='date')
                if has_keyword:
                    p("attack")
                [p(lorem.paragraph()) for i in range(10)]


    return doc.__str__()

def gen_links():
    links = []
    for i in range(random.randint(link_min,link_max)):
        l = random.randint(0, 1000)
        links.append("/%d.html" % l)
    return links


if __name__ == '__main__':
    app.run()

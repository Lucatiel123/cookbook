from urllib.request import urlopen
from xml.etree.ElementTree import parse


u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)
print(doc)


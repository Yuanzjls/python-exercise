# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request



#class DefalutSaxhandler(object):
#    def __init__(self):
#        self.d = {}
#    def start_element(self, name, attrs):
#        if 'city' in attrs:
#            self.d['city'] = attrs['city']
#        if  'forecast' in attrs:
#            self.d['forecast'] = attrs['forecast']

#def parseXml(xml_str):
#    handler = DefalutSaxhandler()
#    parser = ParserCreate()
#    parser.StartElementHandler = handler.start_element
#    parser.Parse(xml_str)

#    return handler.d

## 测试:
#URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

#with request.urlopen(URL, timeout=4) as f:
#    data = f.read()

#result = parseXml(data.decode('utf-8'))
#assert result['city'] == 'Beijing'

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.listx = []
        self.temp = {}
        self.flag = 0

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self.flag = 1
        if 'time' == tag:
            self.flag = 2
        if ('class', 'event-location') in attrs:
            self.flag = 3

    #def handle_endtag(self, tag):
    #    print('</%s>' % tag)

    #def handle_startendtag(self, tag, attrs):
    #    print('<%s/>' % tag)

    def handle_data(self, data):
        if self.flag == 1:
            self.flag = 0
            self.temp['event-title'] = data
        elif self.flag == 2:
            self.flag = 0
            self.temp['time'] = data
        elif self.flag == 3:
            self.flag = 0
            self.temp['event-location'] = data
            self.listx.append(self.temp)
            self.temp = {}
    #def handle_comment(self, data):
    #    print('<!--', data, '-->')

    #def handle_entityref(self, name):
    #    print('&%s;' % name)

    #def handle_charref(self, name):
    #    print('&#%s;' % name)

    def print_information(self):
        for inf in self.listx:
            print('Event title: ', inf['event-title'])
            print('Event time: ', inf['time'])
            print('Event location: ', inf['event-location'])
            print('-----------------------------------------------------------------------')


with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')
    Parser = MyHTMLParser();
    Parser.feed(data)
    Parser.print_information()

    

from requests_html import HTMLSession

session = HTMLSession()

r = session.get('http://oracledoc.com')

viewstate = r.html.find('#__VIEWSTATE', first=True)
viewstategenerator = r.html.find('#__VIEWSTATEGENERATOR', first=True)
eventvalidation = r.html.find('#__EVENTVALIDATION', first=True)

post_data = {
        '__VIEWSTATE': viewstate.attrs['value'],
        '__VIEWSTATEGENERATOR': viewstategenerator.attrs['value'],
        '__EVENTVALIDATION': eventvalidation.attrs['value'],
        'btnProcess': 'Download and Process'
        }

print(post_data)

r = session.post('http://oracledoc.com', data=post_data)
print(r.status_code)

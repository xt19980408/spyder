import urllib.request
import urllib.parse
import request
data = urllib.parse.urlencode({'wd':'兔子'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)

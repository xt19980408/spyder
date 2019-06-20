import urllib.request
url = 'http://www.vdposter.bdstatic.com'
response = urllib.request.urlopen(url)
HTML = response.read(.decode('utf8'))
print(HTML)
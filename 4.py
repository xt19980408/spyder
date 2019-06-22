import requests
URLS = []
url='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
repose = requests.get(url)
HTML=reponse.text
print(HTML)
lines = HTML.split('\n')
    for url in RULS:
    reponse = requests.get(url)
    content = repose.content
    with open(name,'wb')as f:
    f.write(content)
    break
 
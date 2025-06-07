import urllib.request
import urllib.error


def verifyUrl(url):
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.URLError:
        return False


site = 'https://www.google.com'
if verifyUrl(site):
    print(f' O site {site} está disponivel.')
else:
    print(f'O site {site} não está disponivel.')
import re, requests


def find_all_href(text):
    return re.findall(r'<a.*?href=["\']?(?:[a-z-]*://)?((?:www.)?[a-z0-9-_.]*)', text)


def test():
    res = requests.get('http://localhost:8000/names2.html')
    names = list(set(find_all_href(res.text)))
    names.remove('')
    names.remove('..')
    names.sort()

    for name in names:
        print(name)


def run():
    res = requests.get(input())
    names = list(set(find_all_href(res.text)))
    if '' in names:
        names.remove('')
    if '..' in names:
        names.remove('..')
    names.sort()
    for name in names:
        print(name)


run()

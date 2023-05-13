import requests, sys, re


def is_valid(url):
    res = requests.get(url)
    return res.status_code == 200 and \
        re.search(r'text/html', res.headers['content-type'])


def replace_stepic(text):
    return text.replace('stepic.org', 'stepik.org')


def has_href(text, href):
    return re.search(r'<a href="{}"'.format(href), text) is not None


def find_all_href(text):
    return re.findall(r'<a href="(.*)"', text)


def can_go(url_from, url_to):
    res_from = requests.get(url_from)
    for href in find_all_href(replace_stepic(res_from.text)):
        res_href = requests.get(replace_stepic(href))
        if has_href(replace_stepic(res_href.text), replace_stepic(url_to)):
            return 'Yes'
    return 'No'


def run():
    count = 0
    args = []
    for line in sys.stdin:
        args.append(line.rstrip())
        count += 1
        if count == 2:
            print(can_go(args[0], args[1]))
            args.clear()


run()
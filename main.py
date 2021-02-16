import sys
from request import request
from parse import search, parse


def main():
    url = sys.argv[1]
    if 'suwen' in url:
        req = request(url)
        return req
    else:
        req = request(url)
        if type(req) == str:
            return req
        sear = search(req)
        cleaner_data = parse(sear)
        print(cleaner_data)
        return cleaner_data


if __name__ == '__main__':
    main()


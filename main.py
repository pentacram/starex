import sys
from request import request
from parse import search, parse


if __name__ == '__main__':
    def main():
        url = sys.argv[1]
        data = []
        if 'suwen' in url:
            req = request(url)
            data.append(req)
        else:
            req = request(url)
            sear = search(req)
            cleaner_data = parse(req)
            data.append(cleaner_data)
        print(data)
        return data


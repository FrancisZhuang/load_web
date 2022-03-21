import requests


class WebGet:
    @staticmethod
    def get_web(url):
        try:
            source = requests.get(url)
            status_code = source.status_code
            content = source.content
        except requests.exceptions.MissingSchema:
            status_code = 404
            content = ''

        output = {
            "Url": url,
            "Status-code": status_code,
            "Content-length": len(content)
        }

        return output


if __name__ == '__main__':
    web_get = WebGet()
    print(web_get.get_web('https://www.bbc.co.uk/iplayer'))

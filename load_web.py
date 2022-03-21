from utils.request_web import WebGet

import sys


class LoadWeb:
    def __init__(self):
        self.output = sys.stdout

    def call_urls(self, user_input):
        web_get = WebGet()
        results = []
        self.output.write(f'Please enter "exit" after finish input urls.\n')

        for line in user_input:
            if 'exit' == line.rstrip().lower():
                self.output.write(f'\nThank you for inputting URLs, please refer to the result below.\n')
                break
            else:
                url = line.rstrip()
                results.append(web_get.get_web(url))

        return results

    def export_result(self, results):
        for result in results:
            self.output.write(f'{result}\n')


def main():
    load_web = LoadWeb()
    results = load_web.call_urls(sys.stdin)
    load_web.export_result(results)


if __name__ == '__main__':
    main()

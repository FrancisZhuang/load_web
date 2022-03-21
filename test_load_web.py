from load_web import LoadWeb

import responses
import unittest


class TestLoadWeb(unittest.TestCase):
    def setUp(self) -> None:
        self.load_web = LoadWeb()

    @responses.activate
    def test_valid_url(self):
        responses.add(**{
            'method': responses.GET,
            'url': 'https://example.com/1',
            'body': 'This is first test',
            'status': 200,
            'content_type': 'text/plain'
        })
        responses.add(**{
            'method': responses.GET,
            'url': 'https://example.com/2',
            'body': 'Oh Oh, it is something with the page',
            'status': 404,
            'content_type': 'text/plain'
        })
        inputs = ['https://example.com/1', 'https://example.com/2', 'exit']
        results = self.load_web.call_urls(inputs)
        self.assertEqual(results[0].get('Url', ''), 'https://example.com/1')
        self.assertEqual(results[0].get('Status-code', ''), 200)
        self.assertEqual(results[0].get('Content-length', ''), 18)

        self.assertEqual(results[1].get('Url', ''), 'https://example.com/2')
        self.assertEqual(results[1].get('Status-code', ''), 404)
        self.assertEqual(results[1].get('Content-length', ''), 36)

    def test_invalid_url(self):
        inputs = ['1', 'exit']
        results = self.load_web.call_urls(inputs)
        self.assertEqual(results[0].get('Url', ''), '1')
        self.assertEqual(results[0].get('Status-code', ''), 404)
        self.assertEqual(results[0].get('Content-length', ''), 0)


if __name__ == '__main__':
    unittest.main()

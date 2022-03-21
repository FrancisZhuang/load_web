# Load Web
You can input multiple web address and it will return the HTTP GET result.

## Install
   pip install -r requirements.txt
## Run the app
   python load_web.py
## Run the test
   python -m unittest


## Import Format
```console
https://example.com/1
https://example.com/2
1
```

## Export Format
```json
{
"Url": "https://example.com/1",
"Status-code": 200,
"Content_length": 18
},
{
"Url": "https://example.com/2",
"Status-code": 404,
"Content_length": 36
},
{
"Url": "1",
"Status-code": 404,
"Content_length": 0
}
```

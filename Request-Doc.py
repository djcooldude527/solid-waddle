import urllib.request as web
url = "https://example-files.online-convert.com/document/txt/example.txt"

with web.urlopen(url) as response:
        text_content = response.read().decode('utf-8') # Decode to handle character encoding
        print(text_content)
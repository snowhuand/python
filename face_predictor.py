
url = 'https://hackattic.com/challenges/basic_face_detection'
output = json.load(urllib.urlopen(url))
print(output)

import json
from six.moves.urllib.request import urlopen

DEFAULT_ENCODING = 'utf-8'
url = 'https://api.github.com/users?since=100'
urlResponse = urlopen(url)

if hasattr(urlResponse.headers, 'get_content_charset'):
    encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
else:
    encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING

output = json.loads(urlResponse.read().decode(encoding))
print(output)
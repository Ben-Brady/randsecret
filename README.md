# Randsecret

Generate a secure randomly generated secret, that is preserved through restarts.

```python
from randsecret import create_secret

SECRET = create_secret("./test.secret", 32)
>>> b'W;\xd8&\r9\x1e\xc3\xfa\xdc\xa0\xc6\x05+\xde\x84\xd1\x8a\xbe\xcf`-$\xc1\x9d-n\x07P\xa1\x95N'
```

## Deleting A secret

```python
from randsecret import create_secret

create_secret("./test.secret", 32)
>>> b'g\x05\x8d\xd2\x83\x1el\xe3\x05\xbfr\xe0)\x9dn\xe5\xe2X\x14\x0c)\xf1sZ\xad\xb4\xeed\x0c\xd6p\x90'

import os
os.unlink("./test.secret")

create_secret("./test.secret", 32)
>>> b'\x90\xe5\\?%\xab\xba\xbb\xe7,\xf9\xe1\x9e\xa8\x11y\x0f\xce\xc4a\xbd\xbaq}x\x11\xea\x8a\xc9/\x12\xd7'
```


## Base32j

Base32 exclude letter `i j l o`, without padding.  
Alphabet: `0123456789abcdefghkmnpqrstuvwxyz`

```bash
pip install base32j
```

Note: Implementation is copy from Python `base64.py`


## Usage

```python
>>> import base32j
>>> s = base32j.encode(b'hello world')
>>> s
'd1kqsv3f41vqywmccg'
>>> base32j.decode(s)
b'hello world'
```

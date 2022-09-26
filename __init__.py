import hashlib
def decode_txt(str2hash):
  result = hashlib.md5(str2hash.encode())
  return result

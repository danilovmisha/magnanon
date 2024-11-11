def checksum(source_string):
    hash = 0
    for char in source_string:
        hash += ord(char)
    return hash

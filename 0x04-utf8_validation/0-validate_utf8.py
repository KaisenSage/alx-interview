def validUTF8(data):
    def check_byte(byte):
        # Check the byte is of the form 10xxxxxx
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]
        if (byte & 0b10000000) == 0:  # 1-byte character (0xxxxxxx)
            i += 1
            continue
        elif (byte & 0b11100000) == 0b11000000:  # 2-byte character (110xxxxx 10xxxxxx)
            count = 1
        elif (byte & 0b11110000) == 0b11100000:  # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            count = 2
        elif (byte & 0b11111000) == 0b11110000:  # 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
            count = 3
        else:
            return False
        
        for j in range(1, count + 1):
            if i + j >= len(data) or not check_byte(data[i + j]):
                return False
        i += count + 1

    return True


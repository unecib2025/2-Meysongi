checksum_original = 'a1b2c3'
checksum_current = 'a1b2c3'
status = 'файл не изменён' if checksum_original == checksum_current else 'файл повреждён'
print(status)
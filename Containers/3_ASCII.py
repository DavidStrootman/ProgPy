def code(invoerstring: str) -> str:
    # Converts string to ASCII magically
    return ''.join([chr(point) for point in [ord(character) + 3 for character in invoerstring]])


print(code('RutteAlkmaarDen Helder'))

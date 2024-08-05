def string_to_hex(input_string):
    byte_data = input_string.encode('utf-8')

    hex_string = byte_data.hex()

    hex_with_prefix = '0x' + hex_string
    return hex_with_prefix

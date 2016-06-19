"""Module to deal with BMP Files"""


def _int32_to_bytes(i):
    return bytes((
        i & 0xff,
        i >> 8& 0xff,
        i >> 16& 0xff,
        i >> 24 & 0xff,
    ))


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale file
    :param filename: ame of file to write
    :param pixels: Image data in binary format
        values in range(0,256)
    """
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, mode="wb") as bmp:
        # BMP Header
        bmp.write(b'BM') # magic block
        size_bookmark = bmp.tell()
        bmp.seek(4, 1) # leave 4 bytes for size 32 bit int
        bmp.seek(4, 1) # empty block in format
        pixel_offset_bookmark = bmp.tell() # holds int offset to pixel data
        bmp.seek(4,1)

        #Image Header # Little endian
        bmp.write(b'\x28\x00\x00\x00') # header size always 40 dec
        bmp.write(_int32_to_bytes(width))
        bmp.write(_int32_to_bytes(height))
        bmp.write(b'\x01\x00') # planes
        bmp.write(b'\x08\x00') # bits/pixel
        bmp.write(b'\x00\x00\x00\x00') # No compression
        bmp.write(b'\x00\x00\x00\x00') # zero for no compression
        bmp.write(b'\x00\x00\x00\x00') # unused pixel per meter
        bmp.write(b'\x00\x00\x00\x00') # unused pixel per meter
        bmp.write(b'\x00\x00\x00\x00') # use whole color table
        bmp.write(b'\x00\x00\x00\x00') # all clrs are imp

        # color pallete = liner grayscale
        for c in range(256):
            bmp.write(bytes(c,c,c,0)) # bgr0

        # pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * (4 - (len(row)%4)) # row must be mult of 4 byte long
            bmp.write(padding)
        # EOF
        eof_bookmark = bmp.tell()

        # fill size
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))
        # fill pixel offset
        bmp.seek(pixel_data_bookmark)
        bmp.write(_int32_to_bytes(pixel_offset_bookmark))






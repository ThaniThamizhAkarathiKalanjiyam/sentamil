import encode.types as taencode
import letters.tamil as tamil

tamil.getTamilLetters(taencode.UTF8)
tamil.getTamilLetters(taencode.TACE16)


print hex(ord('அ'))
print "ஆ".encode("hex")

codepoints = '\xd3\xd3'
print codepoints.decode("latin-1")

import st_encode.types as taencode
import st_letters.tamil as tamil
import st_calendar.tamil_calendar as tacal

tamil.getTamilLetters(taencode.UTF8)
tamil.getTamilLetters(taencode.TACE16)

print hex(ord('அ'))
print "ஆ".encode("hex")

codepoints = '\xd3\xd3'
print codepoints.decode("latin-1")

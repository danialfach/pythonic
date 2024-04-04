print(" ".isspace())
# output ➜ True, karena string berisi karakter spasi

print("\n".isspace())
# output ➜ True, karena string berisi karakter newline

print("\n\r".isspace())
# output ➜ True, karena string berisi karakter newline 

print("hello\n\r".isspace())
# output ➜ False, karena string berisi tulisan hello yang tidak termasuk dalam kategori whitespace
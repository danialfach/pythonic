from typing import Final

# tipe konstanta PI tidak ditentukan secara explisit,
# melainkan didapat dari tipe data nilai
PI: Final = 3.14

# tipe konstanta TOTAL_MONTH ditentukan secara explisit yaitu `int`
TOTAL_MONTH: Final[int] = 12

print("pi: %f" % (PI))
print("Total Month: %d" % (TOTAL_MONTH))

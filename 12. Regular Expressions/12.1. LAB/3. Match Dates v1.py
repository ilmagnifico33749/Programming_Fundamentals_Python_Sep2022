import re

text = "13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016"

regex = "([0-9]{2}[/]{1}[A-Z]{1}[a-z]{2}[/]{1}[0-9]{4})\\b"

filtered_one = re.findall(regex, text)
print(filtered_one)

# --------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------#
# Input_1: 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
# --------------------------------------------------------------------------------------#
# Output_1:
# Day: 13, Month: Jul, Year: 1928
# Day: 10, Month: Nov, Year: 1934
# Day: 25, Month: Dec, Year: 1937
# --------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------#

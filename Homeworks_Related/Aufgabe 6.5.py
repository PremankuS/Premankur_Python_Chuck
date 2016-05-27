text = "X-DSPAM-Confidence:      0.8475"
start = text.find("0")
end = text.find("5")
print start
print end
string = text[start:(end+1)]
print string
float = float(string)
print float
print type(float)
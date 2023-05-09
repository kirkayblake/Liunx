import base64

a = "2310"
b = bytes(a,"UTF-8")
# b = base64.b64encode(b)

print(b,len(b))

c= int(b)
print(c)
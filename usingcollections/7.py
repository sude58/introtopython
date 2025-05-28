# Methods in book
info = "xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh"
splitted_info = info.split(sep=":")
replaced = "+".join(splitted_info)
print(replaced)

# Alternate method
replaced = info.replace(":", "+")
print(replaced)

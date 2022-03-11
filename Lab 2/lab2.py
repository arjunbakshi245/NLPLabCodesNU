with open("words.txt") as f:
    content_list = f.readlines()

content_list = [x.strip() for x in content_list]

for i in content_list:
    if(i[len(i)-3:]=='\n'):
        i=i[:-2]
print(content_list)
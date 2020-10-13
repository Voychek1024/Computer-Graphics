import re



with open("text.txt", 'r') as in_file:
    lines = in_file.readlines()
    for line in lines:
        # print(line)
        print(re.findall(r'>(.*?)</m', line)[0], end='')

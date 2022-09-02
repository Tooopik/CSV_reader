try:
    with open("Data\\access-code-password-recovery-code.csv", "r", encoding="UTF-8") as file:
        content = file.readlines()

    contentList = [line[:-1].split(";") for line in content]
    for line in contentList[1:]:
        print(
            f'First name:{line[3]:<10} | Last name: {line[4]:<10} | Location: {line[6]}')

except OSError:
    print('File not found')

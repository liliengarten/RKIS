def check_line(line):
    if line[:3] == 'abc':
        new_line = 'www' + line[3:]

    else:
        new_line = line + 'zzz'

    return new_line
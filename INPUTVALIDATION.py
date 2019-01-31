def check_invalid_symbols(text):
    check = True
    if ',' in text:
        check = False
    if '\\' in text:
        check = False
    return check

def check_is_digit(text):
    check = False
    if text.isdigit():
        check = True
    return check

def check_len(text,minlen):
    check = False
    if len(text)>=minlen:
        check = True
    return check

def check_len2(text,thelen):
    check = False
    if len(text)==thelen:
        check = True
    return check

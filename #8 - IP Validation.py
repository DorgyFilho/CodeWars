def is_valid_IP(ip):
    oct = ip.split('.')
    if len(oct) != 4: 
        return False
    for o in oct:
        if not is_valid_octet(o):
            return False
    return True

def is_valid_octet(oct):
    if not oct.isdigit():
        return False
    if len(oct) > 1 and oct[0] == '0':
        return False
    oct = int(oct)
    if oct >= 0 and oct <= 255:
        return True
    else:
        return False

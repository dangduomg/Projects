def base_k_repr(n, /, k, order, pad_to=1):
    res = []
    while n > 0:
        res.append(n % k)
        n //= k
    while len(res) < pad_to:
        res.append(0)
    if order == 'big':
        return res[::-1]
    elif order == 'little':
        return res
    else:
        raise ValueError

def digits_groups(n):
    groups = base_k_repr(n, k=1000, order='little')
    return [base_k_repr(g, k=10, order='big', pad_to=3) for g in groups]
    
def digits_groups_names(n):
    dg = digits_groups(n)
    GROUP_NAMES = '', 'thousand', 'million', 'billion'
    if len(dg) > len(GROUP_NAMES):
        raise ValueError
    return list(zip(dg, GROUP_NAMES))
    
def _small_num_textrepr(digits):
    DIGIT_NAMES = '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    TENS_NAMES = '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    SPECIAL_TENS_NAMES = 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    if len(digits) > 3:
        raise ValueError
    hundreds, tens, ones = digits
    if hundreds == 0 and tens == 0 and ones == 0:
        return 'zero'
    res = []
    if hundreds > 0:
        res.append(f'{DIGIT_NAMES[hundreds]} hundred')
    if tens == 1:
        res.append(SPECIAL_TENS_NAMES[ones])
    else:
        if tens > 0:
            res.append(f'{TENS_NAMES[tens]} {DIGIT_NAMES[ones]}')
        elif tens == 0 and ones > 0:
            res.append(DIGIT_NAMES[ones])
    return ' and '.join(res)
    
def english_join(words):
    res = []
    for i, w in enumerate(words):
        res.append(w)
        if i < len(words) - 2:
            res.append(', ')
        elif i == len(words) - 2:
            res.append(' and ')
    return ''.join(res)
    
def num_textrepr(n):
    groups = digits_groups_names(n)[::-1]
    res = []
    for digits, group_name in groups:
        res.append(_small_num_textrepr(digits) + (f' {group_name}' if group_name else ''))
    return english_join(res)
    
    
def main():
    while True:
        inpt = input('enter number: ')
        if not inpt:
            return
        print(num_textrepr(int(inpt)))
        
if __name__ == '__main__':
    main()    
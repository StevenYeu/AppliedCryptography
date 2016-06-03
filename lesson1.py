def convert_to_bits(n,pad):
    result = []
    while n > 0:
        if n % 2 == 0:
            result = [0] + result
        else:
            result = [1] + result
    while len(result) < n :
        result =  [0] + result
    return result

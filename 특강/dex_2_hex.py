def decimal_to_hex(num):
    """
    해당 코드는 Chat GPT를 통해 제작하였습니다.
    
    함수는 입력된 10진수를 16진수 문자열로 변환하여 반환합니다. 
    음수나 부동소수점은 처리하지 않으며, 숫자가 아닌 다른 값이 입력되었을 경우에는 None을 반환합니다.
    
    이 코드에서는 입력값 num이 정수형이 아니거나 음수일 경우 None을 반환하도록 처리하였습니다. 
    이외에는 입력값 num을 16진수 문자열로 변환하여 반환합니다.
    
    """
    if type(num) != int:
        return None
    if num < 0:
        return None
    if num == 0:
        return "0"
    hex_num = ""
    while num > 0:
        rem = num % 16
        if rem < 10:
            hex_num = str(rem) + hex_num
        else:
            hex_num = chr(ord('A') + (rem - 10)) + hex_num
        num = num // 16
    return hex_num
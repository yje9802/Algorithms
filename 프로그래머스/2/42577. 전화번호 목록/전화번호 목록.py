def solution(phone_book):
    hash_map = {}
    
    for number in phone_book:
        hash_map[number] = 1
        
    for number in phone_book:
        temp = ""
        for n in number:
            temp += n
            if temp in hash_map and temp != number:
                return False
    return True
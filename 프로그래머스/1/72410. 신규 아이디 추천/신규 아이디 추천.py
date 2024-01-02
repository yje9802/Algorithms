import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id) # 마침표 2개 이상이면 하나로 replace
    
    for i in range(len(new_id)):
        if new_id[i] != '.':
            new_id = new_id[i:]
            break
    for j in range(len(new_id)-1, -1, -1):
        if new_id[j] != '.':
            new_id = new_id[:j+1]
            break

    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = 'a'
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
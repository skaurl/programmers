import re

def solution(new_id):
    new_id = new_id.lower() # 1단계
    new_id = re.sub(r'[^a-z0-9\-\_\.]', '', new_id) # 2단계
    new_id = re.sub('\.+', '.', new_id) # 3단계
    new_id = re.sub('^\.|\.$', '', new_id) # 4단계
    new_id = 'a' if new_id == '' else new_id[:15] # 5단계
    new_id = re.sub('\.$', '', new_id) # 6단계
    new_id = new_id + new_id[-1]*(3-len(new_id)) if len(new_id) <= 2 else new_id # 7단계
    return new_id
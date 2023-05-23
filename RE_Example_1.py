# 아이디(ID) Regular Expression

import re

ID_regex = re.compile("([A-za-z]{5,15})")
ID_input = input("아이디를 입력하세요 (최소 5자에서 15자, 시작은 영어문자로해야함): ")
ID_validation = ID_regex.search(ID_input.replace(" ",""))

if ID_validation:
    print("사용 가능합니다.")
else:
    print("사용 불가능합니다.")
    
# [-] 안은 범위를 의미
# [A-za-z]는 소문자, 대문자 모두 가능
# {5,15}는 최소 5개 ~ 15개 반복되어야 함

# 참고사항 (역슬래시 + 문자)
# \d : [0-9]와 동일
# \D : [^0-9]와 동일
# \w : [a-zA-Z0-9_]와 동일
# \W : [^a-zA-Z0-9_]와 동일

# 전화번호 Regular Expression

import re

phone_regex = re.compile("^(01)\d{1}-\d{3,4}-\d{4}$")
phone_input = input("전화번호를 입력하세요. (ex: 010-123-1234)): ")
phone_validation = phone_regex.search(phone_input.replace(" ",""))

if phone_validation:
    print("사용 가능합니다.")
else:
    print("사용 불가능합니다.")
    
# ^(01) : 01로 시작해야 함.
# \d{1} : 정수로 하나를 받음.
# {3,4} : 3 ~ 4개를 받음.

# 참고사항 (역슬래시 + 문자)
# \d : [0-9]와 동일
# \D : [^0-9]와 동일
# \w : [a-zA-Z0-9_]와 동일
# \W : [^a-zA-Z0-9_]와 동일

# 포트(Port) Regular Expression

import re

port_regex = re.compile("([0-9]+)~([0-9]+)")
port_input = input("포트 범위를 입력하세요. (EX:0~65535): ")
port_validation = port_regex.search(port_input.replace(" ",""))

if port_validation:
    print("사용 가능합니다.")
else:
    print("사용 불가능합니다.")
    
# [-] 안은 범위를 의미
# +는 반복으로 한번 이상 반복 가능한 것을 의미

# 참고사항 (역슬래시 + 문자)
# \d : [0-9]와 동일
# \D : [^0-9]와 동일
# \w : [a-zA-Z0-9_]와 동일
# \W : [^a-zA-Z0-9_]와 동일

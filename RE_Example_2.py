# 이메일(E-mail) Regular Expression

import re

email_regex = re.compile("([A-Za-z]+[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+)")
email_input = input("이메일을 입력하세요. (ex:inha123@gmail.com)): ")
email_validation = email_regex.search(email_input.replace(" ",""))

if email_validation:
    print("사용 가능합니다.")
else:
    print("사용 불가능합니다.")
    
# [-] 안은 범위를 의미
# +는 1개 이상을 의미

# 참고사항 (역슬래시 + 문자)
# \d : [0-9]와 동일
# \D : [^0-9]와 동일
# \w : [a-zA-Z0-9_]와 동일
# \W : [^a-zA-Z0-9_]와 동일

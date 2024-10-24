# 반갑습니다. 첫번째 고침입니다.

def print_hello(value: str ) -> Str:
    if isinstance(value, str):
        return f'반가워요, {value}'
    else:
        return "This id not string"


if __name__=='__main__':
    print_hello("jong")

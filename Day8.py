#Swap Case

You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.


def swap_case(s):
    st=""
    for ch in s:
        if ch.islower():
            ch=ch.upper()
        else:
            ch=ch.lower()
        st+="".join(ch)
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

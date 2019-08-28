def swap_case(s):

    sep = list(s)

    for i in range(0, len(sep)):
        if  (sep[i].islower()):
            sep[i]=sep[i].upper()
        elif  (sep[i].isupper()):
            sep[i]=sep[i].lower()
        else:
            pass
    junta = "".join(str(item) for item in sep)
    return junta

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

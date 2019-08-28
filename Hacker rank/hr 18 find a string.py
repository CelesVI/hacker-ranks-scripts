def count_substring(string, sub_string):
    cont = 0
    len_ss = len(sub_string)
    for i in range(len(string) - len_ss + 1):
        if string[i:i+len_ss] == sub_string:
            cont += 1
    return cont

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

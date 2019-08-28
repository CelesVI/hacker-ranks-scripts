def split_and_join(line):
    # write your code here
    sep = list(line.split())
    junta="-".join(str(item) for item in sep)
    return junta

    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

import textwrap 

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    lista = wrapper.fill(text=string)
    return lista

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

with open('input.txt') as f:
    string = [char for char in f.read()]


def get_unique_index(string, len_window):
    for i, char in enumerate(string):     
        window = string[i: i + len_window]
        window = [char for char in window if char != '\n']
        if len(window) == len_window:
            if len(set(window)) == len(window):                      
                return i+len_window
                
if __name__ == '__main__':
    print(get_unique_index(string, 4))
    print(get_unique_index(string, 14))


def solution(riddle):
    for char in riddle:
        if char == '?':
            prev_char = riddle.index(char) - 1
            next_char = riddle.index(char) + 1
            letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            for letter in letters_list:
                while letter != prev_char and letter != next_char:
                    char = letter
    return riddle

solution('he?llow?bu?s')


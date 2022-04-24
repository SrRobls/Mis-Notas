#Para este ejercicio NO es para nda necesario los nested loops, como veremos a continuacion.
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += (len(string)-i) 
        else:
            stuart_score += (len(string)-i)
    
    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    elif kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
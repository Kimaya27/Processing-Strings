terms = ['computer', 'ram', 'binary', 'io', 'network', 'ethernet',
         'java', 'yeet', 'printer', 'hexadecimal', 'megabyte',
         'kilobyte', 'bit', 'code', 'python', 'logic', 'algorithm'
         'heuristic', 'fortnite', 'tik tok', 'octal', 'usb',
         'hdmi', 'server', 'ip', 'mountain dew', 'dell' , 'linux',
         'ubuntu', 'windows', 'mac', 'zip', 'compression', 'jpeg', 
         'gif', 'png', 'unicode', 'ascii', 'rom', 'memory', 'mouse',
         'hard drive',  'peripheral', 'rgb', 'byte', 'dvi', 'html',
         'technology', 'idle', 'holy grail', 'operating system',
         'ide', 'javascript', 'css', 'text editor']

# write functions here

def num_letters(word_list):
    ''' return the total number of characters in terms '''

    count = 0

    for word in word_list:
        count += len(word)

    return count


def first_letter_b(word_list):
    ''' return the number of terms with b as the first letter '''

    count = 0

    for word in word_list:
        if word[0] == 'b':
            count += 1

    return count

def has_e_fourth(word_list):
    ''' return the number of terms with e as the fourth letter '''

    count = 0

    for word in word_list:
        if len(word) > 3 and word[3] == 'e':
            count += 1

    return count

def len_word(word_list):
    ''' return the number of 5 character terms '''

    count = 0

    for word in word_list:
        if len(word) == 5:
            count += len(word)

    return count

def longest_term (word_list):
    ''' return the longest term '''

    count = 0

    for word in word_list:
        if len(word) >= 4:
            count +=1

    return count
    
def num_characters_longest_term (word_list):
    ''' return the number of characters in the longest term '''

    count = 0

    for word in word_list:
        if len(word) > count:
            count = len(word)
            
    return count

def average_len (word_list):
    ''' return the average length of all terms '''

    count = 0

    for word in word_list:
        if sum(map(len, word) ) / len(word):
            count += 1

    return count

def has_s_last (word_list):
    ''' return the number of terms with 's' as the last letter '''

    count = 0

    for word in word_list:
        if word [-1] == 's':
            count += 1

    return count
            





# test functions here

print( num_letters(terms) )
print( first_letter_b(terms) )
print( has_e_fourth(terms) )
print( len_word (terms) )
print( longest_term (terms) )
print( num_characters_longest_term (terms) )
print( average_len (terms) )
print( has_s_last (terms) )

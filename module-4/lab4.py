''' count characters excluding specific chars

user_text = input()
exclusion_chars = [' ', ',','.']

for i in exclusion_chars:
    user_text= user_text.replace(i,'')

print(len(user_text))
'''

''' password modifier
word = 'mypassword'
password=''

replacment_characters = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'
}

for key in replacment_characters:
    word = word.replace(key, replacment_characters[key])

password = word + 'q*s'
print(password)
'''

''' Draw right triangle
triangle_char = '%'
triangle_height = 5

for row in range(0, triangle_height):
    for col in range(0, row+1):
        print(triangle_char, end=' ')
    print()
'''

''' mad libs
'''

word = ''
while word != 'quit':
    user_input = input()
    list = user_input.split()
    word = list[0]
    if word != 'quite':
        print('Eating {} {} a day keeps the doctor away.'.format(list[1], word))

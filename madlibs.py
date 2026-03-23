with open('story.txt', 'r') as f: 
#with = it closes the file as soon as code block inside is finished running
#story.txt = the name(and path) of the file you want to access
#'r' = READ mode, w for WRITE, a for APPEND
#f = variable name to the file object
    story = f.read() #.read() = simplest way to get data out of a file once you've opened it. It pulls the entire contents of the file into a single string


words = set() #we use set instead of list because we only want unique inputs
start_of_word = -1

target_start = '<'
target_end = '>'


for i, char in enumerate(story): #enumerate() = i>>index, char>>value
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word) #add is the equivalent of append(for list)
        start_of_word = -1

answers = {}

for word in words: #this gives the key for out dictionary answers
    answer = input(f'Enter a word for {word}:')
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)
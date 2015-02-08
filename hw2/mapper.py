import re
import sys
word_list= ["hackathon", "Dec", "Chicago", "Java"]
word_list_lower = [x.lower() for x in word_list]
for line in sys.stdin:          
    strip_word = line.strip()
    split_word = re.split('\W+', line)
    for word in split_word:
        if word.lower() in word_list_lower:
            print "%s\t%s" % (word, 1)
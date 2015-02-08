import sys
import re
def ignore_case(str1, str2):
	return re.match(re.escape(str1) + r'\Z', str2, re.I) is not None
word_count_dict = {"hackathon":0, "Dec":0, "Chicago":0, "Java":0}
for line in sys.stdin:
    line = line.strip()
    (word, count) = line.split("\t")
    
    for key in word_count_dict:
        if ignore_case(word, key):
        	word_count_dict[key] += int(count)
    
for key in word_count_dict:
	
    print "%s\t%s" % (key,word_count_dict[key])
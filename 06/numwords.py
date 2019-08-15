sentense="The method close closes the opened file. "
sentense+="A closed file cannot be read or written any more."
sentense+="A closed file cannot be read or written any more."
words=sentense.split(' ')
words=sorted(words)
numwords={}
for i in range(0,len(words)):
    if words[i] in numwords:
       numwords[words[i]]+=1
    else:
       numwords[words[i]]=1
print numwords

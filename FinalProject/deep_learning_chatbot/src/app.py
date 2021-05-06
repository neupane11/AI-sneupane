lines=open('../dataset/movie_lines.txt',encoding='utf-8',errors='ignore').read().split('\n')
conversations=open('../dataset/movie_conversations.txt',encoding='utf-8',errors='ignore').read().split('\n')

#pre-process the data
conversation_list=[]
for conversation in conversations:
    conversation_list.append(conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(",","").split())
#print(conversation_list)

dialogue={}
for line in lines:
    dialogue[line.split(' +++$+++ ')[0]]=line.split(' +++$+++ ')[-1]
#print(dialogue)

questions=[]
answers=[]
for conversation in conversation_list:
    for i in range(len(conversation)-1):
        questions.append(dialogue[conversation[i]])
        answers.append(dialogue[conversation[i+1]])
#del all variables... easier for training purpose
del(conversation,conversations,dialogue,conversation_list,i, line, lines)

sorted_quens=[]
sorted_ans=[]
for i in range(len(questions)):
    if len(questions[i])<15:
        sorted_quens.append(questions[i])
        sorted_ans.append(answers[i])
#print(sorted_ans)
#clean text
import re
def trim_text(txt):
    txt = txt.lower()
    txt = re.sub(r"i'm", "i am", txt)
    txt = re.sub(r"he's", "he is", txt)
    txt = re.sub(r"she's", "she is", txt)
    txt = re.sub(r"that's", "that is", txt)
    txt = re.sub(r"what's", "what is", txt)
    txt = re.sub(r"where's", "where is", txt)
    txt = re.sub(r"\'ll", " will", txt)
    txt = re.sub(r"\'ve", " have", txt)
    txt = re.sub(r"\'re", " are", txt)
    txt = re.sub(r"\'d", " would", txt)
    txt = re.sub(r"won't", "will not", txt)
    txt = re.sub(r"can't", "can not", txt)
    txt = re.sub(r"[^\w\s]", "", txt)
    return txt

clean_quens=[]
clean_ans=[]
for line in sorted_quens:
    clean_quens.append(trim_text(line))
for line in sorted_ans:
    clean_ans.append(trim_text(line))
#print(clean_ans)
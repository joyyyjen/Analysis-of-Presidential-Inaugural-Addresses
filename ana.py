#!/usr/local/bin/python3

from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords

import string
from collections import Counter

#print(string.punctuation)
trans =  str.maketrans('','', string.punctuation)
#trans2 = str.maketrans('� ',", ")
#trans3 = str.maketrans('�',"'")

# -- PART 1 --- #
def toClearToken(doc_txt):
    doc_d = open(doc_txt,'r',encoding = 'latin1')
    
    doc_read = doc_d.read()
    #sys.exit()
    #doc_strings = doc_read.translate(trans2)
    #doc_strings = doc_read.translate(trans3)
    doc_strings = doc_read.translate(trans).lower()
    
    #print(len(doc_strings))
    doc_words = word_tokenize(doc_strings)
    doc_d.close()
    return (doc_read,doc_words)
def TTR(words):
    token_len = len(words)
    type_len = len(set(words))
    ttr = type_len / token_len
    return ttr
def sent_count(doc_reader):
    sents = sent_tokenize(doc_reader)
    sumw= 0
    for sent in sents:
        words = word_tokenize(sent)
        sumw = sumw + len(words)
    avg_len = int( sumw / len(sents))
    return (len(sents),avg_len)  
def WordLength(Who,words):
    avg = sum(len(word) for word in words) / len(words)
    avg = round(avg,2)
    print(Who,"avg word length is",avg)
    #return avg
def freq_20(who,words):
    w_20 = Counter(words).most_common(20)
    print(who,"20 most frequent words:",w_20)
def leastFreq(who, words):
    w_freq = list(Counter(words).most_common())
    
    hapax = list()
    four = list()
    for k in w_freq:
        if k[1] == 1: hapax.append(k[0])
        if k[1] <= 4: four.append((k[0],k[1]))
    sum4 = sum([j[1] for j in four])
    #print(len(four),sum4)
    return (hapax,four,sum4)
def freqWord(words):
    word_freqf = list(Counter(words).most_common())
    freq_word = set([k[0] for k in word_freqf])
    #print(len(word_freqf),len(freq_word))
    return (word_freqf, freq_word)
def TopTen(who,freq,diff):
    print('==={}==='.format(who))
    top10 = list()
    i = 0
    for k in freq:
        #print(k[1])
        if k[0] in diff and i <= 10:
            print('{}:\t{}'.format(k[0],k[1]))
            #print(k[0],":\t",k[1])
            i = i+1
def favor(who,word_freqf,all_comm):
    top20 = list()
    i = 0
    for k in word_freqf:
        if k[0] in all_comm and i <= 20:
            top20.append(k)
            i = i+1
    print('{}\'s top 20 Favored Words:{}'.format(who,top20))
    print()

# --- PART 2 --- #
#=== MATTR ===#

from math import floor
def MATTR(doc):
    N = len(doc)
    L = 100
    #print(N,L)
    windows = [tuple(doc[i:i+L]) for i in range(N-(L-1))]
    #print(windows[0:5])
    V = [len(set(i)) for i in windows]
    mattr = sum(V)/(L*(N-L+1))
    return mattr
def Rank(freq):
    prev = freq[0]
    rank = list()
    leng = 1
    r=0
    r1 = 0
    for k in range(1,len(freq)):
        curr = freq[k]
        if prev != curr:
            if leng != 1:
                sum1 = 0
                for i in range(1,leng+1):
                    sum1 = sum1 + r + i
                for i in range(0,leng):
                    rank.append((sum1/leng,prev))
                r = r+leng
            else: 
                r1 = r1+1
                r = r+1
                rank.append((r,prev))
            prev = curr
            leng = 1
        elif prev == curr:
            r1 = r1+1
            leng += 1
    if leng != 1:
        sum1= 0
        for i in range(1,leng+1):
            sum1 = sum1 + r + i      
        for i in range(0,leng):
            rank.append((sum1/leng,prev))   
    
    rank_AvgRank = list()
    for i in range(1,len(rank)+1):
        rank_AvgRank.append((i,rank[i-1]))
    return rank_AvgRank      
#=== STC ===#
# THIS STC counts the words that are not stop words and are adjective, noun or verbs. #
from collections import Counter
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
#stop_words = open("meta_stopwords")
#stop_words = stop_words.read().lower().split()

def STC(doc):
    
    
    doc_freq = list(Counter(doc).most_common())    
    freq_num = [k[1] for k in doc_freq]
    
    r = Rank(freq_num)
    doc_pos = pos_tag([j[0] for j in doc_freq])
    #print(doc_pos)
    used = list()
    
    wf_pair = [ (w,f[1]) for w,f in zip(doc_pos, r)]
    #print(wf_pair[0:10])
    for i in range(0,len(r)):
        #print(r[i][0],r[i][1][0],r[i][1][1]);
        if r[i][0] < r[i][1][1]: continue
        if r[i][0] == r[i][1][1]: 
            h = r[i][0]
            break
        else:
            nume = r[i][1][0]*r[i+1][0] - r[i+1][1][0]*r[i][0]
            deno = r[i+1][0] - r[i][0] + r[i][1][0] - r[i+1][1][0]
            h = nume/deno
            break
    #print(h)
    stc = 0 
    #print(wf_pair[0][0][1])
    for r in range(0,len(wf_pair)):
        #print(r)
        if wf_pair[r][1][0] <= (2*h):
            if "VB" in wf_pair[r][0][1] or "NN" in wf_pair[r][0][1] or "JJ" in wf_pair[r][0][1]:
                if wf_pair[r][0][0] not in stop_words: 
                    used.append(wf_pair[r][0])
                    nume1 = (2*h- wf_pair[r][1][0]) * wf_pair[r][1][1]
                    deno1 = h*(2*h-1) * wf_pair[0][1][1]
                    stc = stc + (nume1/deno1)
        elif wf_pair[r][1][0] > (2*h): break
    #print(used)
    return stc    
#=== Q ===#
from nltk import pos_tag
#nltk.download('averaged_perceptron_tagger')
def Q(doc):
    pos = pos_tag(doc)
    V = 0
    A = 0
    jj = list()
    vb = list()
    for i in pos:
        if "JJ" in i[1]: 
            if i[1] not in jj: jj.append(i[1])
            A = A + 1
        elif "VB" in i[1]:  
            if i[1] not in vb: vb.append(i[1])
            V = V + 1 
    q = V/(V+A)
    #print(V,A)
    #print(vb,jj)
    return q
    
    
def StyIndeces(who,words):
    mattr = round(MATTR(words),2)
    stc = round(STC(words),4)
    q = round(Q(words),2)
    print('{}\'s MATTR:{}, Q:{}, STC:{}'.format(who,mattr,q,stc))



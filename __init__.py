#!/usr/local/bin/python3
from nltk.corpus import stopwords
from collections import Counter
import ana

if __name__ == "__main__":

#--- READER FORMAT and tokenize words ---#

    bush_r, bush_words = ana.toClearToken("Bush.txt")
    obama_r, obama_words = ana.toClearToken("Obama.txt")
    trump_r, trump_words = ana.toClearToken("Trump.txt")
    wash_r, wash_words = ana.toClearToken("Washington.txt")
    
# ---- A ---- #
    print("Bush's speech length:", len(bush_words))
    print("Obama's speech length:", len(obama_words))
    print("Trump's speech length:", len(trump_words))
    print("Washington's speech length:", len(wash_words))

# ---- B ---- # 
    
    ttr_b = round(ana.TTR(bush_words),2)
    ttr_o = round(ana.TTR(obama_words),2)
    ttr_t = round(ana.TTR(trump_words),2)
    ttr_w = round(ana.TTR(wash_words),2)
    print("Bush's Vocab Diversity:",ttr_b)
    print("Trump's Vocab Diversity:",ttr_t)
    print("Obama's Vocab Diversity:",ttr_o)
    print("Washington's Vocab Diversity:",ttr_w)
# ---- C ---- #
    bush_sent, bu_avg_len = ana.sent_count(bush_r)
    obama_sent, ob_avg_len = ana.sent_count(obama_r)
    trump_sent, tr_avg_len = ana.sent_count(trump_r)
    wash_sent, wa_avg_len = ana.sent_count(wash_r)
    print("Bush's num of sentences:", bush_sent, "Average length:",bu_avg_len)
    print("Obama's num of sentences:", obama_sent, "Average length:",ob_avg_len)
    print("Trump's num of sentences:", trump_sent, "Average length:", tr_avg_len)
    print("Washington's num of sentences:", wash_sent,"Average length:",wa_avg_len)
# ---- D ----#
    ana.WordLength("Bush",bush_words)
    ana.WordLength("Obama",obama_words)
    ana.WordLength("Trump",trump_words)
    ana.WordLength("Washington",wash_words)
# ---- E ---- #
    ana.freq_20("Bush",bush_words)
    ana.freq_20("Obama",obama_words)
    ana.freq_20("Trump",trump_words)
    ana.freq_20("Washington",wash_words)
# ---- E2 (FILTER STOP WORDS) ---- #
    stop_words = set(stopwords.words('english'))
    bush_wordf = [w for w in bush_words if w not in stop_words]
    obama_wordf = [w for w in obama_words if w not in stop_words]
    trump_wordf = [w for w in trump_words if w not in stop_words]
    wash_wordf = [w for w in wash_words if w not in stop_words]
    b_c = Counter(bush_wordf).most_common(20)
    o_c = Counter(obama_wordf).most_common(20)
    t_c = Counter(trump_wordf).most_common(20)
    w_c = Counter(wash_wordf).most_common(20)
    print("Bush_20_freq_words:", b_c)
    print("Obama_20_freq_words:", o_c)
    print("Trump_20_freq_words:", t_c)
    print("Washington_20_freq_words:", w_c)    
# ---- F ---- #
    bush_hapax, bush_4,bush_len = ana.leastFreq("Bush",bush_words)
    obama_hapax, obama_4, obama_len= ana.leastFreq("Obama",obama_words)
    trump_hapax, trump_4 ,trump_len= ana.leastFreq("Trump",trump_words)
    wash_hapax, wash_4, wash_len = ana.leastFreq("Washington",wash_words)

    print("Bush's Hapax Legomena:",bush_hapax)
    print("Bush's Words with a Frequency of at most 4:",bush_4);print()
    print("Obama's Hapax Legomena:",obama_hapax)
    print("Obama's Words with a Frequency of at most 4:",obama_4);print()
    print("Trump's Hapax Legomena:",trump_hapax)
    print("Trump's Words with a Frequency of at most 4:",trump_4);print()
    print("Washington's Hapax Legomena:",wash_hapax)
    print("Washington's Words with a Frequency of at most 4:",wash_4);print()
    print("bush_percentage_hapax:",round(len(bush_hapax)/len(bush_words),3),"\tAt most 4:",round(bush_len/len(bush_words),3))
    print("obama_percentage_hapax:",round(len(obama_hapax)/len(obama_words),3),"\tAt most 4:",round(obama_len/len(obama_words),3))
    print("trump_percentage_hapax:",round(len(trump_hapax)/len(trump_words),3),"\tAt most 4:",round(trump_len/len(trump_words),3))
    print("washington_percentage_hapax:",round(len(wash_hapax)/len(wash_words),3),"\tAt most 4:",round(wash_len/len(wash_words),3))
# ---- G ---- #
    wfb, bu_freq = ana.freqWord(bush_wordf)
    wfo, ob_freq = ana.freqWord(obama_wordf)
    wft, tr_freq = ana.freqWord(trump_wordf)
    wfw, wa_freq = ana.freqWord(wash_wordf)
    wa_diff = wa_freq - bu_freq - ob_freq - tr_freq
    bu_diff = ((bu_freq - ob_freq))- wa_freq - tr_freq
    ob_diff = (ob_freq - bu_freq) - wa_freq - tr_freq
    tr_diff = (tr_freq - bu_freq) - ob_freq - wa_freq
    ana.TopTen("Bush",wfb,bu_diff)
    ana.TopTen("Obama",wfo,ob_diff)
    ana.TopTen("Trump",wft,tr_diff)
    ana.TopTen("Washington",wfw,wa_diff)
# ---- H ---- #
    all_comm = wa_freq & bu_freq & ob_freq & tr_freq
    ana.favor("Bush",wfb,all_comm)
    ana.favor("Obama",wfo,all_comm)
    ana.favor("Trump",wft,all_comm)
    ana.favor("Washington",wfw,all_comm)
    
# ---- PART 2 ----# THIS PART REQUIRED SECTION A RUN FIRSt
    ana.StyIndeces("Trump",trump_words)
    ana.StyIndeces("Obama",obama_words)
    ana.StyIndeces("Bush",bush_words)
    ana.StyIndeces("Washington",wash_words)


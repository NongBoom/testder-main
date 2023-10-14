import pythainlp.util
from pythainlp.util import dict_trie
from pythainlp.corpus.common import thai_stopwords, thai_words
from pythainlp import word_tokenize

# Stop word
thai_stopwords = list(thai_stopwords())

# add words to dict
words = ["ไม่ชอบ","ไม่หล่อ","ไม่สวย","ไม่งาม","ไม่เบื่อ","ไม่รัก","อีทูดี้","อิดอก","กานิเย่","เหว่ง","บาบิกอน","บาบิก้อน","บาบีกอน","บุฟเฟ่","ทปอ","ลาซาด้า",
         "ธนาธร","ฟาโรส","โอฮาน่า","โซคูล","คริป","กกต","เสรีพิศุทธ์","อุงเอิง","แสนสิริ","ไม่ดี","ไม่กิน","ไม่ได้","ไม่สนุก","ไม่แพง","ไม่รู้","ไม่มี","ไม่จริง","การ์นิเย่",
        "บร๊ะเจ้า","คัมแบ็ค","คุชชั่น","ไนซ์","แปลงสีฟัน"]
custom_words_list = set(thai_words())
# add multiple words
custom_words_list.update(words)
trie = dict_trie(dict_source=custom_words_list)

#Function process text
def text_process(text):
    # Remove specific characters and punctuation
    final = "".join(u for u in text if u not in ("?",".",";",":","!",'"',"ๆ","ฯ",">","<","/","-",))
    # Tokenize the text using pythainlp's word_tokenize
    final = word_tokenize(final, custom_dict=trie, engine='newmm')
    # Join the tokens into a string
    final = " ".join(word for word in final if pythainlp.util.isthai(word))
    # Remove Thai stopwords from the text
    final = " ".join(word for word in final.split() if word.lower not in thai_stopwords)
    return final
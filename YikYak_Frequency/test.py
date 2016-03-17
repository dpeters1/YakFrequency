import os.path

base_dir = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
word_dir = os.path.join(base_dir, "Word_Freq_Data")

print word_dir
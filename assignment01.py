# -*- encoding:utf-8 -*-
"""
    2.1. what do you want to acquire in this course？,
         2.2. what problems do you want to solve？,
         2.3. what’s the advantages you have to finish you goal?,
         2.4. what’s the disadvantages you need to overcome to finish you goal?,
         2.5. How will you plan to study in this course period?,
"""


humandaily = """
    humandaily => human_name  jinxing verb activity
    human_name => 小明|小红
    jinxing => 正在|忙着|在
    verb* =>null|verb verb*
    verb => 紧张地|慢悠悠地|急匆匆地|悠闲地
    activity=>吃饭|睡觉|打游戏|散步|看书|听歌
"""

introduction ="""
    introduction => greet , personname comefrom city .
    greet => who hello
    who => 大家|在座的|朋友们
    personname => 刘达|刘以牧
    hello=>你们好|你们好
    comefrom=>来自于|出生于|家乡是
    city=>云南|贵州|湖南|哈尔滨|湖北
"""

import jieba

import random



def generate(grammers, key):
    if key in grammers:
        value = grammers[key]

        return "".join([generate(grammers, j) for j in random.choice(value).split()])
    else:
        return key

def generate_n(grammers, key, n):
    return [ generate(grammers, key) for i in range(n)]

def process_grammer(grammer_str):
    grammer_tree = {}
    for line in grammer_str.split("\n"):
        if not line.strip():continue
        exp, stat = line.split("=>")
        grammer_tree[exp.strip()] = [s.strip() for s in stat.split("|")]
    return grammer_tree



csv_url = "https://github.com/Computing-Intelligence/datasource/raw/master/movie_comments.csv"

import re



def token(txt_str):
    return re.findall("\w+", txt_str)

def cut(str):return list(jieba.cut(str))

def prepare_txt():
    file_path = "/home/cathy/projects/my_testaaaa/train.txt"
    df = pd.read_table(file_path, delimiter="\+\+\$\+\+", names=[0, 1, 2, 3])
    insuranceQA = df[2]

    with open("/home/cathy/projects/my_testaaaa/mytrain.txt", "w") as f:
        for a in insuranceQA:

            # print "".join(token(str(a)))
            f.write("".join(str(a)) + "\n")




import pandas as pd
from collections import Counter
import jieba

if __name__ == "__main__":
    TOKEN = []

    for i, line in enumerate((open("/home/cathy/projects/my_testaaaa/mytrain.txt"))):
        TOKEN += cut(line)

    words_count = Counter(TOKEN)


    def prob_1(word):
        if word not in words_count:
            return 1.0/len(TOKEN)

        return float(words_count[word]) / len(TOKEN)

    TOKEN_2 = ["".join(TOKEN[i:i+2]) for i in range(len(TOKEN)-2)]

    words_count_2 = Counter(TOKEN_2)


    def prob_2(word1, word2):
        if word1 + word2 in words_count_2:
            return float(words_count_2[word1+word2])/len(TOKEN_2)
        return 1.0/len(TOKEN_2)

    # print prob_2(u"房主", u"每年")

    #p(w1w2w3w4) ~ p(w1)*p(w2|w1)*p(w3|w2)*p(w4|w3)

    def get_probablity(str):
        words = cut(str)

        probablity = 1

        for i, word in enumerate(words):
            if i+1 < len(words):
                probablity = probablity * prob_2(word, words[i+1])
        return probablity


    print get_probablity(u"我是否需要提交私人财产车祸索赔的警察报告？")


















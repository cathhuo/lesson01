# -*- encoding:utf-8 -*-

simple_grammar = """
                    sentence => noun_phrase verb_phrase
                    noun_phrase => Article Adj* noun
                    Adj* => null|Adj Adj*
                    verb_phrase => verb noun_phrase
                    Article=> 一个|这个
                    noun=>女人|篮球|桌子|小猫
                    verb=>看着|听着|看见
                    Adj=>蓝色的|好看的|小小的|年轻的
                """
import random

def adj(): return random.choice("蓝色的|好看的|小小的|年轻的".split("|")).strip()

def adj_star():return random.choice([None, adj() + adj_star()])



def generate_langurage(gram, target):
    if target in gram:
        new_expanded = random.choice(gram[target])
        return " ".join(generate_langurage(gram, t) for t in new_expanded)
    else:
        return target


if __name__ == "__main__":
    # print adj_star()
    adj_grammar = """
    Adj* => null | Adj Adj*
    Adj=> 蓝色的| 好看的 | 小小的 | 年轻的
    """

    grammar = {}

    for line in simple_grammar.split("\n"):

        if not line.strip(): continue

        exp, stmt = line.split("=>")

        grammar[exp.strip()] = [s.split() for s in stmt.split("|")]

    print generate_langurage(grammar, "sentence")

    #language model p(w1|w2)*P(w2|w3)*P(w3|w4)*P(w4|w5)*P(w5)






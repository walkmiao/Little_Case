#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 一摞Python风格的纸牌.py
# @Author: lch
# @Date  : 2018/9/10
# @Desc  :
import  collections
import random
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrechDenk:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(i, j)  for j in self.suits for i in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


fd = FrechDenk()
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrechDenk.ranks.index(card.rank)
    return rank_value*len(suit_value) + suit_value[card.suit]


for card in sorted(fd, key=spades_high):
    print(card)
print(len(fd))
print(fd[0])
print(random.choice(fd))
print(fd[:3])
print(fd[12::13])

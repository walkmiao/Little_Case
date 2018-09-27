#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cards.py
# @Author: lch
# @Date  : 2018/9/27
# @Desc  :
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()

class AllCard:
    def __call__(self, *args, **kwargs):
        all_card = [card(rank, suit) for rank in range(1, 14) for suit in ('Heart', 'Black', 'Diamond', 'Square')]
        num = random.randint(1, 51)
        return all_card[num]

class Ace(Card):
    def _points(self):
        return self.rank, self.rank

    def __str__(self):
        return '%s(%s,%s)' % (self.__class__.__name__, self.rank, self.suit)


class Number(Card):
    def _points(self):
        return 1, 10

    def __str__(self):
        return '%s(%s,%s)' % (self.__class__.__name__, self.rank, self.suit)

class Face(Card):
    def _points(self):
        return 10,10

    def __str__(self):
        return '%s(%s,%s)' % (self.__class__.__name__, self.rank, self.suit)


def card(rank, suit):
    if rank == 1:
        return Ace('A', suit)
    elif 2 <= rank <= 10:
        return Number(rank, suit)
    else:
        face = {
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        return Face(face[rank], suit)


c =  AllCard()
for i in range(10):
    print(c())

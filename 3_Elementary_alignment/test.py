#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value


def printCard(C):
  out = [(c.suit + c.value) for c in C]
  print(' '.join(out))


C = [x for x in input().split()]

cards = [Card(c[0], c[1]) for c in C]

for card in cards:
  print("Card suit:" + card.suit + " value:" + card.value)

printCard(cards)

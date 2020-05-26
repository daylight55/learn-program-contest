#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Input line num
num = int(input())
# Input rates
rates = [int(input()) for i in range(num)]

maxv = -100000000000
minv = 100000000000

for i in range(len(rates)):
  maxv = max(maxv, rates[i] - minv)
  minv = min(minv, rates[i])

print(maxv)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def validate_num_input(A, N):
  if len(A) != N:
    print("[ERROR] Number of Input integers is invalid")
    sys.exit()


def bubbleSort(A, N):
  i = 0
  sw = 0
  # Exists neigbor element flag
  flag = True

  while flag:
    flag = False
    j = N - 1
    while j >= i + 1:
      if A[j] < A[j - 1]:
        A[j], A[j - 1] = A[j - 1], A[j]
        flag = True
        sw += 1
      j -= 1
    i += 1
  return A, sw


N = int(input())
A = [int(x) for x in input().split()]

validate_num_input(A, N)
A, sw = bubbleSort(A, N)

print(' '.join(map(str, A)))
print(sw)

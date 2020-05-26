#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def validate_num_input(A, N):
  if len(A) != N:
    print("[ERROR] Number of Input integers is invalid")
    sys.exit()


def bubbleSort(A, N):
  sw = 0
  for i in range(N):
    for j in range(N - 1, i, -1):
      if A[j] < A[j - 1]:
        A[j], A[j - 1] = A[j - 1], A[j]
        sw += 1
  return A, sw


N = int(input())
A = [int(x) for x in input().split()]

validate_num_input(A, N)
A, sw = bubbleSort(A, N)

print(' '.join(map(str, A)))
print(sw)

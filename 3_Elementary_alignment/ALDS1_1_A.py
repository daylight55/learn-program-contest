#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def validate_num_input(A, N):
  if len(A) != N:
    print("[ERROR] Number of Input integers is invalid")
    sys.exit()


def insertionSort(A, N):
  for i in range(N):
    v = A[i]
    j = i - 1
    while j >= 0 and A[j] > v:
      A[j + 1] = A[j]
      j -= 1
    A[j + 1] = v
    print(' '.join(map(str, A)))


N = int(input())
A = [int(x) for x in input().split()]

validate_num_input(A, N)
insertionSort(A, N)

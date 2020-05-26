#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def validate_num_input(A, N):
  if len(A) != N:
    print("[ERROR] Number of Input integers is invalid")
    sys.exit()


def insertionSort(A, N):
  sw = 0
  for i in range(N):
    minj = i
    for j in range(i, N):
      if A[j] < A[minj]:
        minj = j
    A[i], A[minj] = A[minj], A[i]
    if (i != minj):
      sw += 1
  return A, sw


def main():
  N = int(input())
  A = [int(x) for x in input().split()]

  validate_num_input(A, N)
  A, sw = selectionSort(A, N)

  print(' '.join(map(str, A)))
  print(sw)


if __name__ == '__main__':
  main()

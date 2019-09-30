# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 18:04:45 2019

@author: 15927
"""

from sequence import DnaSequence
seq = input("Please input your sequence: ")
#seq = "AGCTCGTACGTCGTACGTACGTACG"
my_seq = DnaSequence(seq)
print(my_seq.seq)
print(my_seq.seqlen)
print(my_seq.seqtype)
print(my_seq.seq_gc())
print(my_seq.rev_com())
my_seq.seq_element()
seq_query = input("Please input your sequence that you want to query: ")
my_seq.sub_seq(seq_query)

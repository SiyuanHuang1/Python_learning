# -*- coding: utf-8 -*-
"""
A class used to describe some imformations about DNA/RNA/protein sequences
Created on Tue Aug  6 11:50:16 2019
@author: hsy
"""

class Sequence():
    def __init__(self, seq):
        #属性1：序列本身
        self.seq = seq
        
        #属性2：序列类型
        set_seq = set(seq)
        set_dna = set("ATGCN")
        set_rna = set("AUGCN")
        set_pro = set("ACDEFGHIKLMNPQRSTVWY")
        if set_seq <= set_dna:
            self.seqtype = "DNA"
        elif set_seq <= set_rna:
            self.seqtype = "RNA"
        elif set_seq <= set_pro:
            self.seqtype = "protein"
        else:
            self.seqtype = "Unknown"
        
        #属性3：序列长度
        self.seqlen = len(seq)
    
        
    #DNA, RNA, protein各种元素的含量
    def seq_element(self):
        element_counts = {}
        for i in self.seq:
            if i in element_counts.keys():
                element_counts[i] += 1
            else:
                element_counts[i] = 1
        
        num = 1
        for key, value in element_counts.items():
            this_key_percent = value / self.seqlen
            print(str(num)+"\t" + key + "\t" + str(value) + "\t" + str(this_key_percent))
            num +=1
            

    #查询是否含有特定的子序列
    #如果有，则返回具体的坐标，从1开始
    #并且将主序列与查询序列的配对关系输出到新文件中，新文件60字符就换行，每行开头有位置编号
    def sub_seq(self, query_seq):
        query_seq_len = len(query_seq)
        times = self.seqlen+1-query_seq_len
        hit_num = 0
        
        for i in range(times):
            part_of_self = self.seq[i:i+query_seq_len]
            if part_of_self == query_seq:
                hit_num += 1
                if hit_num == 1:
                    print("the query seq exists in the ref seq, and the coordinates: \n")
                    print("Num.\tLeft\tRight")
                print(str(hit_num) + "\t" + str(i+1) + "\t" + str(i+query_seq_len))
            
    
    
class DnaSequence(Sequence):
    def __init__(self, seq):
        super().__init__(seq)
        

    #求DNA序列的反向互补序列
    def rev_com(self):
        if self.seqtype == "DNA":
            seq_length = len(self.seq)
            rc_self = ""
            for i in range(1,seq_length+1):
                tmp_base = self.seq[-i]
                if tmp_base == "A":
                    rc_self += "T"
                elif tmp_base == "T":
                    rc_self += "A"
                elif tmp_base == "G":
                    rc_self += "C"
                elif tmp_base == "C":
                    rc_self += "G"
                else:
                    rc_self += "N"
            return rc_self
        else:
            print("Please make sure your sequence is a DNA sequence!")
            
    
    #求DNA序列的GC含量
    def seq_gc(self):
        if self.seqtype == "DNA":
            seq_length = len(self.seq)
            gc_counts = 0
            for i in range(seq_length):
                tmp_base = self.seq[i]
                if tmp_base == "G" or tmp_base == "C":
                    gc_counts += 1
            gc_percent = gc_counts / seq_length
            return gc_percent
        else:
            print("Please make sure your sequence is a DNA sequence!")
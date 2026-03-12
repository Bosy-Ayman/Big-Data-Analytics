#!/usr/bin/env python3

import sys
from collections import defaultdict

def main():
    current_word = None
    document_counts = defaultdict(int)
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            word, doc_info = line.split('\t', 1)
            doc_name, count = doc_info.split(':', 1)
            count = int(count)
        except ValueError:
            continue
        
        if current_word and current_word != word:
            for doc, cnt in document_counts.items():
                print(f"{current_word}\t{doc}:{cnt}")
            document_counts = defaultdict(int)
        
        current_word = word
        document_counts[doc_name] += count
    
    if current_word:
        for doc, cnt in document_counts.items():
            print(f"{current_word}\t{doc}:{cnt}")

if __name__ == "__main__":
    main()
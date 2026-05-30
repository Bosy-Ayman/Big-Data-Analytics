#!/usr/bin/env python3

import sys
from collections import defaultdict

def main():
    current_word = None
    document_counts = defaultdict(int)
    
    # Process each line from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Parse input: word \t document:count
        try:
            word, doc_info = line.split('\t', 1)
            doc_name, count_str = doc_info.split(':', 1)
            count = int(count_str)
        except ValueError:
            # Skip malformed lines
            continue
        
        # If we're moving to a new word
        if current_word and current_word != word:
            # Output the previous word's results
            output_parts = []
            for doc, cnt in sorted(document_counts.items()):
                output_parts.append(f"{doc}:{cnt}")
            
            print(f"{current_word} --> {', '.join(output_parts)}")
            
            # Reset for the new word
            document_counts = defaultdict(int)
        
        # Update current word and counts
        current_word = word
        document_counts[doc_name] += count
    
    # Don't forget to output the last word
    if current_word:
        output_parts = []
        for doc, cnt in sorted(document_counts.items()):
            output_parts.append(f"{doc}:{cnt}")
        
        print(f"{current_word} --> {', '.join(output_parts)}")

if __name__ == "__main__":
    main()


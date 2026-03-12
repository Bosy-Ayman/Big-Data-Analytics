#!/usr/bin/env python3

import sys
import re
import os

def load_stop_words(stopwords_file='stopwords.txt'):
    stop_words = set()
    try:
        if os.path.exists(stopwords_file):
            with open(stopwords_file, 'r') as f:
                for line in f:
                    word = line.strip().lower()
                    if word:
                        stop_words.add(word)
        else:
            # Fallback stop words
            default_stopwords = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
                                'to', 'for', 'of', 'with', 'by', 'from', 'up', 'about', 
                                'into', 'through', 'during', 'before', 'after', 'is', 'are', 
                                'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had']
            stop_words.update(default_stopwords)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    
    return stop_words

def get_filename():
    # For Hadoop Streaming
    filename = os.environ.get('mapreduce_map_input_file', 'unknown')
    return os.path.basename(filename)

def main():
    stop_words = load_stop_words()
    current_filename = get_filename()
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Convert to lowercase and remove punctuation
        line = line.lower()
        line = re.sub(r'[^a-zA-Z0-9\s]', ' ', line)
        
        # Split into words
        words = line.split()
        
        for word in words:
            if len(word) <= 1 or word in stop_words:
                continue
            
            print(f"{word}\t{current_filename}:1")

if __name__ == "__main__":
    main()
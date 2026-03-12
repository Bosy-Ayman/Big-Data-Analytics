#!/usr/bin/env python3

import sys
import re
import os

def load_stop_words():
    stop_words = set()
    # Load stopwords from the current directory (digital-librarian folder)
    stopwords_file = 'stopwords.txt'
    
    try:
        with open(stopwords_file, 'r') as f:
            for line in f:
                word = line.strip().lower()
                if word:  # Only add non-empty words
                    stop_words.add(word)
        print(f"Loaded {len(stop_words)} stop words from {stopwords_file}", file=sys.stderr)
    except FileNotFoundError:
        print(f"Error: {stopwords_file} not found in current directory!", file=sys.stderr)
        print("Using minimal default stop words as fallback", file=sys.stderr)
        # Fallback stop words
        default_stopwords = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
                            'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were']
        stop_words.update(default_stopwords)
    except Exception as e:
        print(f"Error loading stop words: {e}", file=sys.stderr)
        sys.exit(1)
    
    return stop_words

def get_filename():
    # Get the current file name from Hadoop environment

    filename = os.environ.get('mapreduce_map_input_file', '')
    if filename:
        return os.path.basename(filename)
    else:
        # For local testing, return a default name
        return "sample.txt"

def main():
    # Load stop words
    stop_words = load_stop_words()
    
    # Get the document name
    document_name = get_filename()
    
    # Process each line from stdin
    for line in sys.stdin:
        # Remove leading/trailing whitespace
        line = line.strip()
        if not line:
            continue
        
        # Convert to lowercase
        line = line.lower()
        
        # Remove punctuation (keep only letters, numbers, and spaces)
        line = re.sub(r'[^a-zA-Z0-9\s]', ' ', line)
        
        # Split into words
        words = line.split()
        
        # Process each word
        for word in words:
            # Skip empty words
            if not word:
                continue
            
            # Skip single-character words (like 'a', 'i')
            if len(word) <= 1:
                continue
            
            # Skip stop words
            if word in stop_words:
                continue
            
            # Output: word \t document_name:1
            print(f"{word}\t{document_name}:1")

if __name__ == "__main__":
    main()

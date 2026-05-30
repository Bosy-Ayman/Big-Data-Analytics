#!/bin/bash

mkdir -p books
cd books

echo "Downloading books"

wget -O pride_and_prejudice.txt https://www.gutenberg.org/files/1342/1342-0.txt
wget -O war_and_peace.txt https://www.gutenberg.org/files/2600/2600-0.txt
wget -O alice_in_wonderland.txt https://www.gutenberg.org/files/11/11-0.txt
wget -O huckleberry_finn.txt https://www.gutenberg.org/files/76/76-0.txt
wget -O great_expectations.txt https://www.gutenberg.org/files/1400/1400-0.txt
wget -O crime_and_punishment.txt https://www.gutenberg.org/files/2554/2554-0.txt
wget -O brothers_karamazov.txt https://www.gutenberg.org/files/28054/28054-0.txt
wget -O les_miserables.txt https://www.gutenberg.org/files/135/135-0.txt
wget -O don_quixote.txt https://www.gutenberg.org/files/996/996-0.txt
wget -O frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt
wget -O dracula.txt https://www.gutenberg.org/files/345/345-0.txt
wget -O tale_of_two_cities.txt https://www.gutenberg.org/files/98/98-0.txt
wget -O oliver_twist.txt https://www.gutenberg.org/files/730/730-0.txt
wget -O journey_to_center_earth.txt https://www.gutenberg.org/files/3748/3748-0.txt

echo "Done!"
ls -lh
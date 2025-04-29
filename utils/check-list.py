
file = input("What file should be read? -> ")
word_amount = int(input("How many words are in todays puzzle? "))
counter = 1
words_found = 0
fileH = open(file, 'r').readlines()

while counter <= word_amount:
    query = input(f"Enter word {counter} to query -> ")

    found = False  # Track whether the query was found

    for line in fileH:
        line = line.strip()
        if line == query:
            print(f"{query} found in {file}")
            found = True
            words_found += 1
            break

    if not found:
        print(f"No match found for {query} in {file}")

    counter += 1
print(f"Found {words_found} / {word_amount} words !!")

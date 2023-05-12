import matplotlib.pyplot as plt
import string

def count_letter_occurrences():
    # Open the file in read mode
    with open("data.txt", "r") as file:
        # Read the content of the file
        content = file.read()

    # Convert the content to uppercase for case-insensitive counting
    content = content.upper()

    # Initialize a dictionary to store the occurrences of each letter at the beginning of a word
    occurrences = {letter: 0 for letter in string.ascii_uppercase}

    # Split the content into words
    words = content.split()

    # Count the occurrences of each letter at the beginning of a word
    for word in words:
        if len(word) > 0:
            first_letter = word[0]
            if first_letter in occurrences:
                occurrences[first_letter] += 1

    # Calculate the total number of letters at the beginning of a word
    total_letters = sum(occurrences.values())

    # Calculate the percentage of presence for each letter
    percentages = {letter: (count / total_letters) * 100 for letter, count in occurrences.items()}

    # Generate the histogram
    letters = list(percentages.keys())
    presence_percentages = list(percentages.values())

    plt.bar(letters, presence_percentages)
    plt.xlabel('Letters at the beginning of words')
    plt.ylabel('Percentage of presence')
    plt.title('Presence of letters at the beginning of words in the file data.txt')
    plt.show()

# Call the function
count_letter_occurrences()

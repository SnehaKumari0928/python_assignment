from collections import Counter

try:
    with open("sample.txt","r") as file:
        content = file.read()
        content = content.split()
        count = Counter(content)
        print("Total words:", len(content))
        unique_words = []
        for word in content:
            if word not in unique_words:
                unique_words.append(word)

        print("Unique words:",unique_words)
        top_five =  count.most_common(5)


        print("Top 5 most common words:", count.most_common(5))

        print("Words appearing only once:",len(unique_words))

except FileNotFoundError as e:
    print(e)



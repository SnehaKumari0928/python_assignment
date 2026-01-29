from collections import Counter

def analyze_file(filename):
    try:
        with open(filename,"r") as file:
            content = file.read().lower()
            words = content.split()
            count = Counter(words)

            total_words = sum(count.values())
            unique_words = len(count)
            top_five = count.most_common(5)
            once_words = [word for word, count  in count.items() if count == 1 ]

            return {
                "total_words": total_words,
                "unique_words": unique_words,
                "top_five": top_five,
                "once_words": once_words
            }
  
    except FileNotFoundError:
        print("Error: File not found")
        return None

stats = analyze_file("sample.txt")

if stats:
    print("File analizes for 'sample.txt'")
    print("Total words:", stats["total_words"])
    print("Uniqure words:",stats["unique_words"])
    print("Top five:", stats["top_five"])
    print("Once words", stats["once_words"])


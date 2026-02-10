from word_count.core import word_count

def main():
    cnt = word_count("sample.txt")
    print("Top 10 words:")
    for word, freq in cnt.most_common(10):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()

# def reverse_words_count(sentence: str) -> tuple:
#     if not sentence.strip():
#         return ([], 0)
#
#     words = sentence.split()
#     reversed_words = [word[::-1] for word in words]
#     count = len(words)
#
#     return (reversed_words, count)
#
# print(reverse_words_count("hello world python"))



def filter_numbers(numbers: list, threshold: int) -> list:
    return [num for num in numbers if num >= threshold]

print(filter_numbers([1, 5, 10, 3], 5))
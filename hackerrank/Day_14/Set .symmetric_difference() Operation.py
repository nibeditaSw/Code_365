# Set .symmetric_difference() Operation

number_of_english_subscribers = input()
english_subscribers = set(map(int, input().split()))
number_of_french_subscribers = input()
french_subscribers = set(map(int, input().split()))
print(len(english_subscribers.symmetric_difference(french_subscribers)))
# Alternative solution
# print(len(english_subscribers ^ french_subscribers))
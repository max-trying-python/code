# this is a lambda that combines it's first argument with a reversed, first-char stripped version of itself
palindrome = lambda word: word + word[-2::-1]

print(palindrome(input()))

def palindrome(s):
	k = len(s)
	if k < 2:
		return True
	else :
		return s[0] == s[k-1] and palindrome(s[1:k-1])

print(palindrome(input()))
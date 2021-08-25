def longestCommonPrefix(strs):

	if len(strs) == 0:
	    return '' 
	res = ''
	strs = sorted(strs)
	for i in strs[0]:
	    print(strs[-1])
	    if strs[-1].startswith(res+i):
		res += i
	    else:
		break
	return res

n=input.split()
print(longestCommonPrefix(n))

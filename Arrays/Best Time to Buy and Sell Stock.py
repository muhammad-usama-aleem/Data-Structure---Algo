def maxProfit(prices):
	m, mp = float('inf'), 0
#   float('inf') specify a big very big +ive number
	for p in prices:
		if p < m: m = p
		if p - m > mp: mp = p - m
	return mp

print(maxProfit([7,1,5,3,6,4]))

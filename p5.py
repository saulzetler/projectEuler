# Smallest Multiple

import sys
import time

start_time = time.time()
cur = 20
i = 20


while i > 1:
	if not (cur%i == 0):
		# print i
		i = 20
		cur += 20
	else: i = i - 1

print cur
print("This took", time.time() - start_time, "seconds to run.")




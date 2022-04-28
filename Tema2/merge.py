def merge_sort(l):
	length = len(l)
	if length > 1:
		middle = int(length / 2)
		left_array = l[0 : middle]
		right_array = l[middle : length]
		merge_sort(left_array)
		merge_sort(right_array)
		i = 0
		j = 0
		k = 0
		while i < middle and j < length - middle:
			if left_array[i] < right_array[j]:
				l[k] = left_array[i]
				i += 1
			else:
				l[k] = right_array[j]
				j += 1
			k += 1
		while i < middle:
			l[k] = left_array[i]
			k += 1
			i += 1
		while j < length - middle:
			l[k] = right_array[j]
			k += 1
			j += 1
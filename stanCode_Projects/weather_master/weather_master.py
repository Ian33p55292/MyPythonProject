"""
File: weather_master.py
Name: Ian
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -1

def main():
	"""
	The weather report that tell you the highest temperature,
	lowest temperature, average temperature, and cold days
	among the input temperature data.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	"""
	data_t: input temperature data
	"""
	data_t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data_t == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data_t
		minimum = data_t
		total = data_t  # total: the sum of the values of input temperature data
		count = 1  # count: the number of input temperature data
		cold_days = 0
		if data_t < 16:  # add the number of cold days(<16 Celsius degree)
			cold_days += 1
		while True:
			data_t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data_t == EXIT:
				break
			if data_t > maximum:
				maximum = data_t
			if data_t < minimum:
				minimum = data_t
			if data_t < 16:
				cold_days += 1
			total += data_t  # renew the total when one temperature data is added
			count += 1  # renew the count when one temperature data is added
		average = total / count
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold_days) + ' cold day(s)')


	# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()

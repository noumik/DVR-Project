with open('results.txt', 'w') as results:
	for line in open('timings.srt'):
		if line.startswith('0'):
				results.write(line[0:2])
				results.write(line[3:5])
				results.write(line[6:8])
				results.write(line[9:12])
				results.write(line[17:19])
				results.write(line[20:22])
				results.write(line[23:25])
				results.write(line[26:29])
				results.write("\n")
		#       print(line[0:12])
from jtop import jtop
import csv

with jtop() as jetson:
    # Make csv file and setup csv
    with open("logger.csv", 'w') as csvfile:
        stats = jetson.stats
        # Initialize cws writer
        writer = csv.DictWriter(csvfile, fieldnames=stats.keys())
        # Write header
        writer.writeheader()
        # Write first row
        writer.writerow(stats)
        # Start loop
        while jetson.ok():
            stats = jetson.stats
            # Write row
            writer.writerow(stats)
            print("Log at {time}".format(time=stats['time']))
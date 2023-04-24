from jtop import jtop
import csv
from threading import Thread


def log_utils(model, size, dataset, t):
    with jtop() as jetson:
        # Make csv file and setup csv
        with open(f"utils_logger_{dataset}_{model}_{size}_{t}.csv", 'w') as csvfile:
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
                
t = Thread(target = log_utils, args =(10, ), daemon = True)
t.start()

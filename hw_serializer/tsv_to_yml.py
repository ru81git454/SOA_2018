
from ruamel import yaml
import sys
with open(sys.argv[1], 'r') as tsv:
    lines = list(map(lambda x: x.strip().split('\t'), tsv))
    keys = lines[0]
    values = list(map(lambda v: v, lines[1:]))
    array = []
    for value in values:
            new_dict = {k: v for k, v in zip(keys, value)}
            array.append(new_dict)

# Dumper = yaml.RoundTripDumper
# print(yaml.dump(array, Dumper = yaml.RoundTripDumper), end='')
with open(sys.argv[2], 'w') as file:
    yaml.dump(array, file, Dumper=yaml.RoundTripDumper)
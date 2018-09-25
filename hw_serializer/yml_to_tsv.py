from ruamel import yaml
import sys

with open(sys.argv[1], 'r') as infile:
    text = yaml.load(infile)

title = '\t'.join(text[1].keys())

contents = list(map(lambda x: x.values(), text))
contents = list(map(lambda x: '\t'.join(x), contents))
contents.insert(0, title)
with open(sys.argv[2], 'w') as outfile:
    outfile.write("\n".join(contents))
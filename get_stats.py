import sys
from collections import Counter
from google.protobuf import text_format

from protos import interaction_pb2

input_file = sys.argv[1]

num_tables = 0
num_columns = 0


col_counter = Counter()
with open(input_file) as fin:
    for line in fin:
        num_tables += 1
        if num_tables == 5:
            break
        line = line.strip()
        interaction = text_format.Parse(line, interaction_pb2.Interaction())
        col_names = [c.text for c in list(interaction.table.columns)]
        col_counter.update(col_names)

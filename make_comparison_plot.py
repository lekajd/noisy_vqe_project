import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'input_paths',
    nargs='+',
    type=str, # Automatically convert input string to a Path object
    help='Paths to any input data files for analysis'
)
parser.add_argument(
    "-f",
    "--filename",
    type=str,
    required=False,
    help="Name to attach to relevant files"
)
args = parser.parse_args()

assert len(args.input_paths) > 0
data_paths = args.input_paths
print("Data Paths:", data_paths)

labels = ['Op1_Depol', 'Op1_Adamp',
          'Op2_Depol', 'Op2_Adamp',
          'Op3_Depol', 'Op3_Adamp']

# Plot the first one and get axis object
df = pd.read_csv(data_paths[0])
ax = df.plot(kind='line', x='err_per_1q_gate', y='mean_normalized_err', label=labels[0])

# Plot others if they exist
for i,data_path in enumerate(data_paths[1:]):
    df = pd.read_csv(data_path)

    df.plot(kind='line', x='err_per_1q_gate', y='mean_normalized_err', ax=ax, label=labels[i+1])

ax.set_xlabel("Single-Qubit Gate Error")
ax.set_ylabel("Final VQE Error")

if args.filename != None:
    plt.savefig(args.filename + '.png')

# plt.show()


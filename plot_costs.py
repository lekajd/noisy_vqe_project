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
parser.add_argument(
    "-o",
    "--observable",
    type=int,
    required=False
)
args = parser.parse_args()

print(args.input_paths)
assert len(args.input_paths) == 1
data_path = args.input_paths[0]
print(data_path)

# Plot the first one and get axis object
df = pd.read_csv(data_path)
# ax = df.plot(kind='line', y='', label=data_paths[0][:10])

ax = df.plot(kind='line')

actuals = [0, -6.0, -2.0, -1.0]
if args.observable is not None:
    plt.axhline(y=actuals[args.observable], linestyle=':', color='gray')

ax.set_xlabel("Minimizer Iteration")
ax.set_ylabel("Cost (Energy) Estimate")


# # Plot others if they exist
# for data_path in data_paths[1:]:
#     df = pd.read_csv(data_path)

#     df.plot(kind='line', x='err_per_1q_gate', y='mean_normalized_err', ax=ax, label=data_path[:10])

if args.filename != None:
    plt.savefig(args.filename + '.png')

# plt.show()


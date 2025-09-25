import argparse

parser = argparse.ArgumentParser(
		prog='Aodoo',
		description='A tool for odoo developing',
		epilog='Stay the reading of our swan song and epilogue'
	)

parser.add_argument('-g', '--generate', action='store_true')
parser.add_argument('-m', '--module', action='store_true')
parser.add_argument('-a', '--app', action='store_true')
parser.add_argument('-M', '--model', action='store_true')
parser.add_argument('-v', '--view', action='store_true')
parser.add_argument('-s', '--security', action='store_true')
parser.add_argument('-n', '--name', type=str) # NOTE: here the name of the module/model/view gets passed
parser.add_argument('-vm', '--view_model')

print(parser.parse_args())

import json
import pip
import importlib
failed = []
with open('dependencies.json', 'r') as f:
	dependencies = json.load(f)
	for d, v in dependencies['Dependencies'].items():
		try:
			importlib.import_module(d)
		except ImportError:
			if pip.main(['install', '--user', d+v]) == 1:
				failed.append(d)
		else:
			print(d + " is already installed")
print("\nFollowing packages were not installed:\n")
if len(failed) == 0:
	print("Success")
else:
	for package in failed:
		print(package)
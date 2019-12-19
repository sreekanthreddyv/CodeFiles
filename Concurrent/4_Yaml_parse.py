import yaml

# print(dir(yaml))
with open('Ex_Yaml.yaml') as f:
	df = yaml.load(f)

print(df)

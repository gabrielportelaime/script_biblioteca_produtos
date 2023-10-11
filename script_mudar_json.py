import json

# Abrir o arquivo orders.json
with open("biblioteca.json") as file:
	data = json.load(file)
	count = 0
	for i in range(len(data)):
		for j in range(len(data[i]['produtos'])):
			muda_garantia = False
			for k in range(len(data[i]['produtos'][j]['atributos_e_valores'])):
				if(data[i]['produtos'][j]['atributos_e_valores'][k]['valor'] == 'Lacrado'):
					count += 1
					muda_garantia = True
					break
			if(muda_garantia):
				data[i]['produtos'][j]['garantia'] = 12
		# for j in range(len(data[i]['atributos'])):
		# 	for k in range(len(data[i]['atributos'][j]['children'])):
		# 		if(data[i]['atributos'][j]['children'][k]['valor'] == 'Lacrado'):
		# 			count += 1

print(count, 'Produtos modificados!')

with open("bibliotecaProdutos.json", 'w') as file:
    json.dump(data, file, indent=4)

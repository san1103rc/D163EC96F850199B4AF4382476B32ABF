def linearScarchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["shart", "pant", "tshart", "shoes","lofer"]
target = "shoes"
result = linearScarchProduct(products, target)
print(result)
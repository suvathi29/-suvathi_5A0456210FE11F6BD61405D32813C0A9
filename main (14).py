







def LinearSearchProduct(productList,targetProduct):
  indices = []

  for index, Product in enumerate(productList):
    if Product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
Product = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target2 = 'apple'
result = LinearSearchProduct(Product, target)
print(result)









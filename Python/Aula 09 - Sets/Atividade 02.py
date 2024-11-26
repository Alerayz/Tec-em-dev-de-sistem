estoque_loja_a = set(['Air Max TL 2.5 Black and Metallic Silver', 'Womens Air Max SNDR Black', 'NOCTA Nike Hot Step 2 Black', 'Air Max Dn Light Bone and Light Taupe'])
estoque_loja_b = set(['Nocta x Nike Hot Step 2', 'Air Max Dn Light Bone and Light Taupe', 'Womens Air Max SNDRHyper Pink and Black', 'Zoom Vomero Roam Racer Blue'])

produtos_em_ambas = estoque_loja_a.intersection(estoque_loja_b)

produtos_exclusivos_a = estoque_loja_a.difference(estoque_loja_b)

produtos_exclusivos_b = estoque_loja_b.difference(estoque_loja_a)

print("Produtos disponíveis em ambas as lojas:", produtos_em_ambas)
print("Produtos exclusivos da loja A:", produtos_exclusivos_a)
print("Produtos exclusivos da loja B:", produtos_exclusivos_b)
### Como Usar
Primeiro, verifique se todos os pacotes necessários estão devidamente instalados. O código deve provavelmente rodar em diferentes versões de pacotes e do Python, mas foi apenas testado nas versões apontadas.

Basta rodar no terminal o código python "solution.py", seguido do caminho para o arquivo YAML. Como no exemplo a seguir:
```
python solution.py examples/example_1.yaml
```

### Saída
O programa exibe duas informações no terminal assim que é finalizado. O primeiro indica o valor de distância entre as imagens, e o seguinte indica se as duas imagens representam o mesmo produto ou não. O cálculo é feito baseado no valor de threshold do arquivo YAML. 

Exemplo de saída:
```
distância: 0.22856307324787906
Produtos diferentes
```

Além disso, o programa também salva um arquivo de imagem que contém as duas imagens de entrada processadas e aglutinadas lado a lado.

### Formato YAML Esperado
Para o arquivo YAML de entrada, são esperado 4 campos: 

- Dois campos referentes as imagens dos produtos a serem comparados, "image_a" e "image_b". Eles devem conter o caminho, em formato de string, para as respectivas imagens. 

- Um campo referente ao caminho de saída, "ouput_location", também em string. Este deve conter o caminho e nome de arquivo para a imagem de saída.

- Um campo referente ao valor de limiar para a diferença entre os produtos, o "threshold"

Exemplo de arquivo YAML esperado:
```
image_a: products/product_a.jpg
image_b: products/product_b.jpg
threshold: 0.28
output_location: example_1_concatenated.jpg
```


### Depêndencias e Versões Usadas no Enviroment
```
Python                3.10.11
numpy                 2.0.0
opencv-contrib-python 4.10.0.84
pydantic              2.8.2
PyYAML                6.0.2
scipy                 1.14.0
```
from nltk.corpus import wordnet
from nltk.wsd import lesk
print('Задание 1. синсеты для лексемы plant:',wordnet.synsets('plant'))
set1 = wordnet.synset('plant.n.01')
print('Задание 2. определение для лексемы plant в значении "завод":', set1.definition())
set2 = wordnet.synset('plant.n.02')
print('Задание 2. определение для лексемы plant в значении "растение":',set2.definition())
sent1 = 'emily scraped away the dead leaves to reveal the tiny shoot of a new plant'.split()
sent2 = 'factory manufacturing chemicals is often called plant and may have most of equipment like tanks, pressure vessels, chemical reactors'.split()
print('Задание 3:', lesk(sent1, 'plant').definition())
print('Задание 3:', lesk(sent2, 'plant').definition())
print('Задание 4. гиперонимы для значения 1:', wordnet.synset('plant.n.01').hypernyms())
print('Задание 4. гиперонимы для значения 2:', wordnet.synset('plant.n.02').hypernyms())
plant1 = wordnet.synset('plant.n.01')
plant2 = wordnet.synset('plant.n.02')
similarity = []
for i in wordnet.synsets('industry'):
    similarity.append(wordnet.path_similarity(plant1,i))
similarity.sort()
print('Задание 5. Наименьшее расстояние между значением plant "завод" и значениями лексемы industry:', similarity[0])

similarity1 = []
for i in wordnet.synsets('leaf', 'n'):
    similarity1.append(wordnet.path_similarity(plant1,i))
similarity1.sort()
print('Задание 5. Наименьшее расстояние между значением plant "завод" и значениями лексемы leaf:', similarity1[0])

similarity2 = []
for i in wordnet.synsets('industry'):
    similarity2.append(wordnet.path_similarity(plant2,i))
similarity2.sort()
print('Задание 5. Наименьшее расстояние между значением plant "растение" и значениями лексемы industry:', similarity2[0])

similarity3 = []
for i in wordnet.synsets('leaf', 'n'):
    similarity3.append(wordnet.path_similarity(plant2,i))
similarity3.sort()
print('Задание 5. Наименьшее расстояние между значением plant "растение" и значениями лексемы leaf:', similarity3[0])

word1 = wordnet.synset('plant.n.02')
word2 = wordnet.synset('rattlesnake_master.n.01')
print(word2.definition())
print("Задание 6. Расстояние между plant(растение) и rattlesnake's master:", wordnet.path_similarity(word1,word2))

word3 = wordnet.synset('organism.n.01')
print(word3.definition())
word4 = wordnet.synset('whole.n.01')
print(word4.definition())
print("Задание 6. Расстояние между organism и whole:", word3.path_similarity(word4))

#В первом случаем расстояние больше соответствует интуитивным представлениям, во всяком случае растение и средство от укусов можно соотнести друг с другом. Но во втором случае я была очень удивлена, что расстояние такое маленькое  - всего 0, 08.



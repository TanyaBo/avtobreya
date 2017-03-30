import os
import re
import codecs
import sys
import gensim, logging
import pandas as pd
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from nltk import word_tokenize
stop = stopwords.words('russian')
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix

m = 'C:/Users/user/Documents/4 курс/avtobreya/дз6/ruscorpora_1_300_10.bin.gz' # скачиваю модель, натренированную на НКРЯ и подгружаю ее
model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)

path = 'C:/Users/user/Documents/4 курс/avtobreya/дз6/texts'
vectors_anekdots = []# создаю массивы, в которые будут складываться усредненные вектора по текстам из каждого класса
vectors_izvest = []
vectors_teh = []
count = 0 # создаю счетчик документов, всего будет 375
for root, dirs, files in os.walk(path):# последовательно прохожусь по всем трем папкам(анекдоты, газета, журнал)
    for filename in files: # для каждого файла в папке
        open_name = os.path.join(root, filename)
        f = codecs.open(open_name, 'r', 'utf-8-sig')
        vectors = [] # создаю массив, куда будут складываться все вектора слов в одном файле
        for line in f:
            line = line.lower()
            line = re.sub(r"['_,!\-\"\\\/}{?\.()<>&*+;:|$%«»]", '', line).strip()
            line = line.split(' ') #очищаю текст файла от запятых, делю на слова
            for i in line: # для каждого слова в тексте
                try:
                    if i != '' and i != None and i not in stop:
                        normal = morph.parse(i)[0].normal_form
                        tag = morph.parse(normal)[0].tag.POS
                        word = normal + '_' + tag # записываю его начальную форму и часть речи
                        if word in model:
                            vectors.append(model[word]) # считаю для него 300 векторов
                except:
                    pass
        # print(len(vectors))
        average_vector = sum(vectors) / len(vectors) # Теперь усредняю все вектора слов в тексте
        #print(average_vector)
        count += 1 # веду счетчик файлов
        if count <= 125:
            vectors_anekdots.append(vectors)#если файл из первой папки(первые 125 документов), записываю усредненные вектора 125 файлов в массив
        if 125 < count <= 250:
            vectors_izvest.append(vectors)# если файл из второй папки(вторые 125 документов), записываю усредненные вектора 125 файлов в другой массив
        if count > 250:
            vectors_teh.append((vectors))# если файл из третьей папки(третьи 125 документов), записываю усредненные вектора 125 файлов в третий массив

df0 = pd.DataFrame(vectors_anekdots)# из каждого массива создаю датафрейм
df1 = pd.DataFrame(vectors_izvest)
df2 = pd.DataFrame(vectors_teh)

data = pd.concat([df0, df1, df2])# соединяю вместе датафреймы
#print(df.head())

#df['type'] = ['anekdot' for _ in range(125)] + ['izvest' for _ in range(125)] + ['teh_mol' for _ in range(125)] #добавляю новую колонку и присваиваю ей тип текста(источник)

#Строю классификатор

# X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:300], df['type'], test_size=0.2)
# clf = LogisticRegression(penalty="l2", solver="lbfgs", multi_class="multinomial", max_iter=300, n_jobs=4)
# clf.fit(X_train, y_train)
# y_pred = clf.predict(X_test)
# print(classification_report(y_test, y_pred))

# Результатов так и не дождалась, работало всю ночь...очень долго грузит
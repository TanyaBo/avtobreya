import nltk
import pymorphy2
from nltk.collocations import *
from nltk.metrics.spearman import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
morph = pymorphy2.MorphAnalyzer()
stopwords = nltk.corpus.stopwords.words('russian')

punct = '.,!?():;'
words = [word.strip(punct) for word in open('court-V-N.txt', encoding='utf-8').read().split()]#очистка и лемматизация
words_tagged = [morph.parse(word)[0].normal_form for word in words]
finder = BigramCollocationFinder.from_words(words_tagged)
finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in stopwords)# удаляем стопслова и короткие слова

log = finder.nbest(bigram_measures.likelihood_ratio, 5000)# сортируем коллокации по мере коллокационной связи, используя метрику LogLikelihood
##print(log)
pmi = finder.nbest(bigram_measures.pmi, 5000)#сортируем коллокации по мере коллокационной связи, используя метрику PMI
##print(pmi)
gold = [('выдать', 'санкция'), ('вынести', 'постановление'),('принять', 'решение'), #создаем Золотой стандарт
        ('доказать', 'незаконность'), ('удовлетворить','иск'),('избрать', 'мера'),
        ('начаться', 'рассмотрение'), ('отказать', 'удовлетворение'),
        ('подтвердить', 'решение'), ('наложить', 'арест')]
log_ranks = []
pmi_ranks = []
for i in gold:
    log_rank = (i,log.index(i))
    log_ranks.append(log_rank)# выбираем коллокации из ЗС с их показателями метрики LogLikelihood 
    pmi_rank = (i,pmi.index(i))
    pmi_ranks.append(pmi_rank)# выбираем коллокации из ЗС с их показателями метрики PMI
    

log_ranks = sorted(log_ranks,key = lambda x: x[1])
log_colloc = []
for i in log_ranks:
    log_colloc.append(i[0])
print(log_colloc)#отсортировываем 10 коллокаций из ЗС по убыванию показателей метрики LogLikelihood и добавляем в новый массив только сами коллокации

pmi_ranks = sorted(pmi_ranks,key = lambda x: x[1])
pmi_colloc = []
for i in pmi_ranks:
    pmi_colloc.append(i[0])
print(pmi_colloc)#отсортировываем 10 коллокаций из ЗС по убыванию показателей метрики PMI добавляем в новый массив только сами коллокации

gold_ranks = list(ranks_from_sequence(gold))
gold_colloc = []
for i in gold_ranks:
    gold_colloc.append(i[0])
print(gold_colloc)#в массив добавляем только коллокации без рангов

print('%0.1f' % spearman_correlation(ranks_from_sequence(gold_colloc), ranks_from_sequence(pmi_colloc)))
print('%0.1f' % spearman_correlation(ranks_from_sequence(log_colloc), ranks_from_sequence(gold_colloc)))
print('%0.1f' % spearman_correlation(ranks_from_sequence(pmi_colloc), ranks_from_sequence(log_colloc)))


# В дз2 я создала Золотой стандарт(Gold), куда определила 10, наиболее частотных,
#по моему мнению,биграмм встречающихся со словом "суд". Затем я извлекла эти коллокации
#с их частотностью из 2-х списков. В первом списке была использована метрика PMI
#(Pointwise Mutual Information)для определения наиболее частотных коллокаций,
#во втором списке - Log-Likelihood. Возникли сложности
#с подсчетом корреляции, но в итоге, согласно результатам (0,2%) обе метрики одинаково справляются с оценкой коллокационной связи. 
# На мой взгляд, корреляция должна была получиться большей при использовании первого метода(Log),
# так как при сравнении первых 10 наиболее частотных коллокаций из первого списка и золотого
#стандарта было найдено около 4-5 совпадений. Не очень понятно, почему корреляция считается
#по порядку следования коллокаций в списке, а не по номеру ранга, что на мой взгляд, имело бы более показательный результат.




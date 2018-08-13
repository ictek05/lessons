from statistics import variance
import numpy as np

s = [1,2,3,45,6,7,8,9,5,34,6,4,234,566,755,345]

print(np.std(s))  # стандартное отклонение выборки  standard_deviation

print(np.std(s, ddof=1))  # about ddof = http://qaru.site/questions/86702/why-does-numpy-std-give-a-different-result-to-matlab-std
print(np.mean(s)) #поиск среднего
print(np.var(s)) #отклонение

# useful docs = https://howtorecover.me/vvedenie-v-statistiku-s-ispolzovaniem-numpy

cv =  lambda x: (np.var(s) / np.mean(s))  #функция коэфициента вариации - lambda - функция "на ходу"

print (cv(s))
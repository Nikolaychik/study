import pickle, glob
for filename in glob.glob('*.pkl'):
recfile = open(filename, 'rb')
record = pickle.load(recfile)
print(filename, '=>\n ', record)
suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])
# для 'bob','sue','tom'
# извлечь имя Сью  
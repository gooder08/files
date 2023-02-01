f1 = open('1.txt', 'rt', encoding='utf-8')
f2 = open('2.txt', 'rt', encoding='utf-8')
f3 = open('3.txt', 'rt', encoding='utf-8')
final = open('final.txt', 'w', encoding='utf-8')
a = f1.readlines()
b = f2.readlines()
c = f3.readlines()

final.write(f'{f2.name}\n{len(b)}\n{"".join(b)}\n'
            f'{f1.name}\n{len(a)}\n{"".join(a)}\n\n'
            f'{f3.name}\n{len(c)}\n{"".join(c)}')

f1.close()
f2.close()
f3.close()
final.close()

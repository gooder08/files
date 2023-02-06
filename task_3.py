f1 = open('1.txt', 'rt', encoding='utf-8')
f2 = open('2.txt', 'rt', encoding='utf-8')
f3 = open('3.txt', 'rt', encoding='utf-8')
final = open('final.txt', 'w', encoding='utf-8')
final_list = []
a = f1.readlines()
b = f2.readlines()
c = f3.readlines()
final_list.append(f'{f1.name}\n{str(len(a))}\n{"".join(a)}\n')
final_list.append(f'{f2.name}\n{str(len(b))}\n{"".join(b)}\n')
final_list.append(f'\n{f3.name}\n{str(len(c))}\n{"".join(c)}\n')
final_list.sort(key=len)
final.write("".join(final_list))


f1.close()
f2.close()
f3.close()
final.close()

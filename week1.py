# import csv

# with open('mpg.csv') as csvfile:
#     mpg = list(csv.DictReader(csvfile))

# cylinders = set(d['cyl'] for d in mpg)

# print(cylinders)

# ctyMpgByCyl = []

# for c in cylinders:
#     summpg = 0
#     cyltypecount = 0
#     for d in mpg:
#         if d['cyl'] == c:
#             summpg += float(d['cty'])
#             cyltypecount += 1
#     # ctyMpgByCyl.append((c, '{0:.2f}'.format(summpg / cyltypecount)))
#     ctyMpgByCyl.append((c, round(summpg / cyltypecount, 2)))
# # how about a more 'pythonic' way to do this?

# ctyMpgByCyl.sort(key=lambda x: x[0])

# print(ctyMpgByCyl)

# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson',
#           'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


# def split_title_and_name(person):
#     title = person.split()[0]
#     lname = person.split()[-1]
#     return '{0} {1}'.format(title, lname)


# formatted_names = list(map(split_title_and_name, people))

# print(formatted_names)

# for person in people:
#     print(split_title_and_name(person) == (lambda x: '{0} {1}'.format(x.split()[0], x.split()[-1]))(person))


# def times_tables():
#     lst = []
#     for i in range(10):
#         for j in range(10):
#             lst.append(i * j)
#     return lst


# # print(times_tables())

# print([i * j for i in range(10) for j in range(10)])


# generate all possible combos of xx99

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = ['{0}{1}{2:02}'.format(c1, c2, n)
          for c1 in lowercase
          for c2 in lowercase
          for n in range(100)]

print(len(answer))
# for i in range(len(answer)):
#     if i % 10000 == 0:
#         print(answer[i])

# answer = [???]
# correct_answer == answer

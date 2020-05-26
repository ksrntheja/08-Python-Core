import random
import time

names = ['Name01', 'Name02', 'Name03', 'Name04']
subjects = ['Python', 'Java', 'Blockchain']


def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'subject': random.choice(subjects)
        }
        results.append(person)
    return results


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(subjects)
        }
        yield person


t1 = time.clock()
people = people_list(100000)
t2 = time.clock()
print('List took {}'.format(t2 - t1))

t1 = time.clock()
people = people_generator(100000)
t2 = time.clock()
print('Generator took {}'.format(t2 - t1))

# List took 0.130469
# Generator took 0.005947000000000008

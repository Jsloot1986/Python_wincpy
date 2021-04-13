from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())


def unique_koala_facts(target):
     count = 0
     fact_set = set()
     while count <= target:
         fact = random_koala_fact()
         count += 1
         fact_set.update([fact])
     else:
         return sorted(fact_set)

print(unique_koala_facts(20))

def num_joey_facts(target):
    count = 0
    joey_facts = set()
    counter = set()
    while count < target:
        fact = random_koala_fact()
        if "joey" in fact:
            count += 1
            joey_facts.update([fact])
            counter.update([count])
        else:
            continue
    return joey_facts, counter

print(num_joey_facts(10))

def koala_weight(target):
    new_list = set()
    count = 0
    while count < target:
        fact = unique_koala_facts(20)
        count += 1
        item = '14kg'
        new_list.update(fact)
        if target >= 20:
            for i in new_list:
                if item in i:
                    return item
                else:
                    continue

print(koala_weight(20))
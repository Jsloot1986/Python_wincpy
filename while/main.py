from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())


def unique_koala_facts(target: int) -> list:
     count = 0
     fact_list = []
     while count < 50:
         if len(fact_list) == target:
             break
         else:
             fact = random_koala_fact()
             if fact not in fact_list:
                 fact_list.append(fact)
             else:
                 count = + 1
     return fact_list

print(unique_koala_facts(30))

def num_joey_facts(target: int) -> list:
    count = 0
    joey_facts = set()
    while count < 20:
        if len(joey_facts) == target:
            break
        else:
            fact = random_koala_fact()
            if "joey" in fact:
                joey_facts.update([fact])
            else:
                count =+ 1
    return joey_facts

print(num_joey_facts(20))

def koala_weight(target: int) -> int:
    weight_koala = []
    count = 0
    while count < 30:
        if len(weight_koala) == target:
            break
        else:
            fact = random_koala_fact()
            if "14kg" in fact:
                weight_koala.append(fact)
            else:
                count += 1
    return str(weight_koala).find("kg")

print(koala_weight(20))
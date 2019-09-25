#Functions
def make_dough(ingredient1, ingredient2):
    if (ingredient1 == 'wheat' and ingredient2 == 'water') or (ingredient1 == 'water' and ingredient2 == 'wheat'):
        return 'dough'
    else:
        return 'not dough'

def wood_oven(ingredient1):
    if ingredient1 == 'dough':
        return 'Naan bread'
    else:
        return 'not bread'

def run_naan_factory(ingredient1, ingredient2):
    dough_r = make_dough(ingredient1, ingredient2)
    result_bread = wood_oven(dough_r)
    return result_bread

#Calling of Functions
print(make_dough('fire','stones'))
print('////////')
print(run_naan_factory('sand', 'water'))
print('////////')
#Tests TDD
#As a user i can add 'wheat' and 'water' to the function make_dough, so that I can make 'dough'.
                        #evaluates --> True or False (Boolean)
print('Testing make_dough, with wheat and water --> dough to come out')
print(make_dough('wheat', 'water') == 'dough')

print("Testing make_dough, with 'sand' and 'cement' --> dough to come out")
print(make_dough('sand', 'cement') == 'not dough')

#As a user I can pass 'dough' to the function wood_oven, so that I can make bread
print('Testing wood_oven, with dough --> Naan bread to come out')
print(wood_oven('dough') == 'Naan bread')

print('Testing wood_oven, with burnt dough --> Naan bread to come out')
print(wood_oven('burnt dough') == 'not bread')
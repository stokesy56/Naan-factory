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
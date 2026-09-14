from ducks import Duck,compare_duck_height,compare_duck_age
from functools import cmp_to_key

if __name__=='__main__':
    daffy=Duck('Daffy',4,2)
    eui=Duck('Eui',1,4)
    loui=Duck('loui',5,4)
    donald=Duck('Donald',5,6)

    duck_array=[daffy,eui,loui,donald]

    sorted_ducks_by_age=sorted(duck_array,key=cmp_to_key(compare_duck_age))
    sorted_ducks_by_height=sorted(duck_array,key=cmp_to_key(compare_duck_height))
    sorted_duck_by_name=sorted(duck_array,key=lambda x:len(x.name))
    print(f'duck array: {duck_array}')
    print(f'sorted array by age: {sorted_ducks_by_age}')
    print(f'sorted array by height: {sorted_ducks_by_height}')
    print(f'sorted array by name length: {sorted_duck_by_name}')
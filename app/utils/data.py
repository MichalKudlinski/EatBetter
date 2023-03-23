import pandas as pd

foods_all_columns = pd.read_csv("nutrition.csv")

foods_all_columns.rename( columns={'Unnamed: 0':'id'}, inplace=True )
foods_useful_columns = foods_all_columns[['id','name','serving_size','calories','total_fat','protein','carbohydrate','sugars','fiber']]


if (foods_useful_columns['serving_size'] == foods_useful_columns['serving_size'][0]).all():
    print('all_values_same')


foods_useful_columns.drop(columns = 'serving_size', inplace = True)

foods_useful_columns['total_fat'] = foods_useful_columns['total_fat'].str.replace('g','')
foods_useful_columns['protein'] = foods_useful_columns['protein'].str.replace('g','')
foods_useful_columns['carbohydrate'] = foods_useful_columns['carbohydrate'].str.replace('g','')
foods_useful_columns['sugars'] = foods_useful_columns['sugars'].str.replace('g','')
foods_useful_columns['fiber'] = foods_useful_columns['fiber'].str.replace('g','')


foods_useful_columns['total_fat'] = foods_useful_columns['total_fat'].map(lambda x: float(x))
foods_useful_columns['protein'] = foods_useful_columns['protein'].map(lambda x: float(x))
foods_useful_columns['carbohydrate'] = foods_useful_columns['carbohydrate'].map(lambda x: float(x))
foods_useful_columns['sugars'] = foods_useful_columns['sugars'].map(lambda x: float(x))
foods_useful_columns['fiber'] = foods_useful_columns['fiber'].map(lambda x: float(x))


foods_useful_columns = foods_useful_columns[foods_useful_columns.calories !=0]


foods_useful_columns['nutrition_score'] = foods_useful_columns.apply(lambda x: (x['protein'] + x['fiber']) / x['calories'], axis  =1)
foods_final = foods_useful_columns.sort_values(by = 'nutrition_score',ascending = False)[0:100]
print(foods_final.shape)
print(foods_final)


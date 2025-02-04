movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1 function that takes a single movie and returns True if its IMDB is above 5.5
print('№1')
def im():
    import random
    a = random.randrange(0, len(movies), 1)
    if(movies[a]['imdb'] > 5.5):
        return True
    else:
        print(movies[a])
        return False
print(im())

#2 function that returns a sublist of movies with an IMDB score above 5.5.
print('№2')
def db():
    my_list = []
    for i in range(0, len(movies)):
        if movies[i]['imdb'] > 5.5:
            my_list.append(movies[i]['name'])
    return my_list
print(db())

#3 function that takes a category name and returns just those movies under that category.
print('№3')
def category_name(category):
    for i in range(0, len(movies)):
        if movies[i]['category'] == category:
            print(movies[i]['name'], end=' | ')
    return ' '
print(category_name('Romance'))

#4 function that takes a list of movies and computes the average IMDB score.
print('№4')
def avg(mov):
    x = 0
    for i in range(0, len(mov)):
        for j in range (0, len(movies)):
            if mov[i] == movies[j]['name']:
                x += movies[j]['imdb']
    return round(x / len(mov), 2)

mov = ['Hitman', 'The Help']
print(avg(mov))

#5  function that takes a category and computes the average IMDB score.
print('№5')
def avg_imdb(category):
    x = 0
    cnt = 0
    for i in range(0, 15):
        if movies[i]['category'] == category:
            x += movies[i]['imdb']
            cnt += 1
    return round(x / cnt, 2)

print(avg_imdb('Romance'))
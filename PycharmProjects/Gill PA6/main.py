import statistics
myfile = "/Users/simar/Downloads/A6F24data.txt"
ratings= []
with open(myfile, "r") as file:
    s = file.readline()
    while s:
        firstname = s[0:19 + 1]
        print(f'Rater: {firstname}')



        age_str = s[25:26 + 1].strip()
        if age_str.isdigit():
            age = int(age_str)
        if age >= 78:
            print(f'Age: {age} silent')
        elif age < 78 and age >= 59:
            print(f'Age: {age} baby boomer')
        elif age < 59 and age >= 43:
            print(f'Age: {age} gen x')
        elif age < 43 and age >= 27:
            print(f'Age: {age} millenial')
        elif age < 27 and age >= 4:
            print(f'Age: {age} gen z')

            print(f'{firstname} rated 7 movies')

        for line in file:
                    movie = line[0:16]
                    rating = int(line[20:21].strip())
                    ratings.append(rating)
                    genre = line[21:22]
                    if genre == "C":
                        print(f'Movie: {movie}   Comedy     Rating: {rating} ')
                    elif genre == "R":
                        print(f'Movie: {movie}  Rom Com     Rating: {rating} ')
                    elif genre == "A":
                        print(f'Movie: {movie}   Action     Rating: {rating} ')
                    elif genre == "S":
                        print(f'Movie: {movie}  Sci-fi      Rating: {rating} ')
                    elif genre == "H":
                        print(f'Movie: {movie}   Horror     Rating: {rating} ')
                    elif genre == "D":
                        print(f'Movie: {movie}   Drama      Rating: {rating} ')

        break
average_rating= float(statistics.mean(ratings))
print(f'Average rating: {average_rating: .2f}')



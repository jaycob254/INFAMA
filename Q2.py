
#Function that selects exactly 2 movies to watch within duration of a flight
def flight_movies(flight_hrs,movies):
  #Empty list/array
  towatch=[]

  for each in movies:
  

    try:
      #Subtract flight_hrs from duration of the first movie. Then find the movie with the difference as duration in the movie list. If one exists, append the indexes of the two movies to the towatch list/array. If none exists in the first iteration exists, move to the next iteration.
      # The try catch statement is for handling ValueError if a movie duration is not found in the movies list/array.
      other=flight_hrs-each
      x=movies.index(other)
      towatch.append(movies.index(each))
      towatch.append(x)
      break
    

    except ValueError:
      # print("Hakuna kama hio") 
      continue
    
  return towatch

print(flight_movies(540,[60,120,180,240,300]))
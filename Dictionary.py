#looping through a dictionary 
1) keys()
fav_sports = {"amrita":"cricket","pooja":"ludo","khushi":"badminton"
             }
for k in fav_sports.keys():
  print(k)
  #output: amrita
           #pooja
           #khushi

  2) values()
  for v in fav_sports.values():
    print(v)
    o/p: cricket
         ludo
         badminton 

3) keys values both .items()
for k,v in fav_sports.items():
  print(k+"fav game"+v)



             
             
             
             
             
             

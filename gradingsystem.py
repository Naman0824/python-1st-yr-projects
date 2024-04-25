more_enteries=True
while more_enteries:
      while True:
            name=input('Enter Name Of Student : ')
            if name.isnumeric():
                  print('please enter only albhabetic characters')
            else:
                  break
      while True:
            try:
                  subjects=int(input('enter number of subjects student have : '))
                  if subjects<1:
                        raise ValueError('please enter valid value ')
                  elif subjects>15:
                        raise ValueError('too many subjects please enter subjects range from 1 to 15 only')
                  else:
                        break
            except ValueError as e:
                  print(e)
      l=[]
      for i in range (subjects):
            while True:
                  try:
                        print("enter marks of subject of ",i+1,' : ',end=' ')
                        marks=float(input())
                        if marks<1 or marks>100:
                              raise ValueError('please enter marks from 1 to 100 only')
                        else:
                              l.append(marks)
                              break
                  except ValueError as e:
                        print(e)
      total_marks=0
      for i in l:
            total_marks+=i
      avg=total_marks/subjects
      
      if avg<40:
            print('')
            print('------------------------------')
            print('Student result : fail')
            print('Student average score is ',avg)
            print('Student subjects wise score :- ')
            for i in range(len(l)):
                  print('score in subject ',i+1,' is = ', l[i] )
      elif avg>=40 and avg <=50:
            print('')
            print('------------------------------')
            print('Student GRADE IS : C')
            print('Student average score is ',avg)
            print('Student subjects wise score :- ')
            for i in range(len(l)):
                  print('score in subject ',i+1,' is = ', l[i] )
      elif avg>=51 and avg<=60:
            print('')
            print('------------------------------')
            print('Student GRADE : B')
            print('Student average score is ',avg)
            print('Student subjects wise score :- ')
            for i in range(len(l)):
                  print('score in subject ',i+1,' is = ', l[i] )
      elif avg>=61 and avg <=70:
            print('')
            print('------------------------------')
            print('Student GRADE : B+')
            print('Student average score is ',avg)
            print('Student subjects wise score :- ')
            for i in range(len(l)):
                  print('score in subject ',i+1,' is = ', l[i] )
      elif avg>=71 and avg <=80:
            print('')
            print('------------------------------')
            print('Student GRADE : A')
            print('Student average score is ',avg)
            print('Student subjects wise score :- ')
            for i in range(len(l)):
                  print('score in subject ',i+1,' is = ', l[i] )
      elif avg>=81 and avg <=90:
            print('')
            print('------------------------------')
            print('Student GRADE : A+')
            print('Student average score is ',avg)
            print('Student subjects wise score :- ')
            for i in range(len(l)):
                  print('score in subject ',i+1,' is = ', l[i] )
      elif avg>=91 and avg <=100:
            print('')
            print('------------------------------')
            print('Student GRADE : O ')
            print('Student average score is ',avg)
            print('Student subjects wise score :- ')
            for i in range(len(l)):
                  print('score in subject ',i+1,' is = ', l[i] )
      while True:
            try:
                  more_ent=int(input('for MORE ENTERIES press 1 \nTO QUIT press any numeric value other than 1 : '))
                  if more_ent <1 and more_ent>2:
                        raise ValueError('please enter valid input only')
                  else:
                        break
            except ValueError as e:
                  print(e)
      if more_ent==1:
            continue
      else:
         more_enteries=False
"""
TODO:
проверка центральной и правой дороги,не показывать текст камни когда
ты проехал по дороге

"""

name ='Илья Муромец'


way_left = False
way_center = False
way_right = False

while way_left == False or way_center == False or way_right == False:
  print('надпись:')
  print('налево поехать убитым быть,')
  print('прямо поехать богатым быть,')
  print('направо поехать женатым быть,')

  way = input('в какую сторону ехать? ')
  if way == 'налево':
      if way_left == False:
        print(name, 'убит')
        way_left = True
      else:
        print(name,'уже был тут')
  elif way == 'прямо':
      if way_center == False:
          print()
     print(name,'богат')
     way_center = True
  elif way == 'направо':
     print(name,'женат')
     way_right = True
  else:
     print('Нет такой дороги')
     
print('конец игры')
     
    
   

    

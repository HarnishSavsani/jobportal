def my_function():
      x=int(input())
      y=int(input())
      z=int(input())

      thor = int(z-x)
      loki = int(z-y)

      if (thor > loki):
        print(thor)
      elif (loki>thor):
        print(loki)
      elif (loki == thor):
        print(loki)


loop = input()

for i in range(1,int(loop)):
    my_function()
        






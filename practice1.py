
#!/usr/bin/python3

list=[1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=" ")




class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)

n=5
counter=1
while counter <= n:
    print(next(myiter))
    counter = counter + 1


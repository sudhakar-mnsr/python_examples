class Name:
   def __init__(self,first,last,middle):
      self.Last=last
      self.Middle=middle
      self.First=first
   def __str__(self):
      return self.First + ' ' +self.Middle + ' ' + self.Last
   def initials(self):
      return self.First[0]+self.Last[0]+self.Middle[0]

aName=Name('Manukonda','NSR','Sudhakar')
bName=Name('Manukonda','ESV','Krupakar')

print aName
print aName.initials()

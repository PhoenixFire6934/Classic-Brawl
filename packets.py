self = ""

self.writeVint(2)  # Battle End Screen Type
self.writeVint(1)  # Rank Score
self.writeVint(0)  # Battle Tokens
self.writeVint(0)  # Trophies Value
self.writeVint(0)  # Doubled Tokens
self.writeVint(0)  # Token Doubler Remaining
self.writeVint(0)  # Unknown
self.writeVint(32)  # Type (Capped XP, Star Token, Capped Tokens)

# Player start
self.writeVint(1)  # End Screen Players
for player in Players:
    self.writeString(self.player.name)  # Your Name

    self.writeVint(1)

    self.writeScId(16, 0)  # BrawlerID
    self.writeScId(29, 0)  # SkinID

    self.writeVint(9999)  # Brawler Trophies
    self.writeVint(10)  # Brawler Power Level

    boolean = self.writeBoolean(False)
    if boolean == True:
        self.writeInt(0)  # HighID
        self.writeInt(1)  # LowID
# Player end

# Array1 start
value = self.writeVint(0)
for i in range(value):
    self.writeVint(0)
    self.writeVint(0)
# Array1 end


# Array2 start
count = self.writeVint(0)
for i in range(value):
    self.writeVint(0)
    self.writeVint(0)
    self.writeVint(0)
    self.writeVint(0)

    self.writeScID(0, 0) # Unknown ScID

    count1 = self.writeVint(0)
    for i in range(count1):
      self.writeVint(0)
      self.writeVint(0)

      self.writeScID(0, 0) # Unknown ScID

      self.writeVint(0)

    count2 = self.writeVint(0)
    for i in range(count2):
      self.writeVint(0)
      self.writeVint(0)

      self.writeScID(0, 0)  # Unknown ScID

      self.writeVint(0)

    whatthehellisthat = 6
    if whatthehellisthat == 6:
      self.wrieVint(0)
      self.wrieVint(0)
# Array 2 end


# Array3 start
count = self.writeVint(0)
for i in range(count):
  self.writeVint(0)
  self.writeVint(0)
  self.writeVint(0)
# Array 3 end

# unknown start
boolean = False
if boolean == True:
  self.writeBoolean(True)
  count = self.writeVint(0)
  for i in range(count):
    self.writeVint(0)
    self.writeVint(0)
    self.writeVint(0)
    self.writeVint(0)

    self.writeScID(0, 0) # Unknown ScID

    count1 = self.writeVint(0)
    for i in range(count1):
      self.writeVint(0)
      self.writeVint(0)

      self.writeScID(0, 0) # Unknown ScID

      self.writeVint(0)

    count2 = self.writeVint(0)
    for i in range(count2):
      self.writeVint(0)
      self.writeVint(0)

      self.writeScID(0, 0)  # Unknown ScID

      self.writeVint(0)

    whatthehellisthat = 6
    if whatthehellisthat == 6:
      self.wrieVint(0)
      self.wrieVint(0)
else:
  self.writeBoolean(False)
# unknown end

self.writeScId(28, 0) # i think the 28 is that ??? but im not sure

bool = self.writeBoolean(False)
if bool == True:
  self.writeInt(0)

  count1 = self.writeVint(0)
  for i in range(count):
    self.writeInt(0) # HighID
    self.writeInt(1) # LowID

  count2 = self.writeVint(0)
  for i in range(count):
    self.writeInt(0)  # HighID
    self.writeInt(1)  # LowID

  self.writeInt(0)
  self.writeInt(0)
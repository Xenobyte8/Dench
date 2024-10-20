import random
import uuid
from fileAdapter import addMission, changeMissionStatus, changeGangsterStatus, getMission, getGangster, GangsterCharachteristic
import asyncio
from aiogram.types import CallbackQuery, ContentType, Message
from dbadapter import addGangster, addPlayer


class Player:
   def __init__(self, tgId):
      self.id=uuid.uuid4()
      self.tgId=tgId
      self.money=1000
      try:
         if (addPlayer(self.id, self.tgId, self.money)):
            pass
         else:
            raise ValueError('telegram_id is already registered')
      except ValueError as exp:
         print(exp)

class Gangster:
   def __init__(self, owner, new=True):
        self.id=uuid.uuid4()
        self.owner=owner
        self.name = random.choice(['Иван','Олег','Петр','Бонифаций','Денис','брат Нигерус','Хосе','Уриэль','Джо','Сергей'])
        self.athletics=random.choice([4,4,6,6,8])
        self.charisma=random.choice([4,4,6,6,8])
        self.shooting=random.choice([4,4,6,6,8])
        self.stealth=random.choice([4,4,6,6,8])
        self.intelligence=random.choice([4,4,6,6,8])
        self.state='AVAILABLE' # Доступны вариант AVAILABE, MISSION, UNAVAILABLE, DEAD
        self.mission=0 
        if new: addGangster(self.id, self.owner, self.name, self.athletics, self.charisma, self.shooting, self.stealth, self.intelligence, self.state, self.mission)
        

   def __str__(self):
      return self.name
    
      

   def getDescription(self):
      result="Имя: "+ self.name+", Атлетика: "+ self.athletics+ ", Харизма: " + self.shooting + ", Стелс: "+self.stealth+", Смекалка: " + self.intelligence
      return result


class Mission:
   def __init__(self, name, description, price, reward, tryDifficulty, tryCharacteristic, time):
      self.id=uuid.uuid4()
      self.name=name
      self.description=description
      self.price=price
      self.reward=reward
      self.tryDifficulty=tryDifficulty
      self.tryCharacteristic=tryCharacteristic
      self.status = 'FREE' # могут быть FREE, ACTIVE, FINISHED
      self.owner=0
      self.time=time
      #addMission(self.id, self.name, self.description, self.price, self.reward, self.tryAmount, self.tryCharacteristic, self.status, self.owner, self.time)
   


def checkMissionSuccess(missionId, gangstersId:'list' ):
   resultGangsters=0
   mission=getMission(missionId)
   gangsters=[]
   for i in gangstersId:
      i=getGangster(i)

   for ster in gangsters:
      tryGangster=random.randint(0, GangsterCharachteristic(ster['id'], mission['tryCharacteristic']))
      resultGangsters+=tryGangster
   if resultGangsters <  int(mission['tryDifficulty']): return False
   else: return True

async def playMission(missionId, gangsters:'list', message:Message, owner=0):
   changeMissionStatus(missionId, 'ACTIVE', owner)
   for i in gangsters:
      changeGangsterStatus(gangsterId = i, missionId = missionId, state='MISSION')
   await asyncio.sleep(10)
   print(missionId)
   print(gangsters)
   print(owner)
   result = checkMissionSuccess(missionId, gangsters)
   if result==False: changeMissionStatus(missionId, 'FREE', owner)
   await message.answer(str(result))
   
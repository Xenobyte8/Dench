import csv

def addPlayer(id, tgId, money):
    file = open('./files/players.csv', 'a+', newline ='')
    with file:
        writer = csv.writer(file)
        writer.writerow([id,tgId,money])
    file.close()


def addGangster(id,owner,name,athletics,charisma,shooting,stealth,intelligence,state,mission):
    file = open('./files/gangsters.csv', 'a+', newline ='')
    with file:
        writer = csv.writer(file)
        writer.writerow([id,owner,name,athletics,charisma,shooting,stealth,intelligence,state,mission])
    file.close()

def addMission(id,name,description,price,reward,tryDifficulty,tryCharechteristic,status,owner,time):
    file = open('./files/missions.csv', 'a+', newline ='')
    with file:
        writer = csv.writer(file)
        writer.writerow([id,name,description,price,reward,tryDifficulty,tryCharechteristic,status,owner,time])
    file.close()

def getPlayer(id):
    result=False
    file = open('./files/players.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]==str(id): result={'id': row[0], 'tgId': row[1], 'money': row[2]}
    file.close()
    return result


def getPlayerByTg(id):
    result=False
    file = open('./files/players.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[1]==str(id): result={'id': row[0], 'tgId': row[1], 'money': row[2]}
    file.close()
    return result

def getGangster(id):
    result=False
    file = open('./files/gangsters.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]==str(id): result={'id': row[0], 'owner': row[1], 'name': row[2], 'athletics': row[3], 'charisma': row[4],'shooting': row[5], 'stealth':row[6],'intelligence':row[7]}
    file.close()
    return result

def getMission(id):
    result=False
    file = open('./files/missions.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]==str(id): result={'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'reward': row[4],'tryDifficulty': row[5], 'tryCharechteristic':row[6],'status':row[7], 'owner':row[8], 'time':row[9]}
    file.close()
    return result


def getAvailableMissions():
    result=[]
    file = open('./files/missions.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[7]=='FREE': result.append({'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'reward': row[4],'tryDifficulty': row[5], 'tryCharechteristic':row[6],'status':row[7], 'owner':row[8], 'time':row[9]})
    file.close()
    return result

def changePlayerMoney(id, amount):
    result=False
    file = open('./files/players.csv', newline ='')
    with file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    file.close()
    for row in rows:
        if row[0]==str(id): 
            row[2]=str(amount)
            result=True
    with open('./files/players.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    file.close
    return result

def GangsterCharachteristic(id, charac: 'str'=['athletics', 'charisma', 'shooting', 'stealth', 'intelligence']):
    gangster=getGangster(id)
    if charac=='athletics': return gangster['athletics']
    if charac=='charisma': return gangster['charisma']
    if charac=='shooting': return gangster['shooting']
    if charac=='stealth': return gangster['stealth']
    if charac=='intelligence': return gangster['intelligence']


def getGangstersByOwner(owner):
    result=[]
    file = open('./files/gangsters.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[1]==str(owner):
                result.append({'id': row[0], 'owner': row[1], 'name': row[2], 'athletics': row[3], 'charisma': row[4],'shooting': row[5], 'stealth':row[6],'intelligence':row[7]})
    file.close()
    return result

def changeMissionStatus(id, state: 'str'=['FREE', 'ACTIVE', 'FIFNISHED'], owner=False):
    result=False
    file = open('./files/missions.csv', newline ='')
    with file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    file.close()
    for row in rows:
        if row[0]==str(id):
            print (row[0])
            print(str(id)) 
            row[7]=str(state)
            if owner: row[8]=str(owner) 
            result=True

    with open('./files/missions.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    file.close
    return result


def getAllMissions():
    result=[]
    file = open('./files/missions.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]!='id': result.append({'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'reward': row[4],'tryAmount': row[5], 'tryCharechteristicstealth':row[6],'status':row[7], 'owner':row[8], 'time':row[9]})
    file.close()
    return result


def changeGangsterStatus(gangsterId, state: 'str'=['AVAILABE', 'MISSION', 'UNAVAILABLE', 'DEAD']):
    result=False
    file = open('./files/gangsters.csv', newline ='')
    with file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    file.close()
    for row in rows:
        if row[0]==str(gangsterId):
            row[8]=str(state)
            result=True

    with open('./files/gangsters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    file.close
    return result
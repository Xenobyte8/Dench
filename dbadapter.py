import sqlite3
import uuid

def addPlayer(id, telegram_id, player_money):
    result = False
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data/database.db') as connection:
        cursor = connection.cursor()
        try:
        # Начинаем транзакцию автоматически
            with connection:
                # Выполняем операции
                cursor.execute(
                    f'''
                    INSERT INTO players (id, telegram_id, player_money) VALUES ('{id}', '{telegram_id}', '{player_money}')
                    '''
                    )
            result = True
        except Exception as e:
        # Ошибки будут приводить к автоматическому откату транзакции
            print(e)
            pass
    return result


def addGangster(id,owner,name,athletics,charisma,shooting,stealth,intelligence,state,mission):
    result = False
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data/database.db') as connection:
        cursor = connection.cursor()
        try:
        # Начинаем транзакцию автоматически
            with connection:
                # Выполняем операции
                cursor.execute(f'''INSERT INTO gangsters (id,owner,name,athletics,charisma,shooting,stealth,intelligence,state,mission)
                                    VALUES ('{id}','{owner}','{name}','{athletics}','{charisma}','{shooting}','{stealth}','{intelligence}','{state}','{mission}')'''
                                    )
            result = True
        except Exception as e:
        # Ошибки будут приводить к автоматическому откату транзакции
            print(e)
            pass
    return result

def addMission(id,name,description,price,reward,tryDifficulty,tryCharacteristic,status,owner,time):
    file = open('./files/missions.csv', 'a+', newline ='')
    with file:
        writer = csv.writer(file)
        writer.writerow([id,name,description,price,reward,tryDifficulty,tryCharacteristic,status,owner,time])
    file.close()

def addHeadquaters(planet, owner):
    result = False
    id = uuid.uuid4()
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data/database.db') as connection:
        cursor = connection.cursor()
        try:
        # Начинаем транзакцию автоматически
            with connection:
                # Выполняем операции
                cursor.execute(
                    f'''
                    INSERT INTO headquarters (id, planet, owner) VALUES ('{id}', '{planet}', '{owner}')
                    '''
                    )
            result = True
        except:
        # Ошибки будут приводить к автоматическому откату транзакции
            pass
    return result

'''
def getPlayer(id):
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data/database.db') as connection:
        cursor = connection.cursor()
        try:
        # Начинаем транзакцию автоматически
            with connection:
                # Выполняем операции
                cursor.execute(
                    f"SELECT * FROM players where telegram_id = '{id}'"
                )
                player_id = cursor.fetchone()
            result = gangsters_as_dicts
        except:
        # Ошибки будут приводить к автоматическому откату транзакции
            print('smth went wrong, transaction aborted')
    return result
    '''


def getPlayerByTg(telegram_id):
    result=False
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data/database.db') as connection:
        cursor = connection.cursor()
        try:
        # Начинаем транзакцию автоматически
            with connection:
                # Выполняем операции
                cursor.execute(
                    f"SELECT id FROM players where telegram_id = '{telegram_id}'"
                )
                player_id = cursor.fetchone()
            result = player_id[0]
        except:
        # Ошибки будут приводить к автоматическому откату транзакции
            print('smth went wrong, transaction aborted')
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
            if row[0]==str(id): result={'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'reward': row[4],'tryDifficulty': row[5], 'tryCharacteristic':row[6],'status':row[7], 'owner':row[8], 'time':row[9]}
    file.close()
    return result


def getAvailableMissions():
    result=[]
    file = open('./files/missions.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[7]=='FREE': result.append({'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'reward': row[4],'tryDifficulty': row[5], 'tryCharacteristic':row[6],'status':row[7], 'owner':row[8], 'time':row[9]})
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
    result = []
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data/database.db') as connection:
        cursor = connection.cursor()
        try:
        # Начинаем транзакцию автоматически
            with connection:
                # Выполняем операции
                cursor.execute(
                    f"SELECT * FROM gangsters where owner = '{owner}'"
                )
                gangsters_as_tuples = cursor.fetchall()
                # Преобразуем результаты в список словарей
                gangsters_as_dicts = []
                for i in gangsters_as_tuples:
                    gangster_dict = {
                    'id': i[0],
                    'owner': i[1],
                    'name' : i[2],
                    'athletics' : i[3],
                    'charisma' : i[4],
                    'shooting' : i[5],
                    'stealth' : i[6],
                    'intelligence' : i[7],
                    'state' : i[8],
                    'mission' : i[9],
                    }
                    gangsters_as_dicts.append(gangster_dict)
            result = gangsters_as_dicts
        except:
        # Ошибки будут приводить к автоматическому откату транзакции
            print('smth went wrong, transaction aborted')
    return result


def changeMissionStatus(id, state: 'str'=['FREE', 'ACTIVE', 'FINISHED'], owner=False):
    result=False
    # Устанавливаем соединение с базой данных
    with sqlite3.connect('data/database.db') as connection:
        cursor = connection.cursor()
        try:
        # Начинаем транзакцию автоматически
            with connection:
                # Выполняем операции
                cursor.execute(f'''UPDATE TABLE missions
                                    set status = '{state}',
                                        owner = '{owner}'
                                    where id = '{id}'    
                               '''
                                    )
            result = True
        except Exception as e:
        # Ошибки будут приводить к автоматическому откату транзакции
            print(e)
            pass
    return result


def getAllMissions():
    result=[]
    file = open('./files/missions.csv', newline ='')
    with file:
        reader = csv.reader(file)
        for row in reader:
            if row[0]!='id': result.append({'id': row[0], 'name': row[1], 'description': row[2], 'price': row[3], 'reward': row[4],'tryAmount': row[5], 'tryCharacteristicstealth':row[6],'status':row[7], 'owner':row[8], 'time':row[9]})
    file.close()
    return result


def changeGangsterStatus(gangsterId, missionId, state: 'str'=['AVAILABE', 'MISSION', 'UNAVAILABLE', 'DEAD']):
    result=False
    file = open('./files/gangsters.csv', newline ='')
    with file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    file.close()
    for row in rows:
        if row[0]==str(gangsterId):
            row[8]=str(state)
            row[9] = str(missionId)
            result=True

    with open('./files/gangsters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    file.close
    return result



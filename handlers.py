from aiogram_dialog import Dialog, Window, setup_dialogs, DialogManager
import asyncio
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram import flags
from aiogram.fsm.context import FSMContext
import config
from game import Gangster, Player
from fileAdapter import getAvailableMissions
from states import GetMission
from dbadapter import getGangstersByOwner, getPlayerByTg

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    try:
        Player(str(msg.from_user.id))
        await msg.answer("Привет! Давай играть!)")
    except:
        await msg.answer("Кажется, ты уже у нас зарегистрирован.")

@router.message(Command("getMe"))
async def get_player_by_telegram_id(msg: Message):
    player=getPlayerByTg(msg.from_user.id)
    await msg.answer(str("Твой player_id: " + str(player)))

@router.message(Command("newBro"))
async def CreateGangster(msg: Message):
    player=getPlayerByTg(msg.from_user.id)
    bro=Gangster(str(player))
    await msg.answer(str("Вот твой новый боец "+ str(bro)))

@router.message(Command("getBros"))
async def GetGangsters(msg: Message):
    player=getPlayerByTg(msg.from_user.id)
    gangsters=getGangstersByOwner(str(player))
    for i in gangsters:
        await msg.answer(str(i))

@router.message(Command("getFreeMissions"))
async def GetFreeMissions(msg: Message):
    missions=getAvailableMissions()
    for i in missions:
        await msg.answer(str(i))


@router.message(Command("getMission"))
async def test(msg: Message, dialog_manager: DialogManager):
    player=getPlayerByTg(msg.from_user.id)
    await dialog_manager.start(GetMission.chooseMission, data={'playerId':str(player['id']), 'message':msg})
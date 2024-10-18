from aiogram.fsm.state import StatesGroup, State

class GetMission(StatesGroup):
    chooseMission = State()
    chooseGangsters = State()
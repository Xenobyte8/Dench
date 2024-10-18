import operator
import asyncio
from typing import Any
from aiogram.types import CallbackQuery, ContentType, Message
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import Checkbox, Button, Row, Cancel, Start, Column
from states import GetMission
from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog.widgets.kbd import Back, Next, Row, SwitchTo, Select, Multiselect
from aiogram_dialog.widgets.input import MessageInput
import fileAdapter
from game import playMission


async def getMissions( **kwargs
):
    missions=fileAdapter.getAvailableMissions()
    fruits=[]
    for i in missions:
        fruits.append((i['name'],i['id'] ))
    return {
        "fruits": fruits,
        "count": len(fruits),
    }



async def getGangsters( **kwargs):
    player= kwargs['dialog_manager'].start_data['playerId']
    gangsters=fileAdapter.getGangstersByOwner(player)
    result=[]
    for i in gangsters:
        result.append((i['name'],i['id'] ))
    return {
        "fruits": result,
    }


async def startMission(callback: CallbackQuery, button: Button, manager: DialogManager,):
    print(manager)
    widget = manager.dialog().find('gangstersWidget')
    gangsters=widget.get_checked(manager)
    asyncio.create_task(playMission(manager.dialog_data['Mission'], gangsters,  manager.start_data['playerId']))
    await manager.done()

async def selectMission(callback: CallbackQuery, widget: Any,manager: DialogManager, item_id: str):
    manager.dialog_data['Mission']=item_id
    await manager.next()
    

getMissionDialog = Dialog(
     Window(
        Const("Выбери миссию"),
        Column(
                Select(
                    Format("{item[0]} ({pos}/{data[count]})"),  # E.g `✓ Apple (1/4)`
                    id="s_fruits",
                    item_id_getter=operator.itemgetter(1),
                    # each item is a tuple with id on a first position
                    items="fruits",
                    on_click=selectMission),
        ),
        state=GetMission.chooseMission,
        getter=getMissions,
    ),
    Window( 
        Const("Выбери пацанов, с которыми пойдешь, а потом нажми Go!"),
        Column(
            Multiselect(
                Format("+ {item[0]}"),
                Format("{item[0]}"),
                id="gangstersWidget",
                item_id_getter=operator.itemgetter(1),
                # each item is a tuple with id on a first position
                items="fruits",
                )
            ),
        Column(
            Button(
            Const("Go"),
            id="go",  # id is used to detect which button is clicked
            on_click=startMission)
        ),

        state=GetMission.chooseGangsters,
        getter=getGangsters,)
)
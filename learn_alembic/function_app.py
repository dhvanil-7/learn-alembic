import azure.functions as func
from alembic.config import Config
from alembic import command
import logging


app = func.FunctionApp()


@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def run_db_migrations(myTimer: func.TimerRequest) -> None:
    
    config=Config("./alembic.ini")
    command.upgrade(config, "head")

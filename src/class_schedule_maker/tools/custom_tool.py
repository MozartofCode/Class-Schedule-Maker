from typing import Type
from crewai_tools import BaseTool
import pandas as pd
from pydantic import BaseModel, Field

# Custom tool to get the already existing (planned) calendar of a user for a semester

class CalendarInput(BaseModel):
    """Input schema for Calendar."""
    argument: str = Field(..., description="Description of the argument.")

class ProcessCalendar(BaseTool):
    name: str = "Process Calendar"
    description: str = (
        "This tool processes the calendar to return the empty and non-empty slots of a user for that planned semester."
    )
    args_schema: Type[BaseModel] = CalendarInput

    def _run(self, argument: str) -> str:
        # Load the calendar
        return
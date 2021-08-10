from pydantic import BaseModel
from typing import Optional, List, Union
from pathlib import Path
from pandas import DataFrame

class CreateHod(BaseModel):
    name: str
    email: str
    phone_num: int
    user_name: str
    department: str

class ShowHods(CreateHod):
    class Config():
        orm_mode = True

class DeleteHod(BaseModel):
    name: str
    department: str

class AddDepartment(BaseModel):
    Department: str
    Alias: str

class AddCourse(BaseModel):
    course_name: str
    course_alias: str
    duration: int
    department: str

class DeleteDepartment(BaseModel):
    department: str

class DeleteCourse(BaseModel):
    course_name: str

class AdminPass(BaseModel):
    username: str = 'admin'
    current_pass: str
    new_pass: str

class Admin(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    admin: Optional[str] = None


class AddTeacher(BaseModel):
    name: str
    department: str
    email: str
    phone_number: Optional[int]

class ShowTeacher(AddTeacher):
    class Config():
        orm_mode = True

class DeleteTeacher(BaseModel):
    name: str
    user_name: str

class TimeTable(BaseModel):
    department: str
    course: str
    days: List[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    year: int
    day_1: List[str]
    day_2: List[str]
    day_3: List[str]
    day_4: List[str]
    day_5: List[str]

class TimeTableChecker(BaseModel):
    day: str 
    name: str
    hour: str

class TimeTableEdit(BaseModel):
    course: str
    year: int
    department: str

class CurrentHour(BaseModel):
    name: str
    course: str
    year: str
    hour: str


class Files(BaseModel):
    daily: Union[Path, DataFrame]
    monthly: Union[Path, DataFrame]
    daily_path: Path
    monthly_path: Path
    
    class Config:
        arbitrary_types_allowed = True

class AddStudent(BaseModel):
    course: str
    year: int
    name: str
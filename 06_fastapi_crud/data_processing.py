from constants import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field

def read_json(filename):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
    return data

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(gt=0, lt=2026, description="Year of when the book was published")


class Library(BaseModel):
    name: str
    books: list[Book]

def libary_data(filename):
    json_data = read_json(filename)
    return Library(**json_data)



if __name__ == "__main__":
    #pprint(read_json("library.json"))
    print(repr(libary_data("library.json")))
from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str = Field(description="Title of the movie.")
    year: int = Field(gt=1980, lt=2025, description="Release year of the movie, must be between 1980 and 2025.")
    genre: str = Field(description="Genre of the movie, if there are multiple genres pick the primary one.")
    rating: float = Field(gt=0, lt=10, description="Rating must be between 0 and 10, higher is better, keep it realistic.")



class Prompt(BaseModel):
    prompt: str = Field(description="Prompt to user to find a movie, try to find clossest movie even if the user prompt someting else.")
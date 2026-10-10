from pydantic import BaseModel


class FileCreate(BaseModel):
    file_name: str
    content: str


class FileResponse(BaseModel):
    id: int
    file_name: str
    content: str

    class Config:
        from_attributes = True
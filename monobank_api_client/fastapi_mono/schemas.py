from pydantic import BaseModel, Field


class MonoSchema(BaseModel):
    mono_token: str = Field(..., max_length=44)
    user_id: str

    class Config:
        from_attributes = True


class MonoSchemaUpdate(BaseModel):
    mono_token: str = Field(..., max_length=44)

    class Config:
        from_attributes = True

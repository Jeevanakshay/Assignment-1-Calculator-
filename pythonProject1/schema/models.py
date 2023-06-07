from pydantic import BaseModel


class Snacks(BaseModel):
    """"Class is created"""
    name: str
    quantity: int
    price: int
    tax_price: float


class Email(BaseModel):
    """
    Email class is created
    """
    rec_email: str
    subject: str
    body: str

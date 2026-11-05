from pydantic import BaseModel,Field, ValidationError
class Product(BaseModel):
    name: str = Field(...,min_length=1, max_length=50)
    price: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)
    tags: list[str] = Field(default_factory=list)

try:
    pr1 = Product(name='', price=10000)
except ValidationError as e1:
    print('T1:',e1)

try:
    pr1 = Product(name="Bút", price=0)
except ValidationError as e2:
    print('T2:', e2)

p1 = Product(name="Apple", price=5000000)
p2 = Product(name="Android", price=10000)

p1.tags.append("sale")

print("p1.tags:", p1.tags)  
print("p2.tags:", p2.tags)
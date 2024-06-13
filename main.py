from fastapi import Depends, FastAPI
from requests import Session
from db import Base, engine, SessionLocal, Product
from schemas.user import ProductCreate, ProductGet

app = FastAPI(title="FastAPI Ales")

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products", response_model=list[ProductGet])
def getProducts(db: Session = Depends(get_db)):
    return db.query(Product).all()


@app.get("/products/{id}", response_model=ProductGet)
def getProduct(id: int, db: Session = Depends(get_db)):
    return db.get(Product, id)


@app.post("/products", response_model=ProductGet)
def createProduct(product: ProductCreate, db: Session = Depends(get_db)):
    dbProduct = Product(**product.model_dump())
    db.add(dbProduct)
    db.commit()
    db.refresh(dbProduct)
    return dbProduct


# code for parse data from other api

# def get_data_from_api(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         # listOfProducts = []
#         for item in data:

#             product = Product(
#                 name=item.get("name"),
#                 slug=item.get("slug"),
#                 description=item.get("description"),
#                 price=item.get("price"),
#                 images=item.get("images"),
#                 quantity=item.get("quantity"),
#                 typeId=item.get("typeId"),
#                 categoryIds=item.get("categoryIds"),
#                 socialLinks=item.get("socialLinks"),
#             )
#             db.add(product)
#             db.commit()


# get_data_from_api("https://api.krylshop.ru/api/products")

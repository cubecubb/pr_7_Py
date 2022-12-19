from typing import List
import uuid
from fastapi import APIRouter, Depends
from utils.dependencies import get_product_repo
from utils.models.product import ProductIn, ProductOut
from utils.repositories.product import BaseProductRepository

router = APIRouter()

@router.get("/products", response_model=List[ProductOut])
async def get_products(
    product_repo : BaseProductRepository = Depends(get_product_repo),
    limit : int = 100,
    skip : int = 0
    ):
    return product_repo.get_all(limit=limit, skip=skip)

@router.get("/product", response_model=ProductOut)
async def get_product(
    uuid : uuid.UUID,
    product_repo : BaseProductRepository = Depends(get_product_repo),
    ):
    return product_repo.get_by_id(uuid)

@router.post("/product", response_model=ProductOut)
async def create_product(
    product_in : ProductIn,
    product_repo : BaseProductRepository = Depends(get_product_repo)
    ):
    return product_repo.create(product_in)

@router.put("/product", response_model=ProductOut)
async def put_product(
    uuid : uuid.UUID,
    product_in : ProductIn,
    product_repo : BaseProductRepository = Depends(get_product_repo)
    ):
    return product_repo.put(uuid, product_in)

@router.delete("/product", response_model=str)
async def delete_product(
    uuid : uuid.UUID,
    product_repo : BaseProductRepository = Depends(get_product_repo)
    ):
    return product_repo.delete(uuid)
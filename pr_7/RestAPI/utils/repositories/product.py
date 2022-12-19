import uuid
from typing import List, Dict, Optional
from utils.models.product import ProductIn, ProductOut, ProductStorage
from utils.converter import convert_product_in_to_storage, convert_product_storage_to_out

class BaseProductRepository:
    """ Базовый класс для реализации функционала работы с продуктами """

    def get_by_id(self, id : uuid.UUID) -> ProductOut:
        raise NotImplementedError

    def get_all(self, limit : int, skip : int) -> List[ProductOut]:
        raise NotImplementedError

    def create(self, product : ProductIn) -> ProductOut:
        raise NotImplementedError

    def put(self, id : uuid.UUID, product : ProductIn) -> ProductOut:
        raise NotImplementedError

    def delete(self, id : uuid.UUID) -> str:
        raise NotImplementedError

class ProductTmpRepository(BaseProductRepository):
    """ Реализация продукта с временным хранилищем в объекте Dict """

    def __init__(self) -> None:
        self._dict_products : Dict[uuid.UUID, ProductStorage] = {}

    def get_by_id(self, uuid: uuid.UUID) -> ProductOut:
        """ Получение продукта по ID """

        product : ProductStorage = self._dict_products.get(uuid)
        if product is None:
            return None
        product_out : ProductOut = convert_product_storage_to_out(product)
        return product_out

    def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        """ Получение всех продуктов """

        product_out_list : List[ProductOut] = []
        for _, product in self._dict_products.items():
            product_out_list.append(convert_product_storage_to_out(product))
        return product_out_list[skip:skip+limit]

    def create(self, product : ProductIn) -> ProductOut:
        """ Создание продукта """
        
        product_storage : ProductStorage = convert_product_in_to_storage(product)
        self._dict_products.update({product_storage.id : product_storage})
        product_out : ProductOut = convert_product_storage_to_out(product_storage)
        return product_out

    def put(self, uuid : uuid.UUID, product : ProductIn) -> ProductOut:
        """ Изменение параметров продукта """
        
        old_product : ProductStorage = self._dict_products.get(uuid)
        if old_product is None:
            return None
        new_product : ProductStorage = convert_product_in_to_storage(product)
        self._dict_products.update({uuid : new_product})
        product_out : ProductOut = convert_product_storage_to_out(new_product)
        return product_out
    
    def delete(self, uuid : uuid.UUID) -> str:
        """ Удаление продукта """

        product : ProductStorage = self._dict_products.get(uuid)
        if product is None:
            return None
        self._dict_products.pop(uuid, None)
        return "The product has been successfully removed!"


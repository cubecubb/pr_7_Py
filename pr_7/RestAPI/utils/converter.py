import datetime
import uuid
from utils.models.product import ProductStorage, ProductOut, ProductIn

def convert_product_storage_to_out(product : ProductStorage) -> ProductOut:
    """ Производит конвертацию ProductStorage --> ProductOut """

    tmp_dict : dict = product.dict()
    tmp_dict.pop("secret_token", None)
    return ProductOut(**tmp_dict)

def convert_product_in_to_storage(product : ProductIn) -> ProductStorage:
    """ Производит конвертацию ProductIn --> ProductStorage """

    tmp_dict : dict = product.dict()
    product_storage = ProductStorage(id=uuid.uuid4(),
                                     created_at=datetime.datetime.now(),
                                     **tmp_dict)
    return product_storage
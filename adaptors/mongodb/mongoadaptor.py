"""mongodbadopter is use for save data"""
import asyncio
import json
from typing import List
from common_utilities.file_handler import FileUpload
from bson.objectid import ObjectId


class DataBaseManager:
    """_summary_"""

    def __init__(
        self, client: object, engine: object, config: object, validator: object
    ) -> None:
        self.client = client(config.get_uri())
        self.client.get_io_loop = asyncio.get_running_loop
        self.engine = engine(motor_client=self.client, database="test")
        self.validator = validator

    async def bulk_save(self, instance: List[object]):
        """_summary_

        Args:
            instance (List[object]): _description_

        Returns:
            _type_: _description_
        """
        data = await self.engine.save_all(instance)
        return data

    async def save(self, instance: object):
        """_summary_

        Args:
            instance (object): _description_

        Returns:
            _type_: _description_
        """
        data = await self.engine.save(instance)

        return data

    async def update_one(self, instance: object, value: dict, update: dict):
        """_summary_

        Args:
            instance (object): _description_
            value (dict): _description_
            update (dict): _description_

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        data = object
        if len(value.keys()) <= 1:
            data = await self.get_one(
                instance, {list(value.keys())[0]: list(value.values())[0]}
            )
            if data:
                for key, val in update.items():
                    print(data,"hjjyujy")
                    setattr(data, key, val)
                    print("gtgtgtrtrt","hjjyujy")
                    await self.save(data)
            else:
                raise Exception("object not found")
        else:
            data = await self.get_one(instance, value)
            if data:
                for k, vals in update.items():
                    if hasattr(data,k):
                        setattr(data,k,vals)
                    else:
                        print(f"attribute not found {k}")
                    await self.save(data)
        return data

    async def update_bulk(
        self, instance: object, value: List[dict], update: List[dict]
    ):
        """_summary_

        Args:
            instance (object): _description_
            value (List[dict]): _description_
            update (List[dict]): _description_

        Returns:
            _type_: _description_
        """
        for i in value:
            for j in update:
                await self.update_one(instance, i, j)
        return dict(status=update)

    async def delete_one(self, instance: object, value: dict):
        """_summary_

        Args:
            instance (object): _description_
            value (List[dict]): _description_

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        data = object
        if len(value.keys()) <= 1:
            data = await self.get_one(
                instance, {list(value.keys())[0]: list(value.values())[0]}
            )
            if data:
                data = await self.engine.delete(data)
            else:
                raise Exception("object not found")
        else:
            data = await self.get_one(instance, value)
            if data:
                data = await self.engine.delete(data)
        return data

    async def delete_bulk(self, instance: object, value: List[dict]):
        """_summary_

        Args:
            instance (object): _description_
            value (List[dict]): _description_

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        res = []
        for i in value:

            data = await self.get_one(instance, i)
            if data:
                res.append(data)
                data = await self.engine.delete(data)
            else:
                raise Exception("object not found")
        return res

    async def get_one(self, instance: object, value: dict):
        """_summary_

        Args:
            instance (object): _description_
            value (dict): _description_

        Returns:
            _type_: _description_
        """
        data = object
        if len(value.keys()) <= 1:
            data = await self.engine.find_one(
                instance,
                getattr(instance, list(value.keys())[0])
                == ObjectId(list(value.values())[0]),
            )
        else:
            data = await self.engine.find_one(
                instance, *[getattr(instance, x) == y for x, y in value.items()]
            )
        return data

    async def get_one_email(self, instance: object, value: dict):
        """_summary_

        Args:
            instance (object): _description_
            value (dict): _description_

        Returns:
            _type_: _description_
        """
        data = object
        if len(value.keys()) <= 1:
            data = await self.engine.find_one(
                instance,
                getattr(instance, list(value.keys())[0]) == list(value.values())[0],
            )
        else:
            data = await self.engine.find_one(
                instance, *[getattr(instance, x) == y for x, y in value.items()]
            )
        return data

    async def get_all(self, instance, value=None):
        """_summary_

        Args:
            instance (_type_): _description_

        Returns:
            _type_: _description_
        """
        if value is None:
            data = await self.engine.find(instance, {})
        else:
            if "page" and "size" in value.keys():
                d = value["page"]
                e = value["size"]
                del value["page"]
                del value["size"]
                sw = 0
                if int(d) > 1:
                    sw = int(e) * int(d)
                print(value)
                data = await self.engine.find(instance, value).skip(sw).limit(int(e))
            else:
                data = await self.engine.find(instance, value)
        return data

    async def save_file(self, data: bytes, name: str):
        file_id = await self.fileupload.upload_from_stream(name, data)
        return file_id

    async def get_file(self, id):
        file = await self.fileupload.open_download_stream(ObjectId(id))
        return file

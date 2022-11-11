"""role model"""
from typing import List

from odmantic import Model


class Role(Model):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    rolename: str
    permissions: List[str]

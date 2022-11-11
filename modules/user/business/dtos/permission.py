"""primission model"""
from odmantic import Model


class Permission(Model):
    """_summary_

    Args:
        Model (_type_): _description_
    """

    permissionname: str
    permissionview: str

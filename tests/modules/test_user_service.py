from modules.user.enterprise.services.user import *
from modules.user.business.dtos.user import User
from infrastructure.shared_di.di import obj_graph


async def test_user_service():
    res = []
    db = obj_graph.provide(UserServices)
    dto = User(
        firstname="rajat", lastname="mishra", email="r@r.com", password="ajat322"
    )
    data = await db.create(dto)
    res.append(data)
    assert data == dto

    data = await db.get(User, dict(id=dto.id))
    res.append(data)
    assert data == dto

    data = await db.get_all(User)
    res.append(data)
    assert type(data) == list

    data = await db.update(User, dict(id=dto.id), dict(firstname="man"))
    res.append(data)
    assert data != dto

    data = await db.delete(User, dict(id=dto.id))
    res.append(data)
    assert data != dto

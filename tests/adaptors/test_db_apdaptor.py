import pytest
from adaptors.mongodb.mongoadaptor import DataBaseManager
from infrastructure.shared_di.di import obj_graph
from modules.candidate.business.dtos.candidate import Candidate


async def test_db_adaptor():
    db = obj_graph.provide(DataBaseManager)
    dto = Candidate(firstname="rajat", lastname="mishra", email="r@r.com")
    data = await db.save(dto)
    assert data == dto

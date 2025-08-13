import pytest

from tests.test_main import db_con


@pytest.mark.asyncio
async def pytest_sessionfinish(session):
    if db_con is not None:
        await db_con.close()

from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi import HTTPException

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from .models import operation
from .schemas import OperationCreate
from .tasks import post_operation

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("")
async def get_specific_operations(operation_type: str,
                                  session: AsyncSession =
                                  Depends(get_async_session)):
    try:
        query = select(
            operation.c.type,
            operation.c.quantity,
            operation.c.date).where(
                operation.c.type == operation_type)
        result = await session.execute(query.limit(50))
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("")
async def add_specific_operations(background_tasks: BackgroundTasks,
                                  new_operation: OperationCreate,
                                  session: AsyncSession =
                                  Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.model_dump())
    background_tasks.add_task(post_operation)
    post_operation.delay()

    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

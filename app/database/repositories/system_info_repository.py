from sqlalchemy import select

from app.database.models import SystemInfo
from app.database.session import get_session


class SystemInfoRepository:
    """Repositório para informações do sistema."""

    def get(self, key: str):
        with get_session() as session:
            stmt = select(SystemInfo).where(SystemInfo.key == key)
            return session.scalar(stmt)

    def set(self, key: str, value: str):
        with get_session() as session:

            info = session.scalar(
                select(SystemInfo).where(SystemInfo.key == key)
            )

            if info is None:
                info = SystemInfo(
                    key=key,
                    value=value,
                )
                session.add(info)
            else:
                info.value = value

            session.commit()
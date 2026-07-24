from app.database.database import initialize_database
from app.database.repositories.system_info_repository import (
    SystemInfoRepository,
)

initialize_database()

repo = SystemInfoRepository()

repo.set("version", "0.1.0")

info = repo.get("version")

print(info.key)
print(info.value)
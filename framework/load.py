from git import Repo
import os


class LoadComponents:
    FRAMEWORK_REGISTRY = ""

    async def load(self, **kwargs):
        if (
            "type" in list(kwargs.keys())
            and kwargs["type"] == "modules"
            or kwargs["type"] == "adaptors"
        ):
            await self.modules(kwargs)
        return dict(error="type and from kwargs are required")

    async def modules(self, **kwargs):
        if "type" in list(kwargs.keys()) and kwargs["type"] == "modules":
            if "path" not in list(kwargs.keys()):
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                    }
            else:
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                    "path":kwargs.get("type"),
                    }

            resp = await self.from_(**data)
            return resp
        elif "type" in list(kwargs.keys()) and kwargs["type"] == "adaptors":
            if "path" not in list(kwargs.keys()):
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                    }
            else:
                data = {
                    "from": kwargs.get("from"),
                    "name": kwargs.get("name"),
                    "type": kwargs.get("type"),
                    "path":kwargs.get("type"),
                    }
            resp = await self.from_(**data)
            return resp

    async def from_(self, **kwargs):
        type = kwargs.get("type")
        if "from" in list(kwargs.keys()) and kwargs["from"] == "FRAMEWORK_REGISTRY":
            if "path" not in list(kwargs.keys()):
                os.chdir(kwargs.get("type"))
            else:
                os.chdir(kwargs.get("path"))
            try:
                Repo.clone_from(self.FRAMEWORK_REGISTRY, kwargs.get("name"))
            except Exception as e:
                return e
            os.chdir("../")
            return dict(response=f"{type} loaded sucessfully")
        elif "from" in list(kwargs.keys()) and kwargs["from"] == "GIT_URL":
            if "path" not in list(kwargs.keys()):
                os.chdir(kwargs.get("type"))
            else:
                os.chdir(kwargs.get("path"))
            try:
                Repo.clone_from(kwargs.get("git_url"), kwargs.get("name"))
            except Exception as e:
                return e
            os.chdir("../")
            return dict(response=f"{type} loaded sucessfully")

from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

from company import Company
from exceptions import ApiException

app = FastAPI()

class CompanyController:
    @app.post("/company")
    async def create_company(name: str):
        return Company().create_company(name)

    @app.get("/company/{name}")
    async def get_company(name: str):
        return Company().get_company(name)
    

    @app.middleware("http")
    async def exception_handling(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except ApiException as ex:
            return JSONResponse(content=ex.default_public_error_message,status_code=ex.http_equivalent_status)
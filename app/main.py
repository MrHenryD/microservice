from fastapi import FastAPI

import api.v1.api as v1
import api.v2.api as v2
import api.v3.api as v3

app = FastAPI()


app.include_router(v1.api_router, prefix="/api/v1")
app.include_router(v2.api_router, prefix="/api/v2")
app.include_router(v3.api_router, prefix="/api/v3")

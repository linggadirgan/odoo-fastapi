from fastapi import FastAPI
from app.routers.api_v1 import odoo_routes

app = FastAPI(
    title="FastAPI Odoo Integration",
    description="API for integrating with Odoo using FastAPI",
    version="1.0.0"
)

# Include routers
app.include_router(odoo_routes.router, prefix="/api/v1/odoo", tags=["Production Waste"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

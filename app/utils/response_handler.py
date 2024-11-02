from fastapi.responses import JSONResponse

def create_response(data, message="Success"):
    return JSONResponse(content={"message": message, "data": data})

from fastapi.responses import JSONResponse

def success_response(data):
    response = data
    response['message'] = 'Success' 
    response['response_code'] = '0000' 
    return JSONResponse(content=response)

def notfound_response(data):
    response = data
    response['message'] = 'Data Not Found' 
    response['response_code'] = '4000' 
    return JSONResponse(content=response)

def error_response(message, data={}):
    response = data
    response['message'] = message 
    response['response_code'] = '9999' 
    return JSONResponse(content=response)
def http_status(status):
    match status:
        case 200: 
            return "ok" 
        case 404: 
            return "Found"  
        case 500: 
            return "Internal Server Error" 
        case _:
            return "Unknown status" # Usage print(http_status(500)) # Output: Internal Server
        
        
print(http_status(5007))
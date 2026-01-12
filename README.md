1. Learn the concept of the Path and Query Parameter
2. Learn the concept of serialization, and deserialization, related it with post, and put
    Think of serialization like:    
        - Writing your thoughts (object) into a letter (JSON)
        - Sending it via post (HTTP)
        - The receiver reads it and understands it

    You can’t send raw Python objects over the internet, so they must be serialized.
    Fastapi uses the pydantic models for that purpose
    Serialization is the process of converting in-memory objects into a transportable format like JSON, while deserialization converts it back into usable objects. FastAPI uses Pydantic models to handle serialization, deserialization, and validation automatically.
3. Learn About the Fastapi Header, the content-type and user-agent along with that the status code 
   as well, Header is a dependency helper in FastAPI that lets you read HTTP headers easily.Headers solve communication problems between client and server.
   
    | Part        | Meaning                            |
    | ----------- | ---------------------------------- |
    | URL         | Where the package goes             |
    | Body        | The actual data                    |
    | **Headers** | Instructions & info about the data |

4. Status Code: Status codes tell the client what happened with the request.

    | Range | Meaning       |
    | ----- | ------------- |
    | 1xx   | Informational |
    | 2xx   | Success       |
    | 3xx   | Redirection   |
    | 4xx   | Client error  |
    | 5xx   | Server error  |

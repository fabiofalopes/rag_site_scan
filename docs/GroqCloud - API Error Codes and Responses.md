---
created: 2024-10-10T10:32:20 (UTC +01:00)
tags: []
source: https://console.groq.com/docs/rate-limits
author: 
---

# GroqCloud

> ## Excerpt
> Experience the fastest inference in the world

---
## API Error Codes and Responses

Our API uses standard HTTP response status codes to indicate the success or failure of an API request. In cases of errors, the body of the response will contain a JSON object with details about the error. Below are the error codes you may encounter, along with their descriptions and example response bodies.

### [Error Codes Documentation](https://console.groq.com/docs/rate-limits#error-codes-documentation)

Our API uses specific error codes to indicate the success or failure of an API request. Understanding these codes and their implications is essential for effective error handling and debugging.

### [Success Codes](https://console.groq.com/docs/rate-limits#success-codes)

-   **200 OK**: The request was successfully executed. No further action is needed.

### [Client Error Codes](https://console.groq.com/docs/rate-limits#client-error-codes)

-   **400 Bad Request**: The server could not understand the request due to invalid syntax. Review the request format and ensure it is correct.
-   **401 Unauthorized**: The request was not successful because it lacks valid authentication credentials for the requested resource. Ensure the request includes the necessary authentication credentials and the api key is valid.
-   **404 Not Found**: The requested resource could not be found. Check the request URL and the existence of the resource.
-   **422 Unprocessable Entity**: The request was well-formed but could not be followed due to semantic errors. Verify the data provided for correctness and completeness.
-   **429 Too Many Requests**: Too many requests were sent in a given timeframe. Implement request throttling and respect rate limits.

### [Server Error Codes](https://console.groq.com/docs/rate-limits#server-error-codes)

-   **500 Internal Server Error**: A generic error occurred on the server. Try the request again later or contact support if the issue persists.
-   **502 Bad Gateway**: The server received an invalid response from an upstream server. This may be a temporary issue; retrying the request might resolve it.
-   **503 Service Unavailable**: The server is not ready to handle the request, often due to maintenance or overload. Wait before retrying the request.

### [Informational Codes](https://console.groq.com/docs/rate-limits#informational-codes)

-   **206 Partial Content**: Only part of the resource is being delivered, usually in response to range headers sent by the client. Ensure this is expected for the request being made.

### [Error Object Explanation](https://console.groq.com/docs/rate-limits#error-object-explanation)

When an error occurs, our API returns a structured error object containing detailed information about the issue. This section explains the components of the error object to aid in troubleshooting and error handling.

### [Error Object Structure](https://console.groq.com/docs/rate-limits#error-object-structure)

The error object follows a specific structure, providing a clear and actionable message alongside an error type classification:

```json
{ "error": { "message": "String - description of the specific error", "type": "invalid_request_error" } }
```

### [Components](https://console.groq.com/docs/rate-limits#components)

-   **`error` (object):** The primary container for error details.
    -   **`message` (string):** A descriptive message explaining the nature of the error, intended to aid developers in diagnosing the problem.
    -   **`type` (string):** A classification of the error type, such as `"invalid_request_error"`, indicating the general category of the problem encountered.

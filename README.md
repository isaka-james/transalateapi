
# Flask Translation Application (API) Documentation

## Overview

This document provides details on the Flask Translation Application API, which allows users to translate sentences into different languages. The API end point is  [translateapi.vercel.app/translate](https://translateapi.vercel.app/translate). 

Remember now it only receives the POST requests as mentioned below..

## Making API Requests

To translate sentences, you need to make a POST request to the API endpoint. Use the following Python code as a sample:

```python
import requests

# API endpoint URL
api_url = "https://translateapi.vercel.app/translate"

# Sample data with sentences to be translated
data = {
    "language": "english", #-> the language to be converted to
    "sentences": ["Hello, how are you?", "I love programming"]
}

# Making a POST request to the API
response = requests.post(api_url, json=data)

# Process the API response as needed
print(response.json())
```

Now for the javascript fetching to the api...

```javascript
const fetch = require('node-fetch');

// API endpoint URL
const api_url = "https://translateapi.vercel.app/translate";

// Sample data with sentences to be translated
const data = {
    language: "english", // the language to be converted to
    sentences: ["Hello, how are you?", "I love programming"]
};

// Making a POST request to the API
fetch(api_url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
.then(response => response.json())
.then(responseData => {
    // Process the API response as needed
    console.log(responseData);
})
.catch(error => console.error('Error:', error));
```

Translate your sentences with PHP..

```php
<?php

// API endpoint URL
$api_url = "https://translateapi.vercel.app/translate";

// Sample data with sentences to be translated
$data = [
    "language" => "english", // the language to be converted to
    "sentences" => ["Hello, how are you?", "I love programming"]
];

// Making a POST request to the API
$options = [
    'http' => [
        'header'  => "Content-type: application/json",
        'method'  => 'POST',
        'content' => json_encode($data),
    ],
];

$context  = stream_context_create($options);
$response = file_get_contents($api_url, false, $context);

// Process the API response as needed
var_dump(json_decode($response, true));
?>
```

For the kotlin guys..

```kotlin
import java.net.HttpURLConnection
import java.net.URL
import com.google.gson.Gson

fun main() {
    // API endpoint URL
    val apiUrl = "https://translateapi.vercel.app/translate"

    // Sample data with sentences to be translated
    val data = mapOf(
        "language" to "english", // the language to be converted to
        "sentences" to listOf("Hello, how are you?", "I love programming")
    )

    // Making a POST request to the API
    val url = URL(apiUrl)
    val connection = url.openConnection() as HttpURLConnection
    connection.requestMethod = "POST"
    connection.setRequestProperty("Content-Type", "application/json")
    connection.doOutput = true

    val outputStream = connection.outputStream
    outputStream.write(Gson().toJson(data).toByteArray())
    outputStream.flush()

    // Process the API response as needed
    val responseCode = connection.responseCode
    val response = connection.inputStream.bufferedReader().readText()
    println(response)
}
```

## Response Structure

The API responds with a JSON object containing information about the success of the translation operation or any encountered errors. The structure of the response is as follows:

### Successful Translation

If the translation is successful, the API responds with the following structure:

```json
{
    "success": true,
    "translations_swahili": ["Translated Text 1", "Translated Text 2", ...]
}
```


### For the Errors:

```json
{
    "success": false,
    "error": "Error Message"
}
```

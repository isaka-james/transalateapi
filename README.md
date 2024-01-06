# Flask Translation Application (API) Documentation

## Overview

This documentation provides comprehensive details on the Flask Translation Application API, a powerful tool designed for translating sentences into various languages. The API endpoint, [translateapi.vercel.app/translate](https://translateapi.vercel.app/translate), exclusively caters to POST requests at present.

## Making API Requests

To effectively translate sentences, initiate a POST request to the API endpoint using the provided Python, JavaScript, PHP, or Kotlin code samples:

### Python

```python
import requests

api_url = "https://translateapi.vercel.app/translate"

data = {
    "language": "swahili",
    "sentences": ["Hello, how are you?", "I love programming"]
}

response = requests.post(api_url, json=data)
print(response.json())
```

Javascript

```javascript
const fetch = require('node-fetch');

const api_url = "https://translateapi.vercel.app/translate";

const data = {
    language: "spanish",
    sentences: ["Hello, how are you?", "I love programming"]
};

fetch(api_url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
})
.then(response => response.json())
.then(responseData => {
    console.log(responseData);
})
.catch(error => console.error('Error:', error));

```

PHP

```php
<?php

$api_url = "https://translateapi.vercel.app/translate";

$data = [
    "language" => "german",
    "sentences" => ["Hello, how are you?", "I love programming"]
];

$options = [
    'http' => [
        'header'  => "Content-type: application/json",
        'method'  => 'POST',
        'content' => json_encode($data),
    ],
];

$context  = stream_context_create($options);
$response = file_get_contents($api_url, false, $context);

var_dump(json_decode($response, true));
?>

```

Kotlin

```kotlin
import java.net.HttpURLConnection
import java.net.URL
import com.google.gson.Gson

fun main() {
    val apiUrl = "https://translateapi.vercel.app/translate"

    val data = mapOf(
        "language" to "swahili",
        "sentences" to listOf("Hello, how are you?", "I love programming")
    )

    val url = URL(apiUrl)
    val connection = url.openConnection() as HttpURLConnection
    connection.requestMethod = "POST"
    connection.setRequestProperty("Content-Type", "application/json")
    connection.doOutput = true

    val outputStream = connection.outputStream
    outputStream.write(Gson().toJson(data).toByteArray())
    outputStream.flush()

    val responseCode = connection.responseCode
    val response = connection.inputStream.bufferedReader().readText()
    println(response)
}

```

## Response Structure

The API response, whether successful or encountering errors, adheres to a structured JSON format:

### Successful Translation

If the translation is successful, the API responds with the following structure:

```json
{
    "success": true,
    "translations_swahili": ["Translated Text 1", "Translated Text 2", ...]
}
```


### Errors:

```json
{
    "success": false,
    "error": "Error Message"
}
```

Remember the supported languages for now are: 

```python
language = "english"
language = "swahili"
language = "german"
language = "spanish"
language = "french"
```

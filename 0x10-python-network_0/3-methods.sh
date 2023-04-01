#!/bin/bash
#takes in a url and displays HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
#!/bin/bash
# takes url as an argument sends GET request to the URL & display response
curl -s "$1" | grep Allow:" | cut -d " " -f2-

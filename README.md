# webroot-discovery
This is a white box pen test tool to discover "hidden" files on a site without going through everything yourself.

Note that the full web catalog or source code is needed for the site you want to test.

The script goes through the catalog and crafts URLs based on the structure.

If Burp is running on `127.0.0.1:8080` the script will make GET requests to your burp proxy for further auditing.

## Usage:

`python3 webroot-discovery.py <web catalog> <target URL> <files to include e.g. php, aspx, json, *>`

### Example:

`python3 webroot-discovery.py "/home/oliver/misc/wwwroot" "google.com/" "php"`

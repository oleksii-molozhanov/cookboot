# cookboot
Cooking recipe dedicated backend  

## Run webserver from CLI
```
uvicorn --app-dir ./src  cookboot.asgi:app --reload --log-config uvicorn_log_config.json
```
`--app-dir ./src`: add `./src` to the `sys.path` to make `import` of various modules work.  
`cookboot.asgi:app`: specify the entry point for the webserver (attribute `app` of the module `cookboot.asgi`).  
` --reload`: any changes to source files will trigger an auto-reload of the webserver (usefull for local development).  
`--log-config uvicorn_log_config.json`: specify a log config file for uvicorn.  

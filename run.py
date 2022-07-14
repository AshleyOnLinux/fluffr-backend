import sys

try:
    import uvicorn
except Exception as err:
    print("Uvicorn import error.")
    print(err)
    sys.exit()

try:
    from zenlog import log
except Exception as err:
    print("Zenlog import error.")
    print(err)
    sys.exit()

isDevServer = True           # Enable hot reloading? True = Yes
host = "0.0.0.0"             # 0.0.0.0 = local ip
portNo = 443                 # Port to serve the site on. 443 = https/http
serverStartupWait = 3        # Seconds to wait before server starts serving
terminalClearCMD = "clear"   # cls = windows, clear = anything else.
logLevel = "info"            # level in what should be logged

try:
    # log.info(f"Starting server in {serverStartupWait} seconds...")
    # for _ in range(serverStartupWait):
    #     if serverStartupWait <= 5 and serverStartupWait >= 4:
    #         log.info(f"You have {serverStartupWait} seconds remaining.")
    #     elif serverStartupWait <= 3:
    #         log.warn(f"You have {serverStartupWait} seconds remaining!!")

    #     time.sleep(1)
    #     serverStartupWait -= 1
        

    # os.system(terminalClearCMD)
    # log.warn("Countdown expired.")
    # log.info("Uvicorn server is now live!")    

    uvicorn.run("app:app", host=host, 
                port=portNo, log_level=logLevel,
                reload=isDevServer)

except Exception as err:
    log.error(err)

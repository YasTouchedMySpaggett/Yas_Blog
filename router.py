from multiprocessing import freeze_support
import uvicorn
import streamsync.serve


app_path = "./yas_blog" # . for current working directory
mode = "edit" # run or edit


if __name__ == '__main__':
    asgi_app = streamsync.serve.get_asgi_app(app_path, mode)
    freeze_support()
    uvicorn.run(asgi_app,host="0.0.0.0",port=5328,log_level="warning",ws_max_size=streamsync.serve.MAX_WEBSOCKET_MESSAGE_SIZE)
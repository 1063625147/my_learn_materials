import tornado.ioloop
import tornado.web
import Hash
import json
import os


class UploadHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        file_metas = self.request.files.get('imgName', None)  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            with open('D:\\study\\python\\Graduation_project\\static\\upload\\' + filename, 'wb') as f:
                f.write(meta['body'])


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self, *args, **kwargs):
        file_metas = self.request.files.get('imgName', None)  # 提取表单中‘name’为‘file’的文件元数据
        for meta in file_metas:
            filename = meta['filename']
            imagenames = Hash.main('static/upload/' + filename)
            image_list =[]
            for imagename in imagenames:
                image_list.append("/"+imagename)
            image_dict = {
                "imgNames": image_list
            }
            jsonData = json.dumps(image_dict)
            self.write(jsonData)


class PageHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.render("view.html")


Handlers = [
    (r"/", MainHandler),
    (r"/view.html", PageHandler),
    (r"/upload", UploadHandler),
]
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "xsrf_cookies": False,
}
application = tornado.web.Application(Handlers, **settings)
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()

import web
import json
import threading

urls = ('/(.*)', 'API')
# 创建一个应用，urls参数指明了网站url与应用执行的函数间的一个映射
app = web.application(urls, globals())
# globals()会返回一个类似字典的对象，包含当前空间所有变量、函数、类及模块，
# 键是这些东西的名称，值是响应对象，由此可以通过名字来获取对象。
db = {}
nextid = 0


# Very simple REST API application built with web.py
class API():
    def GET(self, id=None):
        global db, nextid
        if (len(id) == 0):
            return json.dumps(db)
        elif (int(id) in db):
            return json.dumps(db[int(id)])
        else:
            return web.notfound()

    def POST(self, id=None):
        global db, nextid
        db[nextid] = json.loads(web.data())
        nextid += 1
        return json.dumps({'created': nextid - 1})

    def DELETE(self, id):
        global db, nextid
        if (int(id) in db):
            db.pop(int(id))
            return json.dumps({'deleted': int(id)})
        else:
            return web.notfound()

    def PUT(self, id):
        global db, nextid
        if (int(id) in db):
            db[int(id)] = json.loads(web.data())
            return json.dumps({'updated': int(id)})
        else:
            return web.notfound()


def run_server():
    thread = threading.Thread(target=app.run)
    thread.start()
    return thread


if __name__ == '__main__':
    run_server()

from _oracle_jsonrpc import getLoans, setDeposit, depositExists
import _oracle

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

import threading

class oracleThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("Starting " + self.name)
        _oracle.start()
        print ("Exiting " + self.name)


@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]

@Request.application
def jsonrpc(request):
     # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["getLoans"] = lambda: getLoans()
    dispatcher['setDeposit'] = lambda flag: setDeposit(flag)
    dispatcher['depositExists'] = lambda lenderCred: depositExists(lenderCred)
    dispatcher["echo"] = lambda s: s

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    oracle = oracleThread(1, "Oracle Thread", 1)
    oracle.start()
    run_simple('localhost', 8546, jsonrpc)
    oracle.join()

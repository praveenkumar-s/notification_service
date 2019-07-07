from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/auth/create_token')
def create_token():
    pass

@app.route('/auth/tokens/{token}', methods=['POST'])
def updateToken():
    pass

@app.route('/auth/tokens/usage', methods =['GET'])
def getTokenUsage():
    pass

@app.route('/template/create')
def createTemplate():
    pass

@app.route('/template/{template_id}',methods=['POST'])
def updateTemplate(template_id):
    pass


@app.route('/smtp/create')
def createSMTP():
    pass

@app.route('/smtp/{id}', methods=['POST'])
def updateSMTP(id):
    pass

@app.route('/logs', methods = ['GET'])
def getAllLogsPaginated():
    pass

@app.route('/logs/{id}',methods = ['GET'])
def getLogbyID(id):
    pass

@app.route('/mail_job/add', methods = ['GET','POST'])
def perform_mailJob():
    pass

@app.route('/mailjob/status/{id}', methods =['GET'])
def getStatusOfMailJob(id):
    pass





if __name__ == '__main__':
    app.run()
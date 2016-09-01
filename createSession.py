from config import WEBLAB_USERNAME, WEBLAB_PASSWORD, APPLICATION_ROOT, PORT
import json, requests
from time import strftime
import os

def main():
    ip= 'localhost:'+str(PORT)+APPLICATION_ROOT
    username="Tester"


#    try:
    session_id,url = createSession(username,ip)
    option = 0
    while option in (0,1,2):
        print 'Session ID: '+ session_id
        print 'URL: '+ url +'\n'
        print '1.         Check user status'
        print '2.         Kick user out'
        print 'Other.     Exit \n'
        option = input('Option: ')
        if option == 1: checkStatus(ip, session_id)
        elif option == 2: kickOut(ip, session_id)
        else: print 'Goodbye'

#    except:
#        print 'labSessionCreator.py -u <username> -s <server_ip_adress>'




def createSession(user,ip):

    client_initial_data = {
        'back':'http://weblab.deusto.es',
        'url':'http://'+ip+'/weblab/sessions/'
    }

    server_initial_data = {
        'priority.queue.slot.start': strftime("%Y-%m-%d %H:%M:%S")+'.000',
        'priority.queue.slot.length': 200,
        'request.username': user
    }


    serialized_client_initial_data = json.dumps(client_initial_data)
    serialized_server_initial_data = json.dumps(server_initial_data)
    back_url = json.loads(serialized_client_initial_data).get('back','')
    url = json.loads(serialized_client_initial_data).get('url','')
    data = {
        'client_initial_data' : serialized_client_initial_data,
        'server_initial_data' : serialized_server_initial_data,
        'back' : back_url,
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain','authorization':WEBLAB_USERNAME+':'+WEBLAB_PASSWORD}
    resp = requests.post(url, data=json.dumps(data), headers=headers, auth=(WEBLAB_USERNAME,WEBLAB_PASSWORD))
    url=json.loads(resp.content).get('url','')
    session_id = json.loads(resp.content).get('session_id','')

    os.system('nohup google-chrome '+url+ ' &')
    os.system('clear')
    return session_id, url

def checkStatus(ip, session_id):
    os.system('clear')
    url = 'http://'+ ip +'/weblab/sessions/'+ session_id + '/status'
    resp = requests.get(url, auth=(WEBLAB_USERNAME,WEBLAB_PASSWORD))
    print 'Response: '+ resp.text

def kickOut(ip, session_id):
    os.system('clear')
    url = 'http://'+ ip +'/weblab/sessions/'+ session_id
    data = {'action' : "delete"}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.post(url, data=json.dumps(data), headers=headers, auth=(WEBLAB_USERNAME,WEBLAB_PASSWORD))
    print 'Response: '+ resp.text


if __name__ == "__main__":
   main()

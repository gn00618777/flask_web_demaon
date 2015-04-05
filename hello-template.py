from flask import Flask,send_from_directory,request,render_template
from filter import nl2br
from werkzeug import secure_filename

UPLOAD_FOLDER='/flask_web_demaon/ovpn_files/'

app=Flask(__name__)

app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.jinja_env.filters['nl2br']=nl2br

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1 )[1] in ALLOWED_EXTENSIONS

@app.route("/refresh_PPP_Account_html", methods=['GET','POST'])
def refresh_PPP_Account_html():
    return send_from_directory('static/report/flexmonkey/html','PPP_Account.html')

@app.route("/transter_to_interfaces", methods=['GET','POST'])
def transter_to_interfaces():
    import subprocess
    cmd=subprocess.Popen(['ifconfig'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out,err=cmd.communicate()
    templateData={

        'result' : out

    }
    return render_template('net_interfaces.html', **templateData)

@app.route("/<path:filename>")
def showpage(filename):
    return send_from_directory('static/report/flexmonkey/html',filename)

@app.route("/start_pptp_server",methods=['GET','POST'])
def start_pptp_server():
    import subprocess
    server_name=request.form['server_name']
    server_ip=request.form['server_ip']
    clients_ip=request.form['clients_ip']
    subprocess.call(['./revise_pptp_server_config.sh',server_name,server_ip,clients_ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    return send_from_directory('static/report/flexmonkey/html','handling.html')

@app.route("/apply_to_pptp_server",methods=['GET','POST'])
def apply_to_pptp_server():
    import subprocess
    subprocess.call(['./restart_pptp_server.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  
    return send_from_directory('static/report/flexmonkey/html','handling.html')

@app.route("/add_new_account", methods=['GET','POST'])
def add_new_account():

    return send_from_directory('static/report/flexmonkey/html','add_ppp_account.html')

@app.route("/create_new_account",methods=['GET','POST'])
def create_new_account():
    import subprocess
    ppp_account=request.form['ppp_account']
    ppp_password=request.form['ppp_password']
    subprocess.call(['./record_account_password.sh',ppp_account,ppp_password],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return send_from_directory('static/report/flexmonkey/html','PPP_Account.html')

@app.route("/remove_accounts",methods=['GET','POST'])
def remove_accounts():
    import subprocess
    value=request.form['account']
    subprocess.call(['./remove_account.sh',value],stdout=subprocess.PIPE,stderr=subprocess.PIPE) 
    return send_from_directory('static/report/flexmonkey/html','PPP_Account.html')

@app.route("/pptp_client",methods=['GET','POST'])
def connect_to_server_previous():
    import subprocess
    tunnel_name=request.form['tunnel_name']
    server_ip=request.form['server_ip']
    user_name=request.form['user_name']
    user_password=request.form['user_password']
    server_name=request.form['server_name']

    cmd=subprocess.Popen(['./create_tunnel.sh',tunnel_name, server_ip, user_name, user_password, server_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,error=cmd.communicate()

    return send_from_directory('static/report/flexmonkey/html','handling.html')

@app.route("/connect_to_server_with",methods=['GET','POST'])
def connect_to_server_with():
    import subprocess
    import time
    tunnel_name=request.form['tunnel_name_to_be_connect']
    subprocess.call(['./pon_tunnel.sh',tunnel_name],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)
    cmd=subprocess.Popen(['ifconfig'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error=cmd.communicate()
    templateData={

        'result' : out,
        'result1' : error

    }
    return render_template('show_connect_state.html',**templateData)

@app.route('/back_to_show_tunnel',methods=['GET','POST'])
def back_to_show_tunnel():
    import subprocess
    cmd=subprocess.Popen(['cat','tunnel_list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,error=cmd.communicate()
    templateData={

            'result' : out
    }
    return render_template('show_tunnel.html',**templateData)

@app.route("/disconnect_from_server",methods=['GET','POST'])
def disconnect_from_server():
    import subprocess
    import time
    tunnel_name=request.form['tunnel_name_to_be_disconnect']
    subprocess.Popen(['./poff_tunnel.sh',tunnel_name],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    time.sleep(1)
    cmd=subprocess.Popen(['ifconfig'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out,error=cmd.communicate()
    templateData={

        'result' : out

    }
    return render_template('test1.html',**templateData)

@app.route("/add_new_tunnel",methods=['GET','POST'])
def add_new_tunnel():
    return send_from_directory('static/report/flexmonkey/html','PPTP_Client.html')

@app.route("/connect_to_server",methods=['GET','POST'])
def connect_to_server():
    import subprocess
    cmd=subprocess.Popen(['cat','tunnel_list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,error=cmd.communicate()
    templateData={

        'result' : out,

    }
    return render_template('show_tunnel.html',**templateData)


@app.route("/remove_the_tunnel",methods=['GET','POST'])
def remove_tunnel():
    import subprocess
    cmd=subprocess.Popen(['cat','tunnel_list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,error=cmd.communicate()
    templateData={

      'result' : out

    }
    return render_template('remove_tunnel.html',**templateData)

@app.route("/button_to_remove_tunnel", methods=['GET','POST'])
def button_to_remove():
    import subprocess
    tunnel_name=request.form['tunnel_be_remove']
    subprocess.Popen(['./remove_tunnel.sh',tunnel_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return send_from_directory('static/report/flexmonkey/html','handling.html')


@app.route("/move_to_openvpn_server_state",methods=['GET','POST'])
def move_to_openvpn_server_state():
    import subprocess
    cmd=subprocess.Popen(['./judge_server_state.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out=cmd.communicate()

    if out == ('0\n','') :
       return send_from_directory('static/report/flexmonkey/html','openVPN_server.html')
    else :
       return send_from_directory('static/report/flexmonkey/html','show_openVPN_server_state.html')

@app.route("/start_openVPN_server", methods=['GET','POST'])
def start_OpenVPNserver():
    import subprocess
    import os
    domain_select=request.form['domain_select']
    clients_amounts=request.form['clients_num_select']
    subprocess.call(['./revise_openVPN_server_conf.sh',domain_select,clients_amounts],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    subprocess.call(['./create_new_ca.sh',clients_amounts],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    cmd=subprocess.Popen(['./judge_openVPN_server_run.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out=cmd.communicate()
    if out == ('0\n', ''):
        subprocess.call(['./start_openVPN_server.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

        return send_from_directory('static/report/flexmonkey/html','show_openVPN_server_state.html')
    else:
        return send_from_directory('static/report/flexmonkey/html','show_wrong_openVPN_server_msg.html')

@app.route("/back_to_start_openVPN_server_html", methods=['GET','POST'])
def back_to_start_openvpn_server_html():
    return send_from_directory('static/report/flexmonkey/html','openVPN_server.html')


@app.route("/stop_openVPN_server",methods=['GET','POST'])
def stop_openVPN_server():
    import subprocess
 
    subprocess.call(['./stop_openVPN_server.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return send_from_directory('static/report/flexmonkey/html','openVPN_server.html')


@app.route("/move_to_client_config_dir_html",methods=['GET','POST'])
def move_to_client_config_dir_html():
    
    return send_from_directory('static/report/flexmonkey/html','client_config_dir.html')

@app.route("/amount_of_clients",methods=['GET','POST'])
def amount_of_clients():
    import subprocess
    client_number_select=request.form['client_number_select']
    subprocess.call(['./control_ccd.sh',client_number_select],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return send_from_directory('static/report/flexmonkey/html','client_config_dir.html')

@app.route("/<path:add_config_client>",methods=['GET','POST'])
def add_config_client1(add_config_client):
    import subprocess


    if add_config_client == "add_config_client1":
        add_config_client = "add_config_client1"
    elif add_config_client == "add_config_client2":
        add_config_client = "add_config_client2"
    elif add_config_client == "add_config_client3":
        add_config_client = "add_config_client3"
    elif add_config_client == "add_config_client4":
        add_config_client = "add_config_client4"
    elif add_config_client == "add_config_client5":
        add_config_client = "add_config_client5"
    elif add_config_client == "add_config_client6":
        add_config_client = "add_config_client6"
    elif add_config_client == "add_config_client7":
        add_config_client = "add_config_client7"
    elif add_config_client == "add_config_client8":
        add_config_client = "add_config_client8"
    elif add_config_client == "add_config_client9":
        add_config_client = "add_config_client9"
    elif add_config_client == "add_config_client10":
        add_config_client = "add_config_client10"
    elif add_config_client == "add_config_client11":
        add_config_client = "add_config_client11"
    elif add_config_client == "add_config_client12":
        add_config_client = "add_config_client12"
    elif add_config_client == "add_config_client13":
        add_config_client = "add_config_client13"
    elif add_config_client == "add_config_client14":
        add_config_client = "add_config_client14"
    else:
        add_config_client = "add_config_client15"

    subnet_text=request.form['subnet_text']
    subprocess.call(['./show_config_client.sh',add_config_client,subnet_text],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return send_from_directory('static/report/flexmonkey/html','client_config_dir.html')



@app.route("/connect_to_server_with_ovpn",methods=['GET','POST'])
def connect_to_server_with_ovpn():
    import subprocess
    ovpn_file=request.form['ovpn_files']
    fdout=open("bernieout",'w')
    fderr=open("bernieerr",'w')
    cmd=subprocess.Popen(['./connect_server_with_ovpn.sh',ovpn_file],stdout=fdout,stderr=fderr)
   
    return render_template('openVPN_client_state.html')

@app.route("/remove_ovpn_file",methods=['GET','POST'])
def remove_ovpn_file():
    import subprocess
    ovpn_files1=request.form['ovpn_files1']
    subprocess.call(['./remove_ovpn_file.sh',ovpn_files1],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return send_from_directory('static/report/flexmonkey/html','connect_server_with_ovpn.html')

@app.route("/update_connect_message", methods=['GET','POST'])
def update_connect_message():
    fdout=open('bernieout','r')
    contentout=fdout.read()
    templateData={

      'result' : contentout
 
    }
    fdout.close()
    return render_template('openVPN_client_state.html',**templateData)


@app.route("/disconnect_ovpn_from_server",methods=['GET','POST'])
def disconnect_ovpn_from_server():
    import subprocess
    subprocess.Popen(['./disconnect_ovpn_from_server.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    return send_from_directory('static/report/flexmonkey/html','handling.html')

@app.route("/direct_to_openVPN_client_state",methods=['GET','POST'])
def direct_to_openVPN_client_state():
    import subprocess
    cmd=subprocess.Popen(['./judge_if_openvpn_ps.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out=cmd.communicate()
    print(out) 
    if out == ('0\n',''):
       return send_from_directory('static/report/flexmonkey/html','connect_server_with_ovpn.html')
    else :
        return render_template('openVPN_client_state.html')


@app.route("/go_to_openVPN_connect_state_html",methods=['GET','POST'])
def go_to_openVPN_client_state_html():

    return render_template('openVPN_client_state.html')

@app.route("/remove_ovpn", methods=['GET','POST'])
def remove_ovpn():
    import subprocess
    cmd=subprocess.Popen(['./check_ovpn_file_list.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,error=cmd.communicate()
    templateData={

        'result' : out

    }
    return render_template('remove_ovpn.html',**templateData)

@app.route("/remove_ovpn_form", methods=['GET','POST'])
def remove_ovpn_form():
    return send_from_directory('static/report/flexmonkey/html','ovpn_control.html')

@app.route("/file_to_upload", methods=['GET','POST'])
def file_to_upload():
    return send_from_directory('static/report/flexmonkey/html','upload.html')

@app.route('/upload_file_form',methods=['GET','POST'])
def upload_file():
        import os
        import subprocess

        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cmd=subprocess.Popen(['./add_to_ovpn_list.sh',filename],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out=cmd.communicate()
        print(out)
        if out == ('0\n',''):
           return send_from_directory('static/report/flexmonkey/html','handling.html')
        else:
           return send_from_directory('static/report/flexmonkey/html','wrong_format.html')

@app.route("/back_to_upload_html",methods=['GET','POST'])
def back_to_upload_html():
         return send_from_directory('static/report/flexmonkey/html','upload.html')

@app.route("/transter_to_gpio_control",methods=['GET','POST'])
def transter_to_gpio_control():

	import subprocess

        cmd=subprocess.Popen(['./cat_gpio.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out,err=cmd.communicate()
        templateData={

            'result': out

        }
	return render_template('gpio_control.html',**templateData)

@app.route("/transter_to_WIFI_html",methods=['GET','POST'])
def search_SSID():

    return render_template('WIFI.html')

@app.route("/connect_WIFI",methods=['GET','POST'])
def connect_WIFI():
    return send_from_directory('static/report/flexmonkey/html','test.html')

if __name__=="__main__":
   app.run(host='192.168.10.128',port=1300,debug=True)

#!/usr/local/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import requests

###########################################################
# File: srltd_weeklystats.py                              #
# Author: Rommel Rico                                     #
# Last Modified: 25/Aug/2015                              #
# Description: This script sends me an email to post the  #
#   organizational statistics on the Storm Riders forums. #
###########################################################

#Global Variables
API_URL = 'https://robertsspaceindustries.com/api/arena-commander/getLeaderboard'

#Main function
def main():
    br_stats = get_br_stats()
    sb_stats = get_sb_stats()
    cc_stats = get_cc_stats()
    vs_stats = get_vs_stats()
    mc_ov_stats = get_mc_ov_stats()
    mc_rm_stats = get_mc_rm_stats()
    mc_dl_stats = get_mc_dl_stats()
    send_mail(br_stats, sb_stats, cc_stats, vs_stats, mc_ov_stats, mc_rm_stats, mc_dl_stats)

#Returns SRLTD stats for Battle Royale
def get_br_stats():
    values = "{\"mode\":\"BR\",\"map\":\"MAP-ANY\",\"handle\":\"\",\"org\":\"srltd\",\"season\":\"1.1.6\",\"pagesize\":\"10\",\"page\":\"1\"}"
    resp = requests.post(API_URL, data=values, allow_redirects=True)
    stats = "<p>[table][b]Battle Royale[/b]<br/>"
    stats += "[tr][td]Rank[/td][td]Nickname[/td][td]Kills[/td][td]KDR[/td][td]Puntos por Minuto[/tr]<br/>"
    for index, stormrider in enumerate(resp.json()['data']['resultset']):
        if index == 0:
            stats += "[tr][td][color=yellow]" + str(index+1) + "[/color][/td][td][color=yellow]" + str(stormrider['nickname']) + "[/color][/td][td][color=yellow]" + str(stormrider['kills']) + "[/color][/td][td][color=yellow]" + str(stormrider['kill_death_ratio']) + "[/color][/td][td][color=yellow]" + str(stormrider['score_minute']) + "[/color][/td][/tr]<br/>"
        elif index == 1:
            stats += "[tr][td][color=silver]" + str(index+1) + "[/color][/td][td][color=silver]" + str(stormrider['nickname']) + "[/color][/td][td][color=silver]" + str(stormrider['kills']) + "[/color][/td][td][color=silver]" + str(stormrider['kill_death_ratio']) + "[/color][/td][td][color=silver]" + str(stormrider['score_minute']) + "[/color][/td][/tr]<br/>"
        elif index == 2:
            stats += "[tr][td][color=brown]" + str(index+1) + "[/color][/td][td][color=brown]" + str(stormrider['nickname']) + "[/color][/td][td][color=brown]" + str(stormrider['kills']) + "[/color][/td][td][color=brown]" + str(stormrider['kill_death_ratio']) + "[/color][/td][td][color=brown]" + str(stormrider['score_minute']) + "[/color][/td][/tr]<br/>"
        else:
            stats += "[tr][td]" + str(index+1) + "[/td][td]" + str(stormrider['nickname']) + "[/td][td]" + str(stormrider['kills']) + "[/td][td]" + str(stormrider['kill_death_ratio']) + "[/td][td]" + str(stormrider['score_minute']) + "[/td][/tr]<br/>"
    stats += "[/table]</p>"
    return stats

#Returns SRLTD stats for Squadron Battle
def get_sb_stats():
    values = "{\"mode\":\"SB\",\"map\":\"MAP-ANY\",\"handle\":\"\",\"org\":\"srltd\",\"season\":\"1.1.6\",\"pagesize\":\"10\",\"page\":\"1\"}"
    resp = requests.post(API_URL, data=values, allow_redirects=True)
    stats = "<p>[table][b]Squadron Battle[/b]<br/>"
    stats += "[tr][td]Rank[/td][td]Nickname[/td][td]WLR[/td][td]KDR[/td][/tr]<br/>"
    for index, stormrider in enumerate(resp.json()['data']['resultset']):
        if index == 0:
            stats += "[tr][td][color=yellow]" + str(index+1) + "[/color][/td][td][color=yellow]" + str(stormrider['nickname']) + "[/color][/td][td][color=yellow]" + str(stormrider['win_loss_ratio']) + "[/color][/td][td][color=yellow]" + str(stormrider['kill_death_ratio']) + "[/color][/td][/tr]<br/>"
        elif index == 1:
            stats += "[tr][td][color=silver]" + str(index+1) + "[/color][/td][td][color=silver]" + str(stormrider['nickname']) + "[/color][/td][td][color=silver]" + str(stormrider['win_loss_ratio']) + "[/color][/td][td][color=silver]" + str(stormrider['kill_death_ratio']) + "[/color][/td][/tr]<br/>"
        elif index == 2:
            stats += "[tr][td][color=brown]" + str(index+1) + "[/color][/td][td][color=brown]" + str(stormrider['nickname']) + "[/color][/td][td][color=brown]" + str(stormrider['win_loss_ratio']) + "[/color][/td][td][color=brown]" + str(stormrider['kill_death_ratio']) + "[/color][/td][/tr]<br/>"
        else:
            stats += "[tr][td]" + str(index+1) + "[/td][td]" + str(stormrider['nickname']) + "[/td][td]" + str(stormrider['win_loss_ratio']) + "[/td][td]" + str(stormrider['kill_death_ratio']) + "[/td][/tr]<br/>"
    stats += "[/table]</p>"
    return stats

#Return SRLTD stats for Capture the Core
def get_cc_stats():
# {"mode":"CC","map":"MAP-ANY","handle":"","org":"","season":"1","pagesize":"100","page":1}
    values = "{\"mode\":\"CC\",\"map\":\"MAP-ANY\",\"handle\":\"\",\"org\":\"srltd\",\"season\":\"1.1.6\",\"pagesize\":\"10\",\"page\":\"1\"}"
    resp = requests.post(API_URL, data=values, allow_redirects=True)
    stats = "<p>[table][b]Capture the Core[/b]<br/>"
    stats += "[tr][td]Rank[/td][td]Nickname[/td][td]Captura del Nucleo[/td][td]Derribos del Cargador del Nucleo[/td][/tr]<br/>"
    for index, stormrider in enumerate(resp.json()['data']['resultset']):
        if index == 0:
            stats += "[tr][td][color=yellow]" + str(index+1) + "[/color][/td][td][color=yellow]" + str(stormrider['nickname']) + "[/color][/td][td][color=yellow]" + str(stormrider['core_captures']) + "[/color][/td][td][color=yellow]" + str(stormrider['core_carrier_kills']) + "[/color][/td][/tr]<br/>"
        elif index == 1:
            stats += "[tr][td][color=silver]" + str(index+1) + "[/color][/td][td][color=silver]" + str(stormrider['nickname']) + "[/color][/td][td][color=silver]" + str(stormrider['core_captures']) + "[/color][/td][td][color=silver]" + str(stormrider['core_carrier_kills']) + "[/color][/td][/tr]<br/>"
        elif index == 2:
            stats += "[tr][td][color=brown]" + str(index+1) + "[/color][/td][td][color=brown]" + str(stormrider['nickname']) + "[/color][/td][td][color=brown]" + str(stormrider['core_captures']) + "[/color][/td][td][color=brown]" + str(stormrider['core_carrier_kills']) + "[/color][/td][/tr]<br/>"
        else:
            stats += "[tr][td]" + str(index+1) + "[/td][td]" + str(stormrider['nickname']) + "[/td][td]" + str(stormrider['core_captures']) + "[/td][td]" + str(stormrider['core_carrier_kills']) + "[/td][/tr]<br/>"
    stats += "[/table]</p>"
    return stats

#Returns SRLTD stats for Vanduul Swarm Co-Op 
def get_vs_stats():
    values = "{\"mode\":\"VC\",\"map\":\"MAP-ANY\",\"handle\":\"\",\"org\":\"srltd\",\"season\":\"1.1.6\",\"pagesize\":\"10\",\"page\":\"1\"}"
    resp = requests.post(API_URL, data=values, allow_redirects=True)
    stats = "<p>[table][b]Vanduul Swarm Co-op[/b]<br/>"
    stats += "[tr][td]Rank[/td][td]Nickname[/td][td]Kills[/td][td]KDR[/td][/tr]<br/>"
    for index, stormrider in enumerate(resp.json()['data']['resultset']):
        if index == 0:
            stats += "[tr][td][color=yellow]" + str(index+1) + "[/color][/td][td][color=yellow]" + str(stormrider['nickname']) + "[/color][/td][td][color=yellow]" + str(stormrider['kills']) + "[/color][/td][td][color=yellow]" + str(stormrider['kill_death_ratio']) + "[/color][/td][/tr]<br/>"
        elif index == 1:
            stats += "[tr][td][color=silver]" + str(index+1) + "[/color][/td][td][color=silver]" + str(stormrider['nickname']) + "[/color][/td][td][color=silver]" + str(stormrider['kills']) + "[/color][/td][td][color=silver]" + str(stormrider['kill_death_ratio']) + "[/color][/td][/tr]<br/>"
        elif index == 2:
            stats += "[tr][td][color=brown]" + str(index+1) + "[/color][/td][td][color=brown]" + str(stormrider['nickname']) + "[/color][/td][td][color=brown]" + str(stormrider['kills']) + "[/color][/td][td][color=brown]" + str(stormrider['kill_death_ratio']) + "[/color][/td][/tr]<br/>"
        else:
            stats += "[tr][td]" + str(index+1) + "[/td][td]" + str(stormrider['nickname']) + "[/td][td]" + str(stormrider['kills']) + "[/td][td]" + str(stormrider['kill_death_ratio']) + "[/td][/tr]<br/>"
    stats += "[/table]</p>"
    return stats

#Returns SRLTD stats for Murray Cup, Old Vanderval
def get_mc_ov_stats():
    values = "{\"mode\":\"RU\",\"map\":\"OLD-VANDERVAL\",\"handle\":\"\",\"org\":\"srltd\",\"season\":\"1.1.6\",\"pagesize\":\"10\",\"page\":\"1\"}"
    resp = requests.post(API_URL, data=values, allow_redirects=True)
    stats = "<p>[table][b]Murray Cup, Old Vanderval[/b]<br/>"
    stats += "[tr][td]Rank[/td][td]Nickname[/td][td]Mejor Vuelta[/td][td]Mejor Carrera[/td][/tr]<br/>"
    for index, stormrider in enumerate(resp.json()['data']['resultset']):
        if index == 0:
            stats += "[tr][td][color=yellow]" + str(index+1) + "[/color][/td][td][color=yellow]" + str(stormrider['nickname']) + "[/color][/td][td][color=yellow]" + str(stormrider['best_lap']) + "[/color][/td][td][color=yellow]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        elif index == 1:
            stats += "[tr][td][color=silver]" + str(index+1) + "[/color][/td][td][color=silver]" + str(stormrider['nickname']) + "[/color][/td][td][color=silver]" + str(stormrider['best_lap']) + "[/color][/td][td][color=silver]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        elif index == 2:
            stats += "[tr][td][color=brown]" + str(index+1) + "[/color][/td][td][color=brown]" + str(stormrider['nickname']) + "[/color][/td][td][color=brown]" + str(stormrider['best_lap']) + "[/color][/td][td][color=brown]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        else:
            stats += "[tr][td]" + str(index+1) + "[/td][td]" + str(stormrider['nickname']) + "[/td][td]" + str(stormrider['best_lap']) + "[/td][td]" + str(stormrider['best_race']) + "[/td][/tr]<br/>"
    stats += "[/table]</p>"
    return stats

#Returns SRLTD stats for Murray Cup, Rikkord Memorial Raceway
def get_mc_rm_stats():
    values = "{\"mode\":\"RU\",\"map\":\"RIKKORD-MEMORIAL-RACEWAY\",\"handle\":\"\",\"org\":\"srltd\",\"season\":\"1.1.6\",\"pagesize\":\"10\",\"page\":\"1\"}"
    resp = requests.post(API_URL, data=values, allow_redirects=True)
    stats = "<p>[table][b]Murray Cup, Rikkord Memorial Raceway[/b]<br/>"
    stats += "[tr][td]Rank[/td][td]Nickname[/td][td]Mejor Vuelta[/td][td]Mejor Carrera[/td][/tr]<br/>"
    for index, stormrider in enumerate(resp.json()['data']['resultset']):
        if index == 0:
            stats += "[tr][td][color=yellow]" + str(index+1) + "[/color][/td][td][color=yellow]" + str(stormrider['nickname']) + "[/color][/td][td][color=yellow]" + str(stormrider['best_lap']) + "[/color][/td][td][color=yellow]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        elif index == 1:
            stats += "[tr][td][color=silver]" + str(index+1) + "[/color][/td][td][color=silver]" + str(stormrider['nickname']) + "[/color][/td][td][color=silver]" + str(stormrider['best_lap']) + "[/color][/td][td][color=silver]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        elif index == 2:
            stats += "[tr][td][color=brown]" + str(index+1) + "[/color][/td][td][color=brown]" + str(stormrider['nickname']) + "[/color][/td][td][color=brown]" + str(stormrider['best_lap']) + "[/color][/td][td][color=brown]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        else:
            stats += "[tr][td]" + str(index+1) + "[/td][td]" + str(stormrider['nickname']) + "[/td][td]" + str(stormrider['best_lap']) + "[/td][td]" + str(stormrider['best_race']) + "[/td][/tr]<br/>"
    stats += "[/table]</p>"
    return stats

#Returns SRLTD stats for Murray Cup, Defford Link
def get_mc_dl_stats():
    values = "{\"mode\":\"RU\",\"map\":\"DEFFORD-LINK\",\"handle\":\"\",\"org\":\"srltd\",\"season\":\"1.1.6\",\"pagesize\":\"10\",\"page\":\"1\"}"
    resp = requests.post(API_URL, data=values, allow_redirects=True)
    stats = "<p>[table][b]Murray Cup, Defford Link[/b]<br/>"
    stats += "[tr][td]Rank[/td][td]Nickname[/td][td]Mejor Vuelta[/td][td]Mejor Carrera[/td][/tr]<br/>"
    for index, stormrider in enumerate(resp.json()['data']['resultset']):
        if index == 0:
            stats += "[tr][td][color=yellow]" + str(index+1) + "[/color][/td][td][color=yellow]" + str(stormrider['nickname']) + "[/color][/td][td][color=yellow]" + str(stormrider['best_lap']) + "[/color][/td][td][color=yellow]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        elif index == 1:
            stats += "[tr][td][color=silver]" + str(index+1) + "[/color][/td][td][color=silver]" + str(stormrider['nickname']) + "[/color][/td][td][color=silver]" + str(stormrider['best_lap']) + "[/color][/td][td][color=silver]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        elif index == 2:
            stats += "[tr][td][color=brown]" + str(index+1) + "[/color][/td][td][color=brown]" + str(stormrider['nickname']) + "[/color][/td][td][color=brown]" + str(stormrider['best_lap']) + "[/color][/td][td][color=brown]" + str(stormrider['best_race']) + "[/color][/td][/tr]<br/>"
        else:
            stats += "[tr][td]" + str(index+1) + "[/td][td]" + str(stormrider['nickname']) + "[/td][td]" + str(stormrider['best_lap']) + "[/td][td]" + str(stormrider['best_race']) + "[/td][/tr]<br/>"
    stats += "[/table]</p>"
    return stats

#Send Email to Rommel to post in the forums
def send_mail(br_stats, sb_stats, cc_stats, vs_stats, mc_ov_stats, mc_rm_stats, mc_dl_stats):
    me  = "me@YOUR_DOMAIN.com"    #Sender email
    you = "me@YOUR_DOMAIN.com"   #Recipient email
   
    #Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Estadisticas Semanales SRLTD"
    msg['From'] = me
    msg['To'] = you
 
    #Create the body of the message (plan-text and HTML versions)
    text = "%s\n %s\n %s\n %s\n %s\n %s\n %s" % (br_stats, sb_stats, cc_stats, vs_stats, mc_ov_stats, mc_rm_stats, mc_dl_stats)
    
    html = """
        <html>
        <head><title>Estadisticas Semanales SRLTD</title></head>
        <body>
          <p>[center][size=20pt]Estadisticas Semanales STORM RIDERS LTD[/size][/center]
[center][img]http://i.imgur.com/CgSxl6y.png[/img][/center]</p>
          %s<br/>
          %s<br/>
          %s<br/>
          %s<br/>
          %s<br/>
          %s<br/>
          %s<br/>
          <p>[size=12pt]NOTA[/size]: 
Grupos de Lore, Diseno, Programadores, Liderazgo, etc., si ven algo que se puede mejorar en este post, mandenme un mensaje privado o posteen un reply y trabajemos juntos! Las estadisticas salen de manera automatica los Viernes de cada Semana a las 15:00 UTC.</p>
        </body>
        </html>
    """ % (br_stats, sb_stats, cc_stats, vs_stats, mc_ov_stats, mc_rm_stats, mc_dl_stats)

    #Record the MIME types of both parts
    part1 = MIMEText(text.encode('utf-8'), 'plain', 'utf-8')
    part2 = MIMEText(html.encode('utf-8'), 'html', 'utf-8')

    #Attach parts into message container. HTML section is last and thus preferred.
    msg.attach(part1)
    msg.attach(part2)

    #Send the message via SMTP server
    s = smtplib.SMTP('smtp.YOUR_DOMAIN.com')
    s.login('YOUR_USERNAME', 'YOUR_PASSWORD')
    s.sendmail(me, you, msg.as_string())
    s.quit()

#Launch program
if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

cl = LINETCR.LINE()

cl.login(token="Em7SkiqELr5IZWNbGvA8.mo/iIpXMm/2U/v+MJgHSsa.E21SDqcPEP1WwrRKop+ujSyUn5TdM/ysfXgJi0RhrrU=")

cl.loginResult()


ki = LINETCR.LINE()

ki.login(token="Emn615YzQHIzVqlHIAF2.54Ue5vxhzazXL1AqTT8NeG.xqkBTaILdR6xP7UC6d/UXltdURTGrdG/S79jtD0V2yM=")

ki.loginResult()


ki2 = LINETCR.LINE()

ki2.login(token="EmKftNveWryX3iapqbwe.60NNbOgNoAeqMp1L62cEpG.w98CM13iQ1sltz8/4FyAjDS6LfcSKIsvOgvP6fh2Rc4=")

ki2.loginResult()


ki3 = LINETCR.LINE()

ki3.login(token="Emap4F7W2bID2E1GfuQ4.T2VtN7n/mDvFrkBwmVqQDa.jH38sV4Kf0la97HxA1KHUH7j/SylNOVIbdnAq8CegtE=")

ki3.loginResult()


ki4 = LINETCR.LINE()

ki4.login(token="Em8bH4Cs4lLzHMHkL4T5.hiIwQE9ldFfhL3a8C94l5q.1qhITfyU04vWtuyJBd0gVxz/WStRQraO2FKkTvWpjzo=")

ki4.loginResult()


ki5 = LINETCR.LINE()

ki5.login(token="EmICorDtLbsR2QjaUNVf.Ovw+UKye1xfTV+zKxwoBtW.OwoB2cG1Ktbz/V482T2WbaMGiO9Zv9S6i2XsVQ7zoFY=")

ki5.loginResult()


ki6 = LINETCR.LINE()

ki6.login(token="EmR418MmdS2MwbCHLSHe.DNcjB3AgaMigrbmdeISphG.Wbg3M4Fzujk7lLwbJN+MGlkMlTH9YmwoM9Opqna14Vw=")

ki6.loginResult()


ki7 = LINETCR.LINE()

ki7.login(token="Emwl1WCKsxexQK0L9vM0.hIvl/2gfxP6SsXSqGjs2aa.fLcVjgklHWl3p+bhLglr0yIW8auB/k/jsWuiNktdhi0=")

ki7.loginResult()


ki8 = LINETCR.LINE()

ki8.login(token="EmRDwgRF4hktAb8N3db9.r9C7KyV32gZPqgpscode6q./xL3rTt4/U7e+tzrfwMvWF5NB4JEYa6jD89ZBcciDxE=")

ki8.loginResult()


ki9 = LINETCR.LINE()

ki9.login(token="Em7j3LeBF5gzJxBSdJK3.2C54SsfW3HH1kWYh7OaMWW.zs1ZUcHVD/L3wGjILZx8P3M5OlzHW9WZGgYKKDFKoSc=")

ki9.loginResult()


ki10 = LINETCR.LINE()

ki10.login(token="EmQGPi5HQOmLNIQ7xied.GA7t2NpAkdgSX0KBSyP3Fq.Mjabq+ilDSDmhgHYKy7KMmuatLfHuamhweOj/Y6k/5E=")

ki10.loginResult()

cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" **Girls chatBot Help Menu**
â† Public Commandâ†ž
âˆš [Bot]- -Show Contact All Bot                    
âˆš [Group id]- -Show Group ID        
âˆš [Ginfo]- -Show Group Info            
âˆš [Mid all]- -Show all the Bot(s) MID
âˆš [Respon]- -Check Response Bot
âˆš [Speed]- -Check Kecepatan Bot   
âˆš [Banlist]- -Check Banned Contact
âˆš [Gn G.Name]- -Change Group Name
âˆš [Cancel]- -Cancel Group Invitation
âˆš [Tag All]- -Tag All Member 
âˆš [View]- -View Setting
âˆš [Open]-  -Open Url
âˆš [Close]- -Close Url
âˆš [Stafflist]
âˆš [Set]    

â† KICKERâ†ž
**Protect / Damage Your Group**
âˆš [Banned @] Bann Target
âˆš [Unban @]   Unbann Target
âˆš [Kill @]   Kick Target Bann
âˆš [Nk @]    Kick Target User
âˆš [All]  Invite Semua Bot
âˆš [Mayhem] Do not use in d'group
ã€Œ Edited By ã€
https://line.me/R/ti/p/%40kyx3655e
"""

Setgroup =""" **Bot Protection Key**
âˆš [AllProtection]~[AllProtection on / off]
âˆš [Protect QR]~[Qr on / off]
âˆš [Mid Check]~[Contact On / Off]
âˆš [Reject Invite]~[Guest On / Off]
âˆš [Protect Cancel]~[Proc on / off]
âˆš [Member Protect]~[MProtection on / off]
"""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = ki2.getProfile().mid
Cmid = ki3.getProfile().mid
Dmid = ki4.getProfile().mid
Emid = ki5.getProfile().mid
Fmid = ki6.getProfile().mid
Gmid = ki7.getProfile().mid
Hmid = ki8.getProfile().mid
Imid = ki9.getProfile().mid
Jmid = ki10.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,"u30ef8888fc6633edaef95fe68c686c48","ue78b84e555c7640671975690b6df2712"]
admin = ["u30ef8888fc6633edaef95fe68c686c48","ue78b84e555c7640671975690b6df2712"]
staff = ["ue78b84e555c7640671975690b6df2712"]
adminMID = ["u30ef8888fc6633edaef95fe68c686c48","ue78b84e555c7640671975690b6df2712"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"кι∂у αη∂ιк αмкєρ",
    "cName2":"🄼🄴🅁🅁🅈" , 
    "cName3":"нєяℓιиα",
    "cName4":"ᏒᎪᎥsᎪ",
    "cName5":"ツᎪzᎥzᎪhツ",
    "cName6":"cαηтιкα",
    "cName7":"pυтrι",
    "cName8":"кαѕιн",
    "cName9":"ᏒᎥsmᎪ",
    "cName10":"ᏒᎥᏒᎥ",
    "cName11":"үαηтι",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":True,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True,
    "MProtection":False,
    "AllProtection":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        #-------Protect Qr-------#
        if op.type == 11:
            if wait["ProtectQR"] == True:
                if op.param2 not in Bots or staff:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    cl.updateGroup(G)
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
                        
        #------Finish------#
        # -INV KICK- #
        if op.type == 13:
            if wait["Protectguest"] == True:
                if op.param2 in Bots or staff:
                	pass
                else:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
        #------FINISH------#
        
        if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ks.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass

		if op.type == 19:
		    if op.param2 not in Bots:
			if op.param2 in Bots:
			    pass
			elif wait["protect"] == True:
			    wait ["blacklist"][op.param2] = True
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			else:
			    cl.sendText(op.param1,"")
		    else:
			cl.sendText(op.param1,"")
			
		if op.type == 13:
		    if op.param2 not in Bots:
			if op.param2 in Bots:
			    pass
			elif wait["inviteprotect"] == True:
			    wait ["blacklist"][op.param2] = True
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			else:
			    cl.sendText(op.param1,"")
		    else:
			cl.sendText(op.param1,"")
		    if op.param2 not in Bots:
			if op.param2 in Bots:
			    pass
			elif wait["inviteprotect"] == True:
			    wait ["blacklist"][op.param2] = True
			    cl.cancelGroupInvitation(op.param1,[op.param3])
			else:
			    cl.sendText(op.param1,"")
		    else:
			cl.sendText(op.param1,"")
		    if op.param2 not in Bots:
			if op.param2 in Bots:
			    pass
			elif wait["cancelprotect"] == True:
			    wait ["blacklist"][op.param2] = True
			    cl.cancelGroupInvitation(op.param1,[op.param3])
			else:
			    cl.sendText(op.param1,"")
		    else:
			cl.sendText(op.param1,"")

		if op.type == 11:
		    if op.param2 not in Bots:
			if op.param2 in Bots:
			    pass
			elif wait["linkprotect"] == True:
			    wait ["blacklist"][op.param2] = True
			    G = ki.getGroup(op.param1)
			    G.preventJoinByTicket = True
			    ki.updateGroup(G)
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			else:
			    cl.sendText(op.param1,"")
		    else:
			cl.sendText(op.param1,"")
	        if op.type == 5:
	            if wait["autoAdd"] == True:
	                if (wait["message"] in [""," ","\n",None]):
	                    pass
	                else:
	                    cl.sendText(op.param1,str(wait["message"]))

        #--CANCEL KICK--#
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 not in Bots or staff:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
            #------FINISH------#
        if op.type == 15:
            random.choice(KAC).sendText(op.param1, cl.getContact(op.param2).displayName + " Good Bye\n(*Â´ï½¥Ï‰ï½¥*)")
            print op.param3 + "has left the group"
        
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    
            if op.param3 in Dmid:
                if op.param2 in Emid:
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)

            if op.param3 in Emid:
                if op.param2 in Fmid:
                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    
            if op.param3 in Fmid:
                if op.param2 in Gmid:
                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki7.updateGroup(X)
                    Ti = ki7.reissueGroupTicket(op.param1)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    
            if op.param3 in Gmid:
                if op.param2 in Hmid:
                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki8.updateGroup(X)
                    Ti = ki8.reissueGroupTicket(op.param1)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki7.updateGroup(X)
                    Ti = ki7.reissueGroupTicket(op.param1)
                    
            if op.param3 in Hmid:
                if op.param2 in Imid:
                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki9.updateGroup(X)
                    Ti = ki9.reissueGroupTicket(op.param1)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki8.updateGroup(X)
                    Ti = k8.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in Jmid:
                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki10.updateGroup(X)
                    Ti = ki10.reissueGroupTicket(op.param1)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki9.updateGroup(X)
                    Ti = ki9.reissueGroupTicket(op.param1)
                    
            if op.param3 in Jmid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki10.updateGroup(X)
                    Ti = ki10.reissueGroupTicket(op.param1)
                    
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.knviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the groupã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True
			
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ti = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True
                        
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki4.updateGroup(G)
                    Ticket = ki4.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki5.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki5.updateGroup(G)
                    Ticket = ki5.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki6.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki6.updateGroup(G)
                    Ticket = ki6.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki7.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki7.updateGroup(G)
                    Ticket = ki7.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki8.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki8.updateGroup(G)
                    Ticket = ki8.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Imid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki9.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki9.updateGroup(G)
                    Ticket = ki9.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãŒè¹´ã‚Šè¦åˆ¶orã‚°ãƒ«ãƒ¼ãƒ—ã«å­˜åœ¨ã—ãªã„ç‚ºã€\n["+op.param1+"]\nã®\n["+op.param2+"]\nã‚’è¹´ã‚‹äº‹ãŒã§ãã¾ã›ã‚“ã§ã—ãŸã€‚\nãƒ–ãƒ©ãƒƒã‚¯ãƒªã‚¹ãƒˆã«è¿½åŠ ã—ã¾ã™ã€‚")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki10.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki10.updateGroup(G)
                    Ticket = ki10.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                       
        if op.type == 19:
                if op.param3 in Bots:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 not in Bots and staff:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19:
		    if op.param3 in admin:
		        cl.kickoutFromGroup(op.param1,[op.param2])
		        cl.inviteIntoGroup(op.param1,[op.param3])
		    else:
		        pass
		
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ki.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ki.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        ki.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ki.sendText(msg.to,"already")
                        #ki.sendText(msg.to,"already")
                        #kk.sendText(msg.to,"already")
                        #kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ki.sendText(msg.to,"aded")
                        #ki.sendText(msg.to,"aded")
                        #kk.sendText(msg.to,"aded")
                        #kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        #wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        ki.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLÃ¢â€ â€™\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Set"]:
                if msg.from_ in Bots or staff:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,Setgroup)
                    else:
                        cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
            	if msg.from_ in Bots and staff:
                    midd = msg.text.replace("Kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "1 kick " in msg.text:
                midd = msg.text.replace("1 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "2 kick " in msg.text:
                midd = msg.text.replace("2 kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif "3 kick " in msg.text:
                midd = msg.text.replace("3 kick ","")
                ki3.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
            	if msg.from_ in Bots or staff:
                    midd = msg.text.replace("Invite ","")
                    ki.findAndAddContactsByMid(midd)
                    ki.inviteIntoGroup(msg.to,[midd])
            elif "1 invite " in msg.text:
                midd = msg.text.replace("Cv1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "2 invite " in msg.text:
                midd = msg.text.replace("Cv2 invite ","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif "3 invite " in msg.text:
                midd = msg.text.replace("Cv3 invite ","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)
            elif msg.text in ["3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                ki3.sendMessage(msg)
            elif msg.text in ["4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ki4.sendMessage(msg)
            elif msg.text in ["5"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ki5.sendMessage(msg)
            elif msg.text in ["6"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                ki6.sendMessage(msg)
            elif msg.text in ["7"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ki7.sendMessage(msg)
            elif msg.text in ["8"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ki8.sendMessage(msg)
            elif msg.text in ["9"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ki9.sendMessage(msg)
            elif msg.text in ["10"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                ki10.sendMessage(msg)
                
            elif msg.text in ["Bot"]:
            	msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                ki3.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ki4.sendMessage(msg)
            
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ki5.sendMessage(msg)
            
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                ki6.sendMessage(msg)
            
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ki7.sendMessage(msg)
            
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ki8.sendMessage(msg)
            
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ki9.sendMessage(msg)
            
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                ki10.sendMessage(msg)
                
            elif msg.text in ["Ã¦â€žâ€ºÃ£ÂÂ®Ã£Æ’â€”Ã£Æ’Â¬Ã£â€šÂ¼Ã£Æ’Â³Ã£Æ’Ë†","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
     #-----Fungsi List Group------#   
            elif msg.text in ["List group"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[~]%s\n" % (cl.getGroup(i).name   +str (len (cl.getGroup(i).members)))
                    cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))
      #-----Finish--------#
      #-------------Fungsi Creator Start-----------------# 
            elif msg.text in ["Creator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    Creatorbot = "u30ef8888fc6633edaef95fe68c686c48"
                    try:
                        msg.contentMetadata = {'mid': Creatorbot}
                        
                    except:
                        Creatorbot = "Error"
                    cl.sendText(msg.to, "My Creator : ѕρє¢ιαℓ αиιмє http://line.me/ti/p/~kamu-jelek-banget")
                    cl.sendMessage(msg)
        #-------------Fungsi Creator Finish-----------------# 
        #-------------Fungsi Kick By Tag---------------------#
            elif ("Bye " in msg.text):
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            random.choice(KAC).sendText(op.param1, cl.getContact(op.param3).displayName + " ~Sorry  (*Â´ï½¥Ï‰ï½¥*)")
                        except:
                            pass
        #-------------Fungsi Kick By Tag---------------------#
        #-------------Fungsi Ban By Tag---------------------#  
            elif ("BL " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Blacklist")
                   except:
                      pass
        #-------------Fungsi Ban By Tag Finish---------------------#         
            elif msg.text in ["cancel","Cancel"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            ki.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                ki.sendText(msg.to,"No one is inviting")
                            else:
                                ki.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open","Link on"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done")
                        else:
                            ki.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1 open","Cv1 link on"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            
            elif msg.text in ["Close","Link off"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done")
                        else:
                            ki.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1 close","Cv1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ki.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ki.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid all" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                ki2.sendText(msg.to,Bmid)
                ki3.sendText(msg.to,Cmid)
                ki4.sendText(msg.to,Dmid)
                ki5.sendText(msg.to,Emid)
                ki6.sendText(msg.to,Fmid)
                ki7.sendText(msg.to,Gmid)
                ki8.sendText(msg.to,Hmid)
                ki9.sendText(msg.to,Imid)
                ki10.sendText(msg.to,Jmid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "MeUp n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("MeUp n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"name " + string + "Done")
            elif "1Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("1Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"name " + string + "Done")
            elif "2Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("2Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki2.updateProfile(profile)
                        ki2.sendText(msg.to,"name" + string + "Done")
            elif "3Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("3Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki3.updateProfile(profile)
                        ki3.sendText(msg.to,"name" + string + "Done")
            elif "4Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("4Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki4.updateProfile(profile)
                        ki4.sendText(msg.to,"name" + string + "Done")
            elif "5Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("5Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki5.updateProfile(profile)
                        ki5.sendText(msg.to,"name" + string + "Done")
            elif "6Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("6Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki6.updateProfile(profile)
                        ki6.sendText(msg.to,"name" + string + "Done")
            elif "7Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("7Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki7.updateProfile(profile)
                        ki7.sendText(msg.to,"name" + string + "Done")
            elif "8Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("8Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki8.updateProfile(profile)
                        ki8.sendText(msg.to,"name" + string + "Done")
            elif "9Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("9Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki9updateProfile(profile)
                        ki9.sendText(msg.to,"name " + string + "Done")
            elif "10Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("10Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki10.updateProfile(profile)
                        ki10.sendText(msg.to,"name " + string + "Done")
                    
            elif "AllUp n " in msg.text:
                string = msg.text.replace("AllUp n ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki2.updateProfile(profile)
                    ki3.updateProfile(profile)
                    ki4.updateProfile(profile)
                    ki5.updateProfile(profile)
                    ki6.updateProfile(profile)
                    ki7.updateProfile(profile)
                    ki8.updateProfile(profile)
                    ki9.updateProfile(profile)
                    ki10.updateProfile(profile)
                    ki.sendText(msg.to,"name" + string + "Done")
                    ki2.sendText(msg.to,"name" + string + "Done")
                    ki3.sendText(msg.to,"name" + string + "Done")
                    ki4.sendText(msg.to,"name" + string + "Done")
                    ki5.sendText(msg.to,"name" + string + "Done")
                    ki6.sendText(msg.to,"name" + string + "Done")
                    ki7.sendText(msg.to,"name" + string + "Done")
                    ki8.sendText(msg.to,"name" + string + "Done")
                    ki9.sendText(msg.to,"name" + string + "Done")
                    ki10.sendText(msg.to,"name" + string + "Done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            #---------------#
            elif msg.text in ["AllProtection on"]:
            	if msg.from_ in Bots or staff:
            	    if wait["AllProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        wait["Protectguest"] = True
                        wait["ProtectQR"] = True
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")                        
            elif msg.text in ["AllProtection off"]:
            	if msg.from_ in Bots or staff:
            	    if wait["AllProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        wait["Protectguest"] = False
                        wait["ProtectQR"] = False
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["MProtection on"]:
                if msg.from_ in Bots or staff:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["MProtection off"]:
                if msg.from_ in Bots or staff:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done") 
            elif msg.text in ["Blockinvite on","guest on"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Block Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Block Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Blockinvite off","guest off"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Blockinvitation Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Blockinvitation Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Qrp on","qr on"]:
                if msg.from_ in Bots or staff:
                    if wait["ProtectQR"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["ProtectQR"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Qrp off","qr off"]:
                if msg.from_ in Bots or staff:
                    if wait["ProtectQR"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["ProtectQR"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proc on","proc on"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Proc off","proc off"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â€¦Ë†:Ã£â€šÂªÃ£Æ’Â³","K on","Contact on","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€“â€¹"]:
            	if msg.from_ in admin or staff:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â‚¬Â£Ã§ÂµÂ¡Ã¥â€¦Ë†:Ã£â€šÂªÃ£Æ’â€¢","K off","Contact off","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©â€”Å“"]:
            	if msg.from_ in admin or staff:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done ")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¥Ââ€šÃ¥Å  :Ã£â€šÂªÃ£Æ’Â³","Join on","Auto join:on","Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¥ÂÆ’Ã¥Å  Ã¯Â¼Å¡Ã©â€“â€¹"]:
            	if msg.from_ in admin or staff:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¥Ââ€šÃ¥Å  :Ã£â€šÂªÃ£Æ’â€¢","Join off","Auto join:off","Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¥ÂÆ’Ã¥Å  Ã¯Â¼Å¡Ã©â€”Å“"]:
            	if msg.from_ in admin or staff:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"Ã¥â€¦Â³Ã¤Âºâ€ Ã©â€šâ‚¬Ã¨Â¯Â·Ã¦â€¹â€™Ã§Â»ÂÃ£â‚¬â€šÃ¨Â¦ÂÃ¦â€”Â¶Ã¥Â¼â‚¬Ã¨Â¯Â·Ã¦Å’â€¡Ã¥Â®Å¡Ã¤ÂºÂºÃ¦â€¢Â°Ã¥Ââ€˜Ã©â‚¬Â")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "Ã¤Â½Â¿Ã¤ÂºÂºÃ¤Â»Â¥Ã¤Â¸â€¹Ã§Å¡â€žÃ¥Â°ÂÃ§Â»â€žÃ§â€Â¨Ã¨â€¡ÂªÃ¥Å Â¨Ã©â€šâ‚¬Ã¨Â¯Â·Ã¦â€¹â€™Ã§Â»Â")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â€¹â€¢Ã©â‚¬â‚¬Ã¥â€¡Âº:Ã£â€šÂªÃ£Æ’Â³","Leave on","Auto leave:on","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â€¹â€¢Ã©â‚¬â‚¬Ã¥â€¡ÂºÃ¯Â¼Å¡Ã©â€“â€¹"]:
            	if msg.from_ in admin or staff:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â€š")
            elif msg.text in ["Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â€¹â€¢Ã©â‚¬â‚¬Ã¥â€¡Âº:Ã£â€šÂªÃ£Æ’â€¢","Leave off","Auto leave:off","Ã¥Â¼Â·Ã¥Ë†Â¶Ã¨â€¡ÂªÃ¥â€¹â€¢Ã©â‚¬â‚¬Ã¥â€¡ÂºÃ¯Â¼Å¡Ã©â€”Å“"]:
            	if msg.from_ in admin or staff:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å“â€°:Ã£â€šÂªÃ£Æ’Â³","Share on","Share on"]:
            	if msg.from_ in admin or staff:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â€š")
            elif msg.text in ["Ã¥â€¦Â±Ã¦Å“â€°:Ã£â€šÂªÃ£Æ’â€¢","Share off","Share off"]:
            	if msg.from_ in admin or staff:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â€¦Â³Ã¦â€“Â­Ã£â‚¬â€š")
            elif msg.text in ["View"]:
                md = ""
                if wait["MProtection"] == True: md+=" MProtection : on\n"
                else: md+=" MProtection  : off\n"
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect Qr      : on\n"
                else: md+=" Protect Qr   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                else:md+=" Auto Join Group by Ticket : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â€ Å’Ã¦Â²Â¡Ã¥Å“Â¨Ã£â‚¬â€š")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â€žÃ§â€ºÂ¸Ã¥â€ Å’"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
                    
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"Ã§â€ºÂ¸Ã¥â€ Å’Ã¦Â²Â¡Ã¥Å“Â¨Ã£â‚¬â€š")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "Ã¤Â»Â¥Ã¤Â¸â€¹Ã¦ËœÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡â€žÃ§â€ºÂ¸Ã¥â€ Å’"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "Ã¥Ë† Ã©â„¢Â¤Ã¤Âºâ€ Ã¤Âºâ€¹Ã§Å¡â€žÃ§â€ºÂ¸Ã¥â€ Å’Ã£â‚¬â€š")
            elif msg.text in ["Group id","Ã§Â¾Â¤Ã§Âµâ€žÃ¥â€¦Â¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
                
            elif msg.text in ["Cancelall"]:
            	if msg.from_ in admin or staff:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All invitations have been refused")
                    else:
                        cl.sendText(msg.to,"Ã¦â€¹â€™Ã§Â»ÂÃ¤Âºâ€ Ã¥â€¦Â¨Ã©Æ’Â¨Ã§Å¡â€žÃ©â€šâ‚¬Ã¨Â¯Â·Ã£â‚¬â€š")
            elif "album removeÃ¢â€ â€™" in msg.text:
                gid = msg.text.replace("album removeÃ¢â€ â€™","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "Ã¥Ë† Ã©â„¢Â¤Ã¤Âºâ€ Ã¤Âºâ€¹Ã§Å¡â€žÃ§â€ºÂ¸Ã¥â€ Å’Ã£â‚¬â€š")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¨Â¿Â½Ã¥Å  :Ã£â€šÂªÃ£Æ’Â³","Add on","Auto add:on","Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¨Â¿Â½Ã¥Å  Ã¯Â¼Å¡Ã©â€“â€¹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â€š")
            elif msg.text in ["Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¨Â¿Â½Ã¥Å  :Ã£â€šÂªÃ£Æ’â€¢","Add off","Auto add:off","Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¨Â¿Â½Ã¥Å  Ã¯Â¼Å¡Ã©â€”Å“"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â€¦Â³Ã¦â€“Â­Ã£â‚¬â€š")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneÃ£â‚¬â€š")
            elif msg.text in ["Message","Ã¨â€¡ÂªÃ¥â€¹â€¢Ã¨Â¿Â½Ã¥Å  Ã¥â€¢ÂÃ¥â‚¬â„¢Ã¨ÂªÅ¾Ã§Â¢ÂºÃ¨ÂªÂ"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsÃ£â‚¬â€š\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Ã£â€šÂ³Ã£Æ’Â¡Ã£Æ’Â³Ã£Æ’Ë†:Ã£â€šÂªÃ£Æ’Â³","Comment on","Comment:on","Ã¨â€¡ÂªÃ¥â€¹â€¢Ã©Â¦â€“Ã© ÂÃ§â€¢â„¢Ã¨Â¨â‚¬Ã¯Â¼Å¡Ã©â€“â€¹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â€š")
            elif msg.text in ["Ã£â€šÂ³Ã£Æ’Â¡Ã£Æ’Â³Ã£Æ’Ë†:Ã£â€šÂªÃ£Æ’â€¢","Comment on","Comment off","Ã¨â€¡ÂªÃ¥â€¹â€¢Ã©Â¦â€“Ã© ÂÃ§â€¢â„¢Ã¨Â¨â‚¬Ã¯Â¼Å¡Ã©â€”Å“"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â€¦Â³Ã¦â€“Â­Ã£â‚¬â€š")
            elif msg.text in ["Comment","Ã§â€¢â„¢Ã¨Â¨â‚¬Ã§Â¢ÂºÃ¨ÂªÂ"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "$set":
                    cl.sendText(msg.to, "Check sider")
                    ki.sendText(msg.to, "Check sider")
                    kk.sendText(msg.to, "Check sider")
                    kc.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal â™ª\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\nã€Œsetã€you can send â™ª read point will be created â™ª")
#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["Join","one","One"]:
                if msg.from_ in admin or Bots:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
                        
            elif msg.text in ["Kuy"]:
                if msg.from_ in  Bots or staff:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

#-----------------------------------------------
            elif msg.text in ["Bye yank"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            ki2.leaveGroup(msg.to)
                            ki3.leaveGroup(msg.to)                        
			    ki4.leaveGroup(msg.to)
			    ki5.leaveGroup(msg.to)
                            ki6.leaveGroup(msg.to)
                            ki7.leaveGroup(msg.to)                        
			    ki8.leaveGroup(msg.to)
			    ki9.leaveGroup(msg.to)
			    ki10.leaveGroup(msg.to)
			    cl.leaveGroup(msg.to)
                        except:
                            pass
#-----------------------------------------------
            elif msg.text in ["Bye"]:
                if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            ki2.leaveGroup(msg.to)
                            ki3.leaveGroup(msg.to)                        
			    ki4.leaveGroup(msg.to)
			    ki5.leaveGroup(msg.to)
                            ki6.leaveGroup(msg.to)
                            ki7.leaveGroup(msg.to)                        
			    ki8.leaveGroup(msg.to)
			    ki9.leaveGroup(msg.to)
			    ki10.leaveGroup(msg.to)
                        except:
                            pass
#-----------------------------------------------
#-------------Fungsi Tagall User Start---------------#  
            elif msg.text in ["tagall","Tag all"]:
                group = cl.getGroup(msg.to)
                jw = [contact.mid for contact in group.members]
                cb = ""
	        cb2 = ""
                strt = int(0)
                akh = int(0)
                for rs in jw:
                    xname = cl.getContact(rs).displayName
                    xlen = int(len('x')+1)
                    akh = akh + xlen
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(rs)+"},"""
                    strt = strt + int(len('x')+3)
		    akh = akh + 2
		    cb2 += "@x \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------
            elif msg.text in ["Kill"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"Sorry!!")
                            ki2.sendText(msg.to,"ï¼ˆÂ´ãƒ»Ï‰ãƒ»ï½€)")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
      
#---------------kickall started----------------#                   
            elif "Mayhem" in msg.text:
              if msg.from_ in Bots or staff:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    #gs = ki4.getGroup(msg.to)
                    #gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"ã€Œ Mayhem ã€\nMayhem is STARTINGâ™ª\n abort to abortâ™ª")
                    ki2.sendText(msg.to,"ã€Œ Mayhem ã€\n46 victims shall yell hulÂ·laÂ·baÂ·looâ™ª\nhÉ™lÉ™bÉ™ËˆloÍžo hÉ™lÉ™bÉ™ËŒloÍžo")
                    ki3.sendText(msg.to,"Good Bye (*Â´ï½¥Ï‰ï½¥*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki2.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if target not in Bots and staff:
                                try:
                                   klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki3.sendText(msg.to,"Mayhem done")
#----------------kickall finish----------------------#
                                   
            elif "Kickuk" in msg.text:
                if msg.from_ in admin or staff:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Kickuk","")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        #ki.sendText(msg.to,"Just some casual cleansing Ã´")
                        #ki2.sendText(msg.to,"Terima Kasih kak uda undang dd di grup ini")
                        #ki3.sendText(msg.to,"Terima Kasih")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            ki2.sendText(msg.to,"Not found.")
                            ki3.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                            	if target not in Bots and admin:
                                    try:
                                        klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        ki.sendText(msg.to,"Add IG Kami https://instagram.com/spesial_anime07")
                                        ki2.sendText(msg.to,"Add IG Kami https://instagram.com/spesial_anime07")
                                        ki3.sendText(msg.to,"Add IG Kami https://instagram.com/spesial_anime07")
                                   
            elif "Nk " in msg.text:
                  if msg.from_ in Bots or staff:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Sorry...")
                                    ki3.sendText(msg.to,"ï¼ˆÂ´ãƒ»Ï‰ãƒ»ï½€)")
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes ")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Banned @" in msg.text:
                if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        print "[Banned] Sukses"
                        _name = msg.text.replace("Banned @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Dilarang Banned Bot")
                            #ki.sendText(msg.to,"Dilarang Banned Bot")
                            #ki2.sendText(msg.to,"Dilarang Banned Bot")
                            #ki3.sendText(msg.to,"Dilarang Banned Bot")                        
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Akun telah sukses di banned")
                                except:
                                    ki.sendText(msg.to,"Error")
          
            elif "Unbanned @" in msg.text:
                if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        print "[Unban] Sukses"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Tidak Ditemukan.....")
                            #ki.sendText(msg.to,"Tidak Ditemukan.....")
                            #ki2sendText(msg.to,"Tidak Ditemukan.....")
                            #ki3.sendText(msg.to,"Tidak Ditemukan.....")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Akun Bersih Kembali")
                                except:
                                    ki.sendText(msg.to,"Error")
#-----------------------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"Ok  ô€¨ô€„»double thumbs upô¿¿")
                ki2.sendText(msg.to,"Ok  ô€¨ô€„»double thumbs upô¿¿")
                ki3.sendText(msg.to,"Ok  ô€¨ô€„»double thumbs upô¿¿")
#-----------------------------------------------
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Hai"]:
                ki.sendText(msg.to,"Hi Juga yank")
                ki2.sendText(msg.to,"Hallo sayang")
                ki3.sendText(msg.to,"Iya yank")

#-----------------------------------------------

            elif msg.text in ["Bobok yuk"]:
                ki.sendText(msg.to,"Sama aku ya bobok nya")
                ki2.sendText(msg.to,"Iya yuk yank uda anu nih")
                ki3.sendText(msg.to,"Sini beb")
            
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            
#-----------------------------------------------
            elif msg.text in ["Respon","respon"]:
                ki.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»`ï¼‰")
                ki2.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki3.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki4.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki5.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki6.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki7.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki8.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki9.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
                ki10.sendText(msg.to,"ï¼ˆ`ãƒ»Ï‰ãƒ»ï½€ï¼‰")
#-----------------------------------------------
            
            elif "Spam " in msg.text:
              if msg.from_ in Bots or staff:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 60:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 100:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
                        
            elif msg.text in ["Speed","Speedbot","speedbot"]:
            	if msg.from_ in Bots or staff:
                    start = time.time()
                    cl.sendText(msg.to, "Waiting...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    
            elif "Add staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Add admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin add executing"
                    _name = msg.text.replace("Add admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin remove executing"
                    _name = msg.text.replace("Remove admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the admin list")
                            except:
                                pass
                    print "[Command]admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
            
            elif msg.text in ["Admin list","admin list"]:
                if admin == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Admin list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"
                    
            elif msg.text in ["Ip Like", "Ar like"]:
                if msg.from_ in staff:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    try:
                        likePost()
                    except:
                        pass

#------------------------------------------------------------------
            elif msg.text in ["Banned"]:
            	if msg.from_ in admin or staff:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unbanned"]:
            	if msg.from_ in admin or staff:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
                    
        #---------Fungsi Banlist With Tag--------#
            elif msg.text in ["Banlist","ip banlist"]:
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"No user is Blacklisted")
                else:
                    ki.sendText(msg.to,"Blacklisted user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ki.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
        #---------Fungsi Banlist With Tag Finish--------#
        
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill"]:
            	if msg.from_ in admin or staff:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                        #ki2.sendText(msg.to,"There was no blacklist user")
                        #ki3.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ki.cancelGroupInvitation(msg.to,[_mid])
                    ki.sendText(msg.to,"I pretended to cancel and canceled.")
            
            elif "albumÃ¢â€ â€™" in msg.text:
                try:
                    albumtags = msg.text.replace("albumÃ¢â€ â€™","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecÃ¢â€ â€™" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecÃ¢â€ â€™","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
                        
            elif "midb:" in msg.text:
                midd = msg.text.replace("midb:","")
                wait["blacklist"][midd] = True
            
            elif "#çµ‚äº†" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
                    
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    for zx in range(0,20):
        hasil = cl.activity(limit=200)
    if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try: 
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki7.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki7.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki8.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki8.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki9.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki9.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            ki10.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002
            ki10.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by: ѕρє¢ιαℓ αиιмє https://line.me/R/ti/p/%40kyx3655e")
            print "Like"
        except:
            pass
    else:
        print "Already Liked"
        time.sleep(500)
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
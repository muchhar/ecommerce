from django.shortcuts import render,redirect,get_object_or_404
from random import seed
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from random import randint
import requests
import json
from .models import users,product,order,comment as ucom,rating
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect,csrf_exempt
def logout(request):
	try:
		del request.session['u_num']
	except:
		pass
	try:
		del request.session['u_pass']
	except:
		pass
	try:
		del request.session['u_login']
	except:
		pass
	try:
		del request.session['u_rand']
	except:
		pass
	return redirect('/')
def index(request):
	
	try:
		del request.session['up_pass']
		
	except:
		pass
	try:
		del request.session['a_creating']
	except:
		pass
	##############################for delete#######################
	try:
		
		del request.session['qon']
	except:
		pass
	try:
		del request.session['pid']
		
	except:
		pass
	try:
		del request.session['u_rand']
	except:
		pass
	
	#############################################
	b=[]
	c=[]
	d=[]
	a=[]
	k=0
	if request.method=="POST":
		fil=request.POST.get('search')
		log2=product.objects.filter(pname__icontains=fil)
		k=log2
		
	else:
		log2=product.objects.all()
	
		
		for i in range(0,4):
			a.append(log2[len(log2)-1-i])
		for i in range(0,4):
			b.append(log2[len(log2)-5-i])
		for i in range(0,4):
			c.append(log2[len(log2)-9-i])
		for i in range(0,4):
			d.append(log2[len(log2)-11-i])

	try:
		log=users.objects.get(upass=request.session['u_pass'],unum=request.session['u_num'])

		raj="Hello "+log.uname
		try:
			tet=json.loads(log.ucart)
			bb=len(tet)
		except:
			bb="0"
		mt=''
		if len(log2)==0:
			mt="No reselt found"

			return render(request,'usersite/index.html',{'msg':raj,'bb':bb,'k':k,'mt':mt})
		if k!=0:
			
			return render(request,'usersite/index.html',{'msg':raj,'bb':bb,'k':k,'mt':mt})
		return render(request,'usersite/index.html',{'msg':raj,'product1':a,'product2':b,'product3':c,'product4':d,'bb':bb})
		
	except:
		pass
	mt=''
	if len(log2)==0:
		mt="No reselt found"
	if k!=0:
			
		return render(request,'usersite/index.html',{'k':k,'mt':mt})
	return render(request,'usersite/index.html',{'product1':a,'product2':b,'product3':c,'product4':d})
		
		

def loginu(request):
	try:
		a=request.session['u_login']
		return redirect('/')
	except:
		a=1
	if request.method=="POST":
		num=request.POST.get('p_num')
		upass1=request.POST.get('p_pass')
		try:
			log=users.objects.get(upass=upass1,unum=num)

			request.session['u_num']=log.unum
						
			request.session['u_pass']=log.upass
			request.session['u_login']=True
			
			return redirect('/')
		except:
			msg="**Wrong password or username"
			return render(request,'usersite/login.html',{'msg':msg})		
	return render(request,'usersite/login.html')
def signupu(request):
	try:
		a=request.session['u_login']
		return redirect('/')
	except:
		a=1
	
	if request.method=="POST":
		uname=request.POST.get('uname',False)
		upass=request.POST.get('upass',False)
		ugmail=request.POST.get('ugmail',False)
		unum=request.POST.get('unum',False)
		otp=request.POST.get('otp',False)
		ram=request.POST.get('rand',False)
		if otp==False:
			
		
			if unum=="" or upass=="" or uname=="":
				msg='**Fill all detaield'
				return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
			elif unum.isdigit()==False or len(unum)!=10:
				msg='**Please Enter right number'
				return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
			elif len(upass)<8:
				msg='**Password contain minimum 8 digit'
				return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
			elif ugmail!="":
				try:
					if ugmail[len(ugmail)-3]!="." and  ugmail[len(ugmail)-4]!=".":
						msg='**Please enter right email or make null'
						return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})

					else:
						try:
							onum=request.POST.get('onum')
							
							log=users.objects.get(unum=unum)
							msg='**Number alrady resistor'
							return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
							
							
							
						except:
							
							
							rand= str(randint(100000,999999))
							url = "https://www.fast2sms.com/dev/bulk"
							payload = "sender_id=FSTSMS&language=english&route=qt&numbers="+unum+"&message=23554&variables={#BB#}&variables_values="+rand
							headers = {'authorization': "API KEYS",'cache-control': "no-cache",'content-type': "application/x-www-form-urlencoded"}
							response = requests.request("POST", url, data=payload, headers=headers)
							a=response.text
							a=json.loads(a)
							

							if a['return']==False:
								msg='**OTP cant send!'
								return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
							else:
								request.session['u_name']=uname
								request.session['u_num']=unum
								request.session['u_rand']=rand
								request.session['u_pass']=upass
								request.session['u_gmail']=ugmail
								request.session['a_creating']=True
								return render(request,'usersite/otpmbs.html')
				except:
					msg='**Enter correct email'
					return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
			else:
				
				try:
					onum=request.POST.get('onum')
					
					log=users.objects.get(unum=unum)
					msg='**Number alrady resistor'
					return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
					
					
					
				except:
					
					
					rand= str(randint(100000,999999))
					url = "https://www.fast2sms.com/dev/bulk"
					payload = "sender_id=FSTSMS&language=english&route=qt&numbers="+unum+"&message=23554&variables={#BB#}&variables_values="+rand
					headers = {'authorization': "API KEYS",'cache-control': "no-cache",'content-type': "application/x-www-form-urlencoded"}
					response = requests.request("POST", url, data=payload, headers=headers)
					a=response.text
					a=json.loads(a)
					print(a['return'])

					if a['return']==False:
						msg='**OTP cant send!'
						return render(request,'usersite/create.html',{'msg':msg,'uname':uname,'unum':unum,'ugmail':ugmail})
					else:
						request.session['u_name']=uname
						request.session['u_num']=unum
						request.session['u_rand']=121211
						request.session['u_pass']=upass
						request.session['u_gmail']=ugmail
						request.session['a_creating']=True
						return render(request,'usersite/otpmbs.html')
		else:
			
			if otp==request.session['u_rand']:
				#msg="OTP Verifyed"
				del request.session['u_rand']
				c=users()
				
				c.uname=request.session['u_name']
				c.unum=request.session['u_num']
				c.ugmail=request.session['u_gmail']
				c.upass=request.session['u_pass']
				c.save()
				request.session['u_login']=True

				return redirect('/')
				
			else:
				msg="**OTP Not match"
				return render(request,'usersite/otpmbs.html',{'msg':msg})

	else:
		return render(request,'usersite/create.html')

def otpu(request):
	if request.method=="POST":
		otp=request.POST.get('otp',False)
		try:
			if otp==request.session['u_rand']:
				msg="OTP Verifyed"
				#del request.session['u_rand']
				del request.session['u_rand']
				try:
					if request.session['a_creating']==True:
						del request.session['a_creating']
						c=users()
				
						c.uname=request.session['u_name']
						c.unum=request.session['u_num']
						c.ugmail=request.session['u_gmail']
						c.upass=request.session['u_pass']
						c.save()
						request.session['u_login']=True

					return redirect('/')

				except:
					request.session['up_pass']=True

					return redirect('/setpassword')

			else:
				msg="**OTP Not match"
				return render(request,'usersite/otpmbs.html',{'msg':msg})
		except:
			#msg='**Something goes wrong'
			return redirect('/')
	else:
		try:
			a=request.session['u_rand']
			#print(a)
			return render(request,'usersite/otpmbs.html')
			
		except:
			return redirect('/')

		
def sendagain1(request):
	try:
		a=request.session['u_rand']
	except:
		return redirect('/')
	if request.method=="POST":
		
		otp=request.POST.get('otp',False)
		try:
			if otp==request.session['u_rand']:
				msg="OTP Verifyed"
				del request.session['u_rand']
				c=users()
				
				c.uname=request.session['u_name']
				c.unum=request.session['u_num']
				c.ugmail=request.session['u_gmail']
				c.upass=request.session['u_pass']
				c.save()

				return render(request,'usersite/mainmbs.html',{'msg':msg})
			else:
				msg="**OTP Not match"
				return render(request,'usersite/otpmbs.html',{'msg':msg})
		except:
			return redirect('/')

		
	else:

		try:
			a=request.session['u_num']
			#return redirect('/')
		except:
			return redirect('/')
		rand= str(randint(100000,999999))
		url = "https://www.fast2sms.com/dev/bulk"
		payload = "sender_id=FSTSMS&language=english&route=qt&numbers="+request.session['u_num']+"&message=23554&variables={#BB#}&variables_values="+rand
		headers = {'authorization': "api key",'cache-control': "no-cache",'content-type': "application/x-www-form-urlencoded"}
		response = requests.request("POST", url, data=payload, headers=headers)
		a=response.text
		a=json.loads(a)
		

		if a['return']==False:
			msg='**OTP cant send!'
			return render(request,'usersite/otpmbs.html')
		else:
			
			request.session['u_rand']=rand
			
			return redirect('/otp')
			
			#return render(request,'usersite/otpmbs.html')

		

def forg(request):
	try:
		a=request.session['u_login']
		return redirect('/')
	except:
		pass
	if request.method=="POST":
		
		
		try:
			onum=request.POST.get('onum')
			
			log=users.objects.get(unum=onum)
			
			request.session['u_num']=log.unum
			rand= str(randint(100000,999999))

			url = "https://www.fast2sms.com/dev/bulk"
			payload = "sender_id=FSTSMS&language=english&route=qt&numbers="+request.session['u_num']+"&message=23554&variables={#BB#}&variables_values="+rand
			headers = {'authorization': "api key",'cache-control': "no-cache",'content-type': "application/x-www-form-urlencoded"}
			response = requests.request("POST", url, data=payload, headers=headers)
			a=response.text
			a=json.loads(a)
			print(a['return'])

			if a['return']==False:
				msg='**OTP cant send!'
				return render(request,'usersite/forgotpassmbs.html',{'msg':msg})
			else:
				
				request.session['u_rand']=rand
				
				return redirect('/otp')
			
			
			
		except:
			
			msg="**Number not regester"
			return render(request,'usersite/forgotpassmbs.html',{'msg':msg})
	
				
	return render(request,'usersite/forgotpassmbs.html')
def setpass(request):
	try:
		a=request.session['up_pass']
		
	except:
		return redirect('/')
	if request.method=="POST":
		pass1=request.POST.get('pass1',False)
		pass2=request.POST.get('pass2',False)
		try:
			if request.session['up_pass']==True:
								#del request.session['u_rand']
				
				if pass1==pass2 and len(pass1)>7:
					sel=get_object_or_404(users,unum=request.session['u_num'])
					sel.upass=pass1
		
					sel.save()
					del request.session['up_pass']
					return redirect('/login')
				else:
					msg="**Make 8 digit or nat match"
					return render(request,'usersite/setpasswordmbs.html',{'msg':msg})	
			else:
				msg="**Something Wrong"
				return render(request,'usersite/setpasswordmbs.html',{'msg':msg})
		except:
			msg='**Something goes wrong'
			return render(request,'usersite/setpasswordmbs.html',{'msg':msg})
	return render(request,'usersite/setpasswordmbs.html')
#############################################################################
def addproduct(request):
	if not request.user.is_authenticated:
		return redirect('login')
	if request.method=="POST":
		#mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="cmsbharat")
		p=product()
		p.pname=request.POST.get('pname',False)
		p.pdes=request.POST.get('pdes',False)
		p.pprice=request.POST.get('pprice',False)
		p.pq=request.POST.get('pq',False)
		p.pp1=request.POST.get('pp1',False)
		p.pp2=request.POST.get('pp2',False)
		p.pp3=request.POST.get('pp3',False)
		p.save()
		return render(request,'adminsite/Addproduct.html',{'msg':'Saved!'})
	return render(request,'adminsite/Addproduct.html')
@csrf_exempt
def rate(request):
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	if request.method=='POST':
		ide=request.POST.get('ide',False)
		rt=request.POST.get('taker')
		#print(rt)
		if rt!="0":
			#sd=users.objects.get(unum=request.session['u_num'])
			
			try:
				rat2=rating.objects.get(runum=request.session['u_num'],rpid=ide)
				rat2.rat=rt
				rat2.save()
			
			except:
				cc=rating()
				cc.runum=request.session['u_num']
				cc.rpid=ide
				cc.rat=rt
				#cc.cuname=sd.uname
				cc.save()
				
		else:
			request.session['sinfo']="**Please give rate"
			pass
	return redirect('/productv/'+ide)
@csrf_exempt
def comment(request):
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	if request.method=='POST':
		ide=request.POST.get('ide',False)
		cmt=request.POST.get('cmt')
		if cmt!="":
			sd=users.objects.get(unum=request.session['u_num'])
			cc=ucom()
			cc.cunum=request.session['u_num']
			cc.cpid=ide
			cc.cmt=cmt
			cc.cuname=sd.uname
			cc.save()
			
		else:
			request.session['cinfo']="**Please write somthing"
			pass
	return redirect('/productv/'+ide)
def productv(request,ped):
	qinfo=""
	#sinfo=''
	if request.method=="POST":
		qun=request.POST.get('qon',False)
		cmt=request.POST.get('cmt',False)
		availableq=product.objects.get(id=ped)

		if int(qun)<=0:
			#print(qun)
			#request.session['conadd']=True
			qinfo="**Enter valid item"
			print("Enter valid number")
		elif int(qun)>int(availableq.pq):
			qinfo="**Product have only "+availableq.pq+' quantity'

		else:
			
			request.session['pid']=ped
			request.session['qon']=qun
			return redirect('/conadd')
	else:
		pass
	try:
		cinfo=request.session['cinfo']
		del request.session['cinfo']
	except:
		cinfo=''
	try:
		como=ucom.objects.filter(cpid=ped)########how get two in one
	#print(como)
	except:
		como=''
	try:
		rute=rating.objects.filter(rpid=ped)
		tot=0
		for to in rute:
			tot=int(to.rat)+tot
		tot=tot/len(rute)
		tot=round(tot,1)
		ut=len(rute)
	except:
		tot=0
		ut=0
	try:
		sinfo=request.session['sinfo']
		del request.session['sinfo']
	except:
		sinfo=''
	#except:
	#	print('hello')
	#	como=[]
	pi=product.objects.get(id=ped)

	mai=pi.pp1
	return render(request,'usersite/product_detail.html',{'red1':pi,'mai':mai,'qinfo':qinfo,'cinfo':cinfo,'como':como,'sinfo':sinfo,'prat':tot,'ut':ut})
def upimg(request,mai,mai2):
	qinfo=""
	
	if request.method=="POST":
		qun=request.POST.get('qon',False)
		availableq=product.objects.get(id=mai)
		if int(qun)<=0:
			qinfo="**Enter valid item"
			print("Enter valid number")
			#print(qun)
			#request.session['conadd']=True
			
		elif int(qun)>int(availableq.pq):
			qinfo="**Product have only "+availableq.pq+' quantity'
		else:
			request.session['pid']=mai
			request.session['qon']=qun
			return redirect('/conadd')
	else:
		pass
	try:
		como=ucom.objects.filter(cpid=mai)########how get two in one
	#print(como)
	except:
		como=''
	try:
		sinfo=request.session['sinfo']
		del request.session['sinfo']
	except:
		sinfo=''
	try:
		rute=rating.objects.filter(rpid=mai)
		tot=0
		for to in rute:
			tot=int(to.rat)+tot
		tot=tot/len(rute)
		tot=round(tot,1)
		ut=len(rute)
	except:
		tot=0
		ut=0
	pi=product.objects.get(id=mai)
	if mai2=='1':
		poto=pi.pp1
	elif mai2=='2':
		poto=pi.pp2
	elif mai2=='3':
		poto=pi.pp3
	return render(request,'usersite/product_detail.html',{'red1':pi,'mai':poto,'qinfo':qinfo,'como':como,'sinfo':sinfo,'prat':tot,'ut':ut})
def addtocart(request,ped):
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	try:
		er=product.objects.get(id=ped)
		br=users.objects.get(unum=request.session['u_num'])
		try:
			ac=json.loads(br.ucart)
			ac.append(str(ped))
			
		except:
			ac=[str(ped)]
			
		finally:
			
			ac = list(dict.fromkeys(ac))
			
			a=json.dumps(ac)
			br.ucart=a
			br.save()
	except:
		return redirect('/')

	br2=users.objects.get(unum=request.session['u_num'])
	crt=json.loads(br2.ucart)
	depo=[]
	for i in crt:
		dede=product.objects.get(id=int(i))
		depo.append(dede)
	log=product.objects.all()
	log2=product.objects.all()
	b=[]
	c=[]
	d=[]
	f=[]
	
	
	for i in range(0,4):
		f.append(log2[len(log2)-1-i])
	for i in range(0,4):
		b.append(log2[len(log2)-5-i])
	for i in range(0,4):
		c.append(log2[len(log2)-9-i])
	for i in range(0,4):
		d.append(log2[len(log2)-11-i])
	return render(request,'usersite/cart.html',{'cart':depo,'product':f,'product2':b,'product3':c,'product4':d})
def remove(request,pid):

	br2=users.objects.get(unum=request.session['u_num'])
	crt=json.loads(br2.ucart)
	crt.remove(str(pid))
	#ac = list(dict.fromkeys(ac))
			
	a=json.dumps(crt)
	br2.ucart=a
	br2.save()
	log=product.objects.all()
	return redirect('/cartpage',{'product':log})
def cancel(request,pid):
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	br2=order.objects.get(id=int(pid))
	adi=br2.productid
	adq=br2.productq
	ben=product.objects.get(id=adi)
	ben.pq=str(int(ben.pq)+int(adq))
	ben.save()
	br2.status="Cancel"
	br2.save()
	return render(request,'orderc.html')
	#return redirect('/orderc')
def cartpage(request):
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	
	#br=users.objects.get(unum=request.session['u_num'])
	log=product.objects.all()	

	br2=users.objects.get(unum=request.session['u_num'])
	try:
		crt=json.loads(br2.ucart)
		depo=[]
		emt=''
		for i in crt:
			dede=product.objects.get(id=int(i))
			depo.append(dede)
		if len(crt)==0:
			emt="Your cart is empty"

	except:
		depo=[]
		emt="Your cart is empty"
	log2=product.objects.all()
	
	b=[]
	c=[]
	d=[]
	a=[]
	
	
	for i in range(0,4):
		a.append(log2[len(log2)-1-i])
	for i in range(0,4):
		b.append(log2[len(log2)-5-i])
	for i in range(0,4):
		c.append(log2[len(log2)-9-i])
	for i in range(0,4):
		d.append(log2[len(log2)-11-i])
	return render(request,'usersite/cart.html',{'cart':depo,'emt':emt,'product':log,'product':a,'product2':b,'product3':c,'product4':d})
def conadd(request):
	try:
		a= request.session['u_num']
		b=request.session['pid']
	except:
		return redirect('/login')
	add=users.objects.get(unum=request.session['u_num'])
	get=product.objects.get(id=request.session['pid'])
	tot=str(int(get.pprice)*int(request.session['qon']))

	try:
		
		
		dit={'sadd':add.uaddress,'scity':add.ucity,'zip':add.uzip,'mn':add.unum2,'tot':tot}
		msg=""
	except:
		dit={'tot':tot}
		msg=''
	if request.method=="POST":
		sadd=request.POST.get('sadd',False)
		scity=request.POST.get('scity',False)
		zipc=request.POST.get('zip',False)
		mn=request.POST.get('mn',False)
		if sadd=="" or scity=="" or zipc=="" or mn=="":
			msg="**Fill all detaill"
		elif len(zipc)<6 or zipc.isdigit()==False:
			msg="**Enter correct zipcode"
		elif len(mn)!=10 or mn.isdigit()==False:
			msg="**Please provide right number"
		else:
			
			uunum=request.session['u_num']
			br2=users.objects.get(unum=uunum)
			br2.uaddress=sadd
			br2.ucity=scity
			br2.uzip=zipc
			br2.unum2=mn
			
	
			br2.save()
			ppp=product.objects.get(id=request.session['pid'])
			ppq=request.session['qon']
			sname=ppp.pname
			spoq=ppq
			stotal=str(int(ppp.pprice)*int(spoq))
			uunumq=ppq
			uunumpid=request.session['pid']
			payc={'sname':sname,'spoq':spoq,'stotal':stotal,'unum':uunum}
			add=users.objects.get(unum=request.session['u_num'])
			dit={'sadd':add.uaddress,'scity':add.ucity,'zip':add.uzip,'mn':add.unum2}
			msg=""
			##########################payment gateway start##################################
			MERCHANT_KEY = "your key"
			key=""
			SALT = "your salt key"
			PAYU_BASE_URL = "https://secure.payu.in/_payment"
			action = ''
			posted={}
			# Merchant Key and Salt provided y the PayU.
			for i in request.POST:
				posted[i]=request.POST[i]
			hash_object = hashlib.sha256(b'randint(0,20)')
			txnid=hash_object.hexdigest()[0:20]
			hashh = ''
			posted['txnid']=txnid
			posted['uunum']=uunum
			posted['udf2']=uunum

			posted['udf3']=uunumpid
			posted['udf4']=uunumq
			hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
			posted['key']=key
			posted['furl']="http://localhost:8000/Failure/"
			posted['surl']="http://localhost:8000/Success/"
			hash_string=''
			hashVarsSeq=hashSequence.split('|')
			for i in hashVarsSeq:
				try:
					hash_string+=str(posted[i])
				except Exception:
					hash_string+=''
				hash_string+='|'
			hash_string+=SALT
			hash_string=hash_string.encode('utf-8')
			hashh=hashlib.sha512(hash_string).hexdigest().lower()
			action =PAYU_BASE_URL
			

			return render(request,'usersite/conformaddress.html',{"posted":posted,"tot":stotal,'uunum':uunum,'uunumpid':uunumpid,'uunumq':uunumq,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,'dit':dit,'payc':payc,"hash_string":hash_string,"action":"https://secure.payu.in/_payment"})
			
		return redirect('https://secure.payu.in/_payment')
			
	

	return render(request,'usersite/conformaddress.html',dit)
@csrf_protect
@csrf_exempt
def youracc(request):
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	msg2=''
	msg3=''
	if request.method=="POST":
		#mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="cmsbharat")
		#p=product()
		uname=request.POST.get('uname',False)
		ugmail=request.POST.get('ugmail',False)
		uaddress=request.POST.get('uaddress',False)
		ucity=request.POST.get('ucity',False)
		uzip=request.POST.get('uzip',False)
		unum2=request.POST.get('unum2',False)
		if uname=="":
			msg2="**name requere"
		elif ugmail!='':
			if len(ugmail)<5:
				msg2='**Please enter right email or make null'
			elif ugmail[len(ugmail)-3]!="." and  ugmail[len(ugmail)-4]!=".":
				msg2='**Please enter right email or make null'
			else:
				#save
				udata=users.objects.get(unum=a)
				udata.uname=uname
				udata.ugmail=ugmail
				udata.uaddress=uaddress
				udata.ucity=ucity
				udata.uzip=uzip
				udata.unum2=unum2
				udata.save()
				msg3='Information update!'

		else:
			udata=users.objects.get(unum=a)
			udata.uname=uname
			udata.ugmail=ugmail
			udata.uaddress=uaddress
			udata.ucity=ucity
			udata.uzip=uzip
			udata.unum2=unum2
			udata.save()
			msg3='Information update!'
			#save
		#p.pp3=request.POST.get('pp3',False)
	udata=users.objects.get(unum=a)
	return render(request,'usersite/youraccmbs.html',{'udata':udata,'msg2':msg2,'msg3':msg3})
def changepass(request):
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	msg2=''
	msg3=''
	if request.method=="POST":
		oldpa=request.POST.get('oldpa')
		newpa1=request.POST.get('newpa1')
		newpa2=request.POST.get('newpa2')
		try:
			old=users.objects.get(unum=a,upass=oldpa)
			if len(newpa1)<7:
				msg2="*Please make 8 digit password"
			elif newpa1!=newpa2:
				msg2="*Your new password not match"
			else:
				old.upass=newpa1
				old.save()
				return redirect('/youracc')
		except:
			msg2="*You enter wrong old password"
		
	return render(request,'usersite/changepasswordmbs.html',{'pain':msg2})
def yourorder(request):
	emt=""
	de=[]
	try:
		a= request.session['u_num']
	except:
		return redirect('/login')
	try:
		ad=order.objects.filter(userid=a,status='success')
		if len(ad)==0:
			emt="You have not any order"
		else:
			for i in ad:
				det=product.objects.get(id=i.productid)
				det.ketu=i.id
				de.append(det)

	except:
		ad=''
		emt="You have not any order"
	pro=product.objects.all()
	log2=product.objects.all()
	
	b=[]
	c=[]
	d=[]
	a=[]
	
	
	for i in range(0,4):
		a.append(log2[len(log2)-1-i])
	for i in range(0,4):
		b.append(log2[len(log2)-5-i])
	for i in range(0,4):
		c.append(log2[len(log2)-9-i])
	for i in range(0,4):
		d.append(log2[len(log2)-11-i])
	return render(request,'usersite/order.html',{'emt':emt,'cart':de,'product':a,'product2':b,'product3':c,'product4':d})
@csrf_protect
@csrf_exempt
def  success(request):
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	unum=request.POST.get('udf2',False)
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt="buetsmHhB4"
	unum=request.POST.get('udf2',False)
	upid=request.POST.get('udf3',False)
	uq=request.POST.get('udf4',False)
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	#hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	retHashSeq=retHashSeq.encode('utf-8')
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	print('payment state =',status)
	if status=='success':
		
		k=users.objects.get(unum=unum)
		c=order()
		c.status=status
		c.txnid=txnid
		c.amount=amount
		c.productid=upid
		c.productq=uq
		c.unum=k.unum2
		c.uname=k.uname
		c.userid=unum
		c.save()
		
		
		return render(request,'sucess.html',{"txnid":txnid,"status":status,"amount":amount})
	else:
		return render(request,'Failure.html')
@csrf_protect
@csrf_exempt
def failure(request):
	c = {}
	#print(request.session['u_num'])
	unum=request.POST.get('udf2',False)
	upid=request.POST.get('udf3',False)
	uq=request.POST.get('udf4',False)
	#print(unum,upid,uq)
	#c.update(csrf(request))
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt="buetsmHhB4"
	print(productinfo)
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	retHashSeq=retHashSeq.encode('utf-8')
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	
	return render(request,"Failure.html",c)

	

	
	

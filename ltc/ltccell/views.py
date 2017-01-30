from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection,transaction
from django.shortcuts import redirect
from datetime import datetime, date
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
def home(request):
	return render(request,'home.html')

@never_cache
def login(request):
	return render(request,'login.html')

@never_cache	
def login1(request):
	if(request.POST):
		user_id=request.POST.get("id",None)
		psw=request.POST.get("password",None)
		sql='''select * from employee where employee_id = "'''+user_id+'''" and department = "'''+psw+'''";'''
		cursor=connection.cursor()
		cursor.execute(sql)
		row=cursor.fetchone()
		if(row==None):
			return HttpResponse("Invalid Username or Password")	
		else :			
			
			sql='''select * from employee where employee_id = "'''+user_id+'''";'''
			sql2='''select count(*) from dependents where employee_id = "'''+user_id+'''" group by employee_id;'''
			sql3='''select * from dependents where employee_id = "'''+user_id+'''";'''
			#print(sql2)
			cursor1=connection.cursor()
			cursor1.execute(sql)
			row1=cursor1.fetchone()
			cursor1.execute(sql2)
			row2=cursor1.fetchall()
			if(row1==None):
				return HttpResponse("Invalid Request")	
			else :
				#return HttpResponse("hiii")
				e_id=row1[0]
				e_name=row1[1]
				e_des=row1[2]
				e_dob=row1[3]
				e_pay=row1[4]
				e_dept=row1[5]
				e_ht=row1[6]
				e_email=row1[7]
				e_add=row1[8]
				e_con=row1[9]
				e_appt=row1[10]
				if(row2==None):
					members=0
				else:
					members=row2[0][0]
					cursor1.execute(sql3)
					row3=cursor1.fetchall()
				return render(request,'logged.html',{'e_id':e_id,'e_name':e_name,'e_des':e_des,'e_dob':e_dob,'e_pay':e_pay,'e_dept':e_dept,'e_ht':e_ht,'e_email':e_email,'e_add':e_add,'e_con':e_con,'e_appt':e_appt,'members':members})	

@never_cache
def logged(request):
	return render(request,'logged.html')

@never_cache
def register1(request):
	if(request.POST):
		name=request.POST.get("r_name",None)
		e_id=request.POST.get("r_id",None)
		desig=request.POST.get("r_designation",None)
		dept=request.POST.get("r_dept",None)
		pay=request.POST.get("r_pay",None)
		ht=request.POST.get("r_hometown",None)
		dob=request.POST.get("r_dob",None)
		email=request.POST.get("r_email",None)
		add=request.POST.get("r_add",None)
		con=request.POST.get("r_contact",None)
		appt=request.POST.get("r_appt",None)
		#sql='''INSERT INTO employee VALUES("'''+e_id+'''","'''+name+'''","'''+desig+'''","'''+dob+'''","'''+pay+'''","'''+dept+'''",'''+ht+''',"'''+email+'''","'''+add+'''","'''+con+'''","'''+appt+'''");'''
		sql="INSERT INTO employee VALUES(%s,'%s','%s','%s',%s,'%s','%s','%s','%s','%s','%s')"%(e_id,name,desig,dob,pay,dept,ht,email,add,con,appt)
		#sql="INSERT INTO t VALUES('isha');"
		try:
			cursor=connection.cursor()			
			cursor.execute(sql)
			transaction.commit()
		except:
			return HttpResponse("Invalid Request")
		r_n1=request.POST.get("r_n1",None)
		r_n2=request.POST.get("r_n2",None)
		r_n3=request.POST.get("r_n3",None)
		r_n4=request.POST.get("r_n4",None)
		r_n5=request.POST.get("r_n5",None)
		r_n6=request.POST.get("r_n6",None)
		r_n7=request.POST.get("r_n7",None)
		if len(r_n1)!=0 :
			r_a1=request.POST.get("r_a1",None)
			r_r1=request.POST.get("r_r1",None)
			sql="INSERT INTO dependents (employee_id, name, age,relationship) VALUES(%s,'%s','%s','%s')"%(e_id,r_n1,r_a1,r_r1)
			try:
				cursor=connection.cursor()			
				cursor.execute(sql)
				transaction.commit()
			except:
				return HttpResponse("Invalid Request")
		if len(r_n2)!=0 :
			r_a2=request.POST.get("r_a2",None)
			r_r2=request.POST.get("r_r2",None)
			sql="INSERT INTO dependents (employee_id, name, age,relationship) VALUES(%s,'%s','%s','%s')"%(e_id,r_n2,r_a2,r_r2)
			try:
				cursor=connection.cursor()			
				cursor.execute(sql)
				transaction.commit()
			except:
				return HttpResponse("Invalid Request")
		if len(r_n3)!=0 :
			r_a3=request.POST.get("r_a3",None)
			r_r3=request.POST.get("r_r3",None)
			sql="INSERT INTO dependents (employee_id, name, age,relationship) VALUES(%s,'%s','%s','%s')"%(e_id,r_n3,r_a3,r_r3)
			try:
				cursor=connection.cursor()			
				cursor.execute(sql)
				transaction.commit()
			except:
				return HttpResponse("Invalid Request")
		if len(r_n4)!=0 :
			r_a4=request.POST.get("r_a4",None)
			r_r4=request.POST.get("r_r4",None)
			sql="INSERT INTO dependents (employee_id, name, age,relationship) VALUES(%s,'%s','%s','%s')"%(e_id,r_n4,r_a4,r_r4)
			try:
				cursor=connection.cursor()			
				cursor.execute(sql)
				transaction.commit()
			except:
				return HttpResponse("Invalid Request")
		if len(r_n5)!=0 :
			r_a5=request.POST.get("r_a5",None)
			r_r5=request.POST.get("r_r5",None)
			sql="INSERT INTO dependents (employee_id, name, age,relationship) VALUES(%s,'%s','%s','%s')"%(e_id,r_n5,r_a5,r_r5)
			try:
				cursor=connection.cursor()			
				cursor.execute(sql)
				transaction.commit()
			except:
				return HttpResponse("Invalid Request")		
		return render(request,'registered.html')
		if len(r_n6)!=0 :
			r_a6=request.POST.get("r_a6",None)
			r_r6=request.POST.get("r_r6",None)
			sql="INSERT INTO dependents (employee_id, name, age,relationship) VALUES(%s,'%s','%s','%s')"%(e_id,r_n6,r_a6,r_r6)
			try:
				cursor=connection.cursor()			
				cursor.execute(sql)
				transaction.commit()
			except:
				return HttpResponse("Invalid Request")
		if len(r_n7)!=0 :
			r_a7=request.POST.get("r_a7",None)
			r_r7=request.POST.get("r_r7",None)
			sql="INSERT INTO dependents (employee_id, name, age,relationship) VALUES(%s,'%s','%s','%s')"%(e_id,r_n7,r_a7,r_r7)
			try:
				cursor=connection.cursor()			
				cursor.execute(sql)
				transaction.commit()
			except:
				return HttpResponse("Invalid Request")
		return render(request,'registered.html')
	return HttpResponse("Invalid Request")	

@never_cache
def claim(request):
	return render(request,'claim.html')

@never_cache
def claimed(request):
	return render(request,'claimed.html')

@never_cache
def drawn(request):
	return render(request,'drawn.html')

@never_cache
def advance1(request):
	if(request.POST):
		e_id=request.POST.get("id",None)
		dept=request.POST.get("department",None)
		nature=request.POST.get("nature",None)
		block=request.POST.get("blockyear",None)
		mode=request.POST.get("mode",None)
		od=request.POST.get("onwarddate",None)
		return1=request.POST.get("returndate",None)
		nearest=request.POST.get("nearest",None)
		req=request.POST.get("req",None)
		advance=request.POST.get("advance",None)
		sql="INSERT INTO ltc_cell (employee_id, department, nature_of_ltc,block_year,mode_of_journey,date_of_onward_journey,date_of_return_journey,railway_st_airport,advance_drawn) VALUES(%s,'%s','%s','%s','%s','%s','%s','%s',%s)"%(e_id,dept,nature,block,mode,od,return1,nearest,advance)
		try:
			cursor=connection.cursor()			
			cursor.execute(sql)
			transaction.commit()
		except:
			return HttpResponse("Invalid Request")
		#sql1=
		#print(sql1)
		sql1='''select sanction_id from ltc_cell where employee_id = "'''+e_id+'''" and date_of_onward_journey = "'''+od+'''";'''		
		#cursor.execute('''SELECT sanction_id FROM ltc_cell WHERE ( employee_id = '''+e_id+''' and mode_of_journey = '''+ mode +''' and date_of_onward_journey = '''+ od +''' ''')
		cursor.execute(sql1)
		row=cursor.fetchone()
		sanctionid=row[0]
		return render(request,'drawn.html',{'sanctionid':sanctionid})		
	return HttpResponse("Invalid Request")	

@never_cache
def advance(request):
	return render(request,'advance.html')

@never_cache
def claim2(request):
	if(request.POST):
		e_id=request.POST.get("id2",None)
		ds=request.POST.get("d_station",None)
		dd=request.POST.get("d_date",None)
		dt=request.POST.get("d_hour",None)
		a_s=request.POST.get("a_station",None)
		ad=request.POST.get("a_date",None)
		at=request.POST.get("a_hour",None)
		class1=request.POST.get("class",None)
		fare=request.POST.get("fare",None)
		no=request.POST.get("train_flight_no",None)
		total=request.POST.get("claim2",None)
	        sanction=request.POST.get("sanctionletter",None)
		sql="INSERT INTO journey (employee_id, departure_station,departure_date,departure_time,arrival_station,arrival_date,arrival_time,class_of_travel,fare,flight_train_no,total_cost,sanction_id) VALUES(%s,'%s','%s','%s','%s','%s','%s','%s',%s,'%s',%s,%s)"%(e_id,ds,dd,dt,a_s,ad,at,class1,fare,no,total,sanction)
		
		try:
			cursor=connection.cursor()			
			cursor.execute(sql)
			transaction.commit()
			
		except:
			return HttpResponse("Invalid Request")
		
		sql1='''select advance_drawn from ltc_cell where sanction_id = "'''+sanction+'''";'''
			#cursor.execute('''SELECT advance_drawn FROM ltc_cell WHERE sanction_id='''+sanction+''';''')
		total=int(total)
		cursor.execute(sql1)
		row=cursor.fetchone()
		advance=row[0]
		advance=int(advance)
		refund=total-advance
		return render(request,'claimed.html' , {'refund':refund})
	
	return HttpResponse("Invalid Request")

@never_cache	
def register(request):
	return render(request,'register.html')

@never_cache
def registered(request):
	return render(request,'registered.html')

@never_cache
def adminlogin(request):
	return render(request,'adminlogin.html')

@never_cache
def adminlogged(request):
	
	return render(request,'adminlogged.html')

@never_cache
def adminlogin1(request):
	if(request.POST):
		admin_id=request.POST.get("admin_id",None)
		admin_password=request.POST.get("admin_password",None)
		if(admin_id=="isha" and admin_password=="isha"):
			context_dict={}
			cursor=connection.cursor()			
			sql1='''select employee_id , sanction_id from ltc_cell;'''
			cursor.execute(sql1)
			row=cursor.fetchall()
			#print(row)
			context_dict['advance']=row
			context_dict['count_advance']=len(row)
			sql2='''select employee_id, sanction_id from journey;'''
			cursor.execute(sql2)
			row2=cursor.fetchall()
			#print(row2)
			context_dict['claiming']=row2
			context_dict['count_claim']=len(row2)		
			return render(request,'adminlogged.html',context_dict)
		else:
			return HttpResponse("Invalid Username and Password")
	return HttpResponse("Invalid Request")

	


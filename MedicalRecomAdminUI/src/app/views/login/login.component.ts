import { Component, Input} from '@angular/core';
import {RouterModule,Routes,Router} from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CookieService } from "ngx-cookie-service";
import {SupportService } from "../base/support.service";
@Component({
  selector: 'app-dashboard',
  templateUrl: 'login.component.html'
})
export class LoginComponent{ 
adminName="";
adminPassword="";
response=JSON;
constructor(private router: Router,private httpClient: HttpClient,
private cookieService: CookieService, private user:SupportService){}
adminLogin(a:string,b:string){
	if (a=='' && b=='')
	{
	alert("enter user name and password");
	}
	else{
	if(a==''){
	alert("please enter password");
	
	}
	else{
	if(b==''){
	alert("please enter email");
	}
	else{
	this.httpClient.post('http://3.16.156.90:5000/admin-login/', {"email":this.adminName,"password":this.adminPassword}).subscribe(data => {
    this.response = data as JSON;
    console.log(this.response['response']);
    if(this.response['response']=='1'){
    this.router.navigateByUrl('/dashboard');
    if(this.cookieService.get("userid")==''){
    console.log(this.cookieService.get("userid"))
    this.cookieService.set("userid", b);}
	}
	else{
	alert("invalid password");
	}
	
    })
    
	}}
	
	
	}
}
forgetPassword(){
	this.router.navigateByUrl('/register');
}
}

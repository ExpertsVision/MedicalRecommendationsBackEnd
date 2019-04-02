import { Component } from '@angular/core';
import {RouterModule,Routes,Router} from '@angular/router';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-dashboard',
  templateUrl: 'register.component.html'
})
export class RegisterComponent {
adminName="";
adminPassword="";
response=JSON;
  constructor(private router: Router,private httpClient: HttpClient) { }
updateAccount(){
	this.httpClient.post('http://3.16.156.90:5000/update-login/', {"email":this.adminName,"password":this.adminPassword}).subscribe(data => {
    this.response = data as JSON;
    console.log(this.response);
    
    })
    if(this.response){
    this.router.navigateByUrl('/login');}
}
}

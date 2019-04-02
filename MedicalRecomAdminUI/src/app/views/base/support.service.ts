import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CookieService } from "ngx-cookie-service";
import { Inject }  from '@angular/core';
import { DOCUMENT } from '@angular/common';
import {RouterModule,Router} from '@angular/router';
import {Observable} from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class SupportService {
all_tags=JSON;
tags_list=[];
public email_id;
users_chat_list=[];
serviceval="service response working";
  constructor(private httpClient: HttpClient, private cookieService: CookieService,
  private router: Router) { 
    this.email_id=this.cookieService.get("userid");
    console.log(this.email_id);
  	if(this.email_id!=''){
  		this.router.navigateByUrl('/dashboard');
  	}
  	else{
    this.router.navigateByUrl('/login');

  	}
  }
  //showalltags(): any{
  //return this.httpClient.post('http://127.0.0.1:5000/show_alltags/',{"a":"b"});
  
  //}



}

import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Inject }  from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { OnInit } from '@angular/core';
@Component({
  templateUrl: 'cards.component.html',
  styleUrls: ['cards.component.css']
})
export class CardsComponent implements OnInit {
username="";
useremailid="";
searchusername="";
searchuseremail="";
search_result=JSON;
search_result2=JSON;
delresponse=JSON;
res="";
us1="";
uid="";
users=[];
flag=false;
search_result_user=JSON;
all_users_list=[];
deluser="";
delid="";
index:number;
savEditUser="";
savEditId="";
p:number;
edit_user_res=JSON;
public showContent: boolean;
public pageLoaded:boolean;

  constructor(private httpClient: HttpClient, @Inject(DOCUMENT) document) { setTimeout(()=>{
    this.showContent=true;
    }, 2000);
    }

  ngOnInit() {
    this.httpClient.post('http://18.214.223.82:5000/all-users/', {"showuser":1}).subscribe(data => {
  this.search_result_user = data as JSON;
  this.all_users_list.push(this.search_result_user);
  //console.log(this.all_users_list);
  
  })

    //this.showallUser();
  }

  adduser() {
    this.httpClient.post('http://18.214.223.82:5000/add-user/',{"user_name":this.username, "email_id":this.useremailid}).subscribe(data => {
    this.search_result = data as JSON;
    this.res=this.search_result['response']
    //alert(this.res);
  })
  
  this.users.push({user_name:this.username, 
  user_id:this.useremailid});
  //console.log(this.users);
    this.uid=this.useremailid;
    this.us1 =this.username;
  }

  searchuser() {
    this.flag=true;
    this.httpClient.post('http://18.214.223.82:5000/search-user/',{"user_name":this.searchusername, "email_id":this.searchuseremail}).subscribe(data => {
    this.search_result2 = data as JSON;
    //console.log(this.search_result2);
    //alert(this.search_result2['email_id']+""+this.search_result2['user_name']);
    
  })
  }

  
  resetvalueofadd(){
    (<HTMLInputElement>document.getElementById("username")).value='';
    (<HTMLInputElement>document.getElementById("email")).value='';
  }

  resetvalueofsearch(){
    (<HTMLInputElement>document.getElementById("susername")).value='';
    (<HTMLInputElement>document.getElementById("semail")).value='';
  }


//showallUser(){
 // this.pageLoaded=true;
 // this.httpClient.post('http://18.214.223.82:5000/all-users/', {"showuser":1}).subscribe(data //=> {
//  this.search_result_user = data as JSON;
 // this.all_users_list.push(this.search_result_user);
 // console.log(this.all_users_list);
  
  //})

  //}

deleteuser(val1:string, val2:string){

  this.delid=val2;
  this.deluser=val1;
  this.httpClient.post('http://18.214.223.82:5000/delete-user/',{"user_name":this.deluser, "email_id":this.delid}).subscribe(data => {
    this.delresponse = data as JSON;
    //console.log(this.delresponse);
    //alert(this.delresponse['response']);
    
  })
}

editsave(val1:string, val2:string){
  this.savEditUser=val1;
  this.savEditId=val2;
  this.httpClient.post('http://18.214.223.82:5000/edit-user/',{"user":this.savEditUser, "email":this.savEditId}).subscribe(data => {
    this.edit_user_res = data as JSON;
    //console.log(this.edit_user_res);
    //alert(this.edit_user_res['response']);
    
  })
}

}
  



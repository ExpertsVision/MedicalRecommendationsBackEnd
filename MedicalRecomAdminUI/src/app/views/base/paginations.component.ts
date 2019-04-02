import { Component, Input, ViewEncapsulation  } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { OnInit } from '@angular/core';
//import { ModalService, ModalComponent } from 'angular-5-popup';
//import { ViewChild } from '@angular/core'
//import { ModalDirective } from 'ngx-bootstrap/modal';
import {SupportService } from "./support.service";

@Component({
  templateUrl: 'paginations.component.html',
  styles: ['.pager li.btn:active { box-shadow: none; }'],
  styleUrls: ['./paginations.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class PaginationsComponent implements OnInit {
  flag=false;
  searchusername="";
  searchuseremail="";
  search_result2=JSON;
  get_conversations=JSON;
  all_conversation_list=[];
  p:number;
  index: number;
  getres=JSON;
  get_users=JSON;
  month_dail_week_users=[];
  chat_response_json=JSON;
  chat_list=[];
  viewchatflag=false;
  chating=[];
  daily_success_ans="";
  daily_users="";
  daily_rating="";
  constructor(private httpClient: HttpClient, 
  private user:SupportService) { }

  ngOnInit() {
      this.httpClient.post('http://18.214.223.82:5000/all-conversation/', {"showuser":1}).subscribe(data => {
    this.get_conversations = data as JSON;
    this.all_conversation_list.push(this.get_conversations);
    //console.log(this.all_conversation_list);
    
    })

    this.httpClient.post('http://18.214.223.82:5000/get-user-stats/', {"showuser":1}).subscribe(data => {
    this.get_users = data as JSON;
    this.month_dail_week_users.push(this.get_users);
    //console.log(this.month_dail_week_users);
    this.daily_success_ans=this.month_dail_week_users[0][1]['dailyAns'];
    //console.log(this.daily_success_ans);
    this.daily_users=this.month_dail_week_users[0][1]['dailyUser'];
    //console.log(this.daily_users);
    this.daily_rating=this.month_dail_week_users[0][1]['dailyRating'];
    //console.log(this.daily_rating);
    })
  }

  searchuser() {
    this.flag=true;
    this.httpClient.post('http://18.214.223.82:5000/search-conversation/',{"username":this.searchusername, "email":this.searchuseremail}).subscribe(data => {
    this.search_result2 = data as JSON;
    //console.log(this.search_result2);
    //alert(this.search_result2['email_id']+""+this.search_result2['user_name']);
    
    })
    }

  resetvalueofsearch(){
    (<HTMLInputElement>document.getElementById("susername")).value='';
    (<HTMLInputElement>document.getElementById("semail")).value='';
  }


  deleteConversation(val1:string, val2:string){
    
    
    this.httpClient.post('http://18.214.223.82:5000/delete-conversation/',{"username":val1, "email":val2}).subscribe(data => {
      this.getres = data as JSON;
      //console.log(this.getres);
      alert(this.getres['response']);
      
    })
  }
  daily(){
  let value=document.getElementById("dailusers");
  let title=document.getElementById("dailuser");
  title.textContent='Daily Users';
  value.textContent=this.month_dail_week_users[0][0]['dailyUser'];
  }
  weekly(){
  let value=document.getElementById("dailusers");
  let title=document.getElementById("dailuser");
  title.textContent='Weekly Users';
  value.textContent=this.month_dail_week_users[0][0]['weeklyUser'];
  }
  monthly(){
  let value=document.getElementById("dailusers");
  let title=document.getElementById("dailuser");
  title.textContent='Monthly Users';
  value.textContent=this.month_dail_week_users[0][0]['monthlyUser'];
  }

  dailyAns(){
  let value=document.getElementById("answers");
  value.textContent=this.month_dail_week_users[0][1]['dailyAns'];
  let title=document.getElementById("ans-title");
  title.textContent='Daily Success Answers';
  }
  weeklyAns(){
  let value=document.getElementById("answers");
  value.textContent=this.month_dail_week_users[0][1]['weeklyAns'];
  let title=document.getElementById("ans-title");
  title.textContent='Weekly Success Answers';
  }
  monthlyAns(){
  let value=document.getElementById("answers");
  value.textContent=this.month_dail_week_users[0][1]['monthlyAns'];
  let title=document.getElementById("ans-title");
  title.textContent='Monthly Success Answers';
  }

  dailyRating(){
  let value=document.getElementById("rating");
  value.textContent=this.month_dail_week_users[0][2]['dailyRating'];
  let title=document.getElementById("avgrating");
  title.textContent='Daily Average Rating';
  }
  weeklyRating(){
  let value=document.getElementById("rating");
  value.textContent=this.month_dail_week_users[0][2]['weeklyRating'];
  let title=document.getElementById("avgrating");
  title.textContent='Weekly Average Rating';
  }
  monthlyRating(){
  let value=document.getElementById("rating");
  value.textContent=this.month_dail_week_users[0][2]['monthlyRating'];
  let title=document.getElementById("avgrating");
  title.textContent='Monthly Average Rating';
  }
  public showContent= false;
  public showConten1= false;

  viewChat(val1:string, val2:string, model:string){
  //this.myModal.nativeElement.className = 'modal fade';
  //let colorchange=document.getElementById("proveochat");
  //let div = document.getElementById("userchat").contains(colorchange);
  //if(div){
  //console.log("yes");
  //}
    this.showContent=true;
    //let index=id;
    let mdl_id=model;
    //console.log(index);
    //let userEmail=this.all_conversation_list[0][index]['email'];
    //let userName=this.all_conversation_list[0][index]['name'];
    let userEmail=val2;
    let userName=val1;
    //console.log(userName);
    //console.log(userEmail);
    this.httpClient.post('http://18.214.223.82:5000/get-user-chat/',{"email":userEmail, "name":userName}).subscribe(data => {

      this.chat_response_json = data as JSON;
      this.chat_list.push(this.chat_response_json);
      this.user.users_chat_list=this.chat_list;
      //console.log(this.chat_list);
      //alert(this.chat_list['user']);
      this.chating=this.user.users_chat_list;
    
    
     
    })

     document.getElementById(mdl_id).style.display = "block";
     
    }
    


  closeForm(id:string) {
  let mdl_id=id;
    document.getElementById(mdl_id).style.display = "none";
    this.chat_list=[];
  }
   
review_response_json=JSON;
review_list=[];

 viewReviews(val1:string, val2:string, model:string){
    this.showConten1=true;
    //let index=id;
    let mdl_id=model;
    //console.log(index);
    //let userEmail=this.all_conversation_list[0][index]['email'];
    //let userName=this.all_conversation_list[0][index]['name'];
    let userEmail=val2;
    let userName=val1;
    //console.log(userName);
    //console.log(userEmail);
    this.httpClient.post('http://18.214.223.82:5000/get-reviews/',{"email":userEmail}).subscribe(data => {

      this.review_response_json = data as JSON;
      this.review_list.push(this.review_response_json);
      console.log(this.review_list);
     
    
     
    })
    document.getElementById(mdl_id).style.display = "block";
    //document.getElementById("modal2").style.display = "block";
    }
    closeModal2(id:string) {
    this.review_list=[];
    let mdl_id=id;
    document.getElementById(mdl_id).style.display = "none";
   
}
query='yes';

highlight(val:string) {
        console.log(val);
        if(val=='yes'|| val=='YES' || val=='Yes') {
        //document.getElementById(id.toString()).style.color="green";
        //document.getElementById("userchat").style.fontSize = "xx-large";
        
        val=val.fontcolor("green");
        val=val.fontsize(4);
        
        let span='<span color="red" font-size="20px">'+'<strong>'+val+'</strong>' + '</span>';
        return span;
        }
        if(val=='no'|| val=='No' || val=='NO'){
        val=val.fontcolor("red");
        val=val.fontsize(4);
        let span='<span color="red" font-size="20px">'+'<strong>'+val+'</strong>' + '</span>';
        return span;
        
        }
        else{
        //document.getElementById("userchat").style.background="green";
          return val;
        }
        }


}

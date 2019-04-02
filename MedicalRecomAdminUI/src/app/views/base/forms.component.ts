import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Inject }  from '@angular/core';
import { DOCUMENT } from '@angular/common';
import {SupportService } from "./support.service";
import { OnInit } from '@angular/core';

@Component({
  templateUrl: 'forms.component.html',
  styleUrls: ['forms.component.css']
})
export class FormsComponent implements OnInit{
  addhashtag="";
  addresponse="";
  search_hashtag="";
  search_result_tag=JSON;
  show_all_tags=JSON;
  all_tags_list=[];
  collection = [];
  val="";
  res1="";
  res2="";
  flag=false;
  flag2=false;
  users= [];
  deltag="";
  delresponse="";
  index:number;
  deltagres=JSON;
  isEditable:boolean;
  savEdit1="";
  savEdit2="";
  edit_tagres=JSON;
  p:number;
  constructor(private httpClient: HttpClient, @Inject(DOCUMENT) document,private user:SupportService) {
  this.val=this.user.serviceval;
 
  
  }
  ngOnInit() {
    this.showallTags();

    
  }
  
  addhashtags(){
  this.httpClient.post('http://18.214.223.82:5000/add-hashtags/',{"hashtag":this.addhashtag, "response":this.addresponse}).subscribe(data => {
  if(true){
  this.search_result_tag = data as JSON;
  this.res1=this.search_result_tag['response']
  alert(this.res1);}
  })
  }
  resethashtags(){
    (<HTMLInputElement>document.getElementById("name1")).value='';
    (<HTMLInputElement>document.getElementById("name")).value='';
  }

  searchtag(){
  this.flag=true;
  this.httpClient.post('http://18.214.223.82:5000/search-tags/',{"hashtag":this.search_hashtag}).subscribe(data => {
  this.search_result_tag = data as JSON;
  console.log(this.search_result_tag);
  this.res2=this.search_result_tag['response']
  
  })

  }

  resetsearchtag(){
  (<HTMLInputElement>document.getElementById("name2")).value='';
  }

  showallTags(){
  this.httpClient.post('http://18.214.223.82:5000/all-tags/', {"showtags":1}).subscribe(data => {
  this.search_result_tag = data as JSON;
  
  this.all_tags_list.push(this.search_result_tag);
  
 

  })
  //return this.all_tags_list;
  
  

  }

  deletetag(val:string){
  
  this.deltag=val;
  
  this.httpClient.post('http://18.214.223.82:5000/delete-tag/',{"hashtag":this.deltag, "response":this.delresponse}).subscribe(data => {
    this.deltagres = data as JSON;
    //console.log(this.deltagres);
    alert(this.deltagres['response']);
    
  })
}

editsave(val1:string, val2:string){
  this.savEdit1=val1;
  this.savEdit2=val2;
  console.log(this.savEdit1);
  console.log(this.savEdit2);
  this.httpClient.post('http://18.214.223.82:5000/edit-tag/',{"hashtag":this.savEdit2, "response":this.savEdit1}).subscribe(data => {
    this.edit_tagres = data as JSON;
    //console.log(this.edit_tagres);
    alert(this.edit_tagres['response']);
    
  })
}


  
}

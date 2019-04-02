import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { getStyle, hexToRgba } from '@coreui/coreui/dist/js/coreui-utilities';
import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';
import { HttpClient } from '@angular/common/http';
import { Chart } from 'chart.js';
import { Inject }  from '@angular/core';
import { DOCUMENT } from '@angular/common';

@Component({
  templateUrl: 'dashboard.component.html',
  styleUrls: ['dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  
  selectedCategory="";
  response1="";
  response2="";
  grade="";
  title="";
  gradeVersion:number;
  riskFactor="";
  ageRange0:number;
  ageRange1:number;
  frequency="";
  recomendation="";
  source="";
  gender="";
  all_responses_list=[];
  response_result=JSON;
  add_response_res=JSON;
  p:number;
  categories=[];
  all_categories=[];
  editCatName="";
  editPart1="";
  editPart2="";
  index:number;
  edit_response=JSON;
  getres=JSON;
  remove_dupli_cat=[];
  oldcatName="";
  oldPart1="";
  oldPart2="";
  constructor(private httpClient: HttpClient, @Inject(DOCUMENT) document) { }

  ngOnInit() {

    this.httpClient.post('http://3.16.156.90:5000/show-all-recommendations/', {"showresponses":1}).subscribe(data => {
    this.response_result = data as JSON;
    this.all_responses_list.push(this.response_result);
    //console.log(this.response_result);
    //console.log("yes it is working");
    //console.log(this.all_responses_list[0][0]['Risk Factor Information']);
    //console.log(this.all_responses_list[0][0]);
    this.categories.push(this.response_result);
    //var i;
    //for (i = 0; i < this.all_responses_list[0].length; i++) { 
    //console.log(this.all_responses_list[0][i]['Source']);
    //}
    //this.all_categories.push(this.categories[0][i]['category']);}
    //let remove_duplicates_cat=Array.from(new Set(this.all_categories))
    //console.log(this.all_categories);
    //console.log(remove_duplicates_cat);
    //this.remove_dupli_cat=remove_duplicates_cat;
  
  })
 
  }

  addresponse(){
  this.httpClient.post('http://3.16.156.90:5000/add-recomendations/', {"title":this.title,"grade":this.grade, "gradeVersion":this.gradeVersion,"ageRange0":this.ageRange0,"ageRange1":this.ageRange1,
  "riskFactor":this.riskFactor,"frequency":this.frequency,"source":this.source,
  "recomendation":this.recomendation,"gender":this.gender}).subscribe(data => {
    this.add_response_res = data as JSON;
    //alert(this.add_response_res);
    alert(this.add_response_res['response']);
    }
  
  )
  console.log(this.grade);
  console.log(this.gradeVersion);
  console.log(this.ageRange0);
  console.log(this.ageRange1);
  console.log(this.riskFactor);
  console.log(this.frequency);
  console.log(this.source);
  console.log(this.recomendation);
  
  }

  resetresponseval(){
    (<HTMLInputElement>document.getElementById("select1")).value='';
    (<HTMLInputElement>document.getElementById("text-response1")).value='';
    (<HTMLInputElement>document.getElementById("text-response2")).value='';
  }

  editSave(val1:string, val2:string, val3:string,val4:string,val5:string,val6:string,val7:string,val8:string,val9:string,val10:string,val11:string){
  
    console.log(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11);
    this.httpClient.post('http://3.16.156.90:5000/edit-recomendations/',{"ID":val1,
    "Title":val2, "Gender":val3,"Grade":val4, "GradeVersion":val5, "AgeRange0":val6,"AgeRange1":val7,"Frequency":val8,"Risk":val9,"Source":val10, "Recomendation":val11}).subscribe(data => {
      this.edit_response = data as JSON;
      //console.log(this.edit_response);
      alert(this.edit_response['response']);
      })
  }
delCatName="";
delPart1="";
delPart2="";
  deleteResponse(val1:string){
    console.log(typeof(val1.toString()));
    this.delCatName=val1;
    this.httpClient.post('http://3.16.156.90:5000/delete-recomendations/',{"id":val1.toString()}).subscribe(data => {
      this.getres = data as JSON;
      console.log(this.getres);
      alert(this.getres['response']);
      console.log(typeof(val1));
      
    })
  }

  oldvalues(val:string, val2:string, val3:string){
  console.log(val);
  console.log(val2);
  console.log(val3);
  this.oldcatName=val;
  this.oldPart1=val2;
  this.oldPart2=val3;
  }



}


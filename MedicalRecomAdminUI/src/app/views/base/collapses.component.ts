import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Inject }  from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { OnInit } from '@angular/core';

@Component({
  templateUrl: 'collapses.component.html',
  styleUrls: ['collapses.component.css']
})

export class CollapsesComponent implements OnInit{
	//categories=['Please Select Category','Category #1', 'Category #2', 'Category #3'];
	selectedCategory="";
	response1="";
	response2="";
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

    this.httpClient.post('http://18.214.223.82:5000/show-all-response/', {"showresponses":1}).subscribe(data => {
  	this.response_result = data as JSON;
  	this.all_responses_list.push(this.response_result);
  	//console.log(this.all_responses_list);

    this.categories.push(this.response_result);
    var i;
    for (i = 0; i < this.categories[0].length; i++) { 
    //console.log(this.categories[0][i]['category']);
    this.all_categories.push(this.categories[0][i]['category']);}
    let remove_duplicates_cat=Array.from(new Set(this.all_categories))
    //console.log(this.all_categories);
    //console.log(remove_duplicates_cat);
    this.remove_dupli_cat=remove_duplicates_cat;
  
  })
 
  }

  addresponse(){
  this.httpClient.post('http://18.214.223.82:5000/add-response/', {"category":this.selectedCategory, "response1":this.response1,"response2":this.response2}).subscribe(data => {
  	this.add_response_res = data as JSON;
    //alert(this.add_response_res);
  	//this.res1=this.['response']
  	alert(this.add_response_res['response']);
  	}
  
  )
  
  }

  resetresponseval(){
    (<HTMLInputElement>document.getElementById("select1")).value='';
    (<HTMLInputElement>document.getElementById("text-response1")).value='';
    (<HTMLInputElement>document.getElementById("text-response2")).value='';
  }

  editSave(val1:string, val2:string, val3:string){
  
    this.editCatName=val1;
    this.editPart1=val2;
    this.editPart2=val3;
    
    this.httpClient.post('http://18.214.223.82:5000/edit-response/',{"category":this.editCatName,
    "old_response1":this.oldPart1, "new_response1":this.editPart1,
    "old_response2":this.oldPart2, "new_response2":this.editPart2}).subscribe(data => {
      this.edit_response = data as JSON;
      //console.log(this.edit_response);
      alert(this.edit_response['response']);
      
    })
  }
delCatName="";
delPart1="";
delPart2="";
  deleteResponse(val1:string, val2:string, val3:string){
    
    this.delCatName=val1;
    this.delPart1=val2;
    this.delPart2=val3;
    //console.log(this.delCatName);
    //console.log(this.delPart1);
    //console.log(this.delPart2);
    this.httpClient.post('http://18.214.223.82:5000/delete-response/',{"category":this.delCatName, "response1":this.delPart1, "response2":this.delPart2}).subscribe(data => {
      this.getres = data as JSON;
      //console.log(this.getres);
      alert(this.getres['response']);
      
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

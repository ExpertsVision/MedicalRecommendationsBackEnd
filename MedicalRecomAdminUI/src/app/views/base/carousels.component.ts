import { Component } from '@angular/core';
import { CarouselConfig } from 'ngx-bootstrap/carousel';
import { HttpClient } from '@angular/common/http';
import { Inject }  from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { OnInit } from '@angular/core';
import {SupportService } from "./support.service";
//import { FormControl, FormGroup } from '@angular/forms';

@Component({
  templateUrl: 'carousels.component.html', 
  styleUrls: ['carousels.component.css'],
    providers: [
    { provide: CarouselConfig, useValue: { interval: 1500, noPause: true } }
  ]
})

export class CarouselsComponent implements OnInit {

  drugName="";
  tcgpiName="";
  ddid="";
  conceptId="";
  fileToUpload: File = null;
  getres=JSON;
  getres1=JSON;
  alldrugs=JSON;
  edit_drug_res=JSON;
  all_drugs_list=[];
  savEditDrugname=""
  savEditDDID="";
  savEditConceptId="";
  index: number;
  deldrugName="";
  delddId="";
  delconceptId="";
  resAfterAdd=JSON;
  flag=false;
  searchDrugname="";
  searchDrugResult=JSON;
  p:number;
  myFiles:string [] = [];
  myPdfFiles:string []=[];
  xmlfileName="";
  pdffileName="";
  constructor(private httpClient: HttpClient, @Inject(DOCUMENT) document,private user:SupportService) {
  }

  ngOnInit() {

    this.httpClient.post('http://18.214.223.82:5000/all-drugs/', {"showdrugs":1}).subscribe(data => {
    this.alldrugs = data as JSON;
    //this.all_drugs_list.push(this.alldrugs);
    this.user.tags_list.push(this.alldrugs);
    this.all_drugs_list=this.user.tags_list;
    console.log(this.all_drugs_list);
  
    })
  }
  getFileDetails (e) {

    for (var i = 0; i < e.target.files.length; i++) { 
      this.myFiles.push(e.target.files[i]);
    }
    //console.log(this.myFiles);
    this.xmlfileName=this.myFiles[0]['name'];
    //console.log(this.xmlfileName);
  }

  getPdfFileDetails (e) {
  
    for (var i = 0; i < e.target.files.length; i++) { 
      this.myPdfFiles.push(e.target.files[i]);
    }
    //console.log(this.myPdfFiles);
    this.pdffileName=this.myPdfFiles[0]['name'];
    //console.log(this.pdffileName);
  }

  addDrug(){
    if(this.myFiles.length!=0){
      const frmData = new FormData();
      for (var i = 0; i < this.myFiles.length; i++) { 
        frmData.append("fileUpload", this.myFiles[i]);
      }
      this.httpClient.post('http://18.214.223.82:5000/xml-file/', frmData).subscribe(data => {
      this.getres = data as JSON;
      //console.log(this.getres['response'])
    })
    this.myFiles=[];
    }
    
    if(this.myPdfFiles.length!=0){
      const frmData2 = new FormData();
      for (var i = 0; i < this.myPdfFiles.length; i++) { 
        frmData2.append("fileUpload", this.myPdfFiles[i]);
      }
      this.httpClient.post('http://18.214.223.82:5000/pdf-file/', frmData2).subscribe(data => {
      this.getres1 = data as JSON;
      //console.log(this.getres1['response'])
    })
    this.myPdfFiles=[];
    }
  
    //console.log(frmData);
    this.httpClient.post('http://18.214.223.82:5000/add-drug/',{"drugname":this.drugName, "DDID":this.ddid,"ConceptId":this.conceptId,"TCGPI":this.tcgpiName,"xmlfile":this.xmlfileName,"pdffile":this.pdffileName}).subscribe(data => {
    this.resAfterAdd = data as JSON;
    alert(this.resAfterAdd['response']);
  })

  
  }

  resetPdfInputField(){
    (<HTMLInputElement>document.getElementById("drugname")).value='';
    (<HTMLInputElement>document.getElementById("tcgpiname")).value='';
    (<HTMLInputElement>document.getElementById("ddidname")).value='';
    (<HTMLInputElement>document.getElementById("conceptidname")).value='';
    (<HTMLInputElement>document.getElementById("xmlfile-input")).value='';
    (<HTMLInputElement>document.getElementById("pdffile-input")).value='';
    this.myFiles=[];
  }

  resetXmlInputField(){
  this.myFiles=[];
  (<HTMLInputElement>document.getElementById("xmlfile-input")).value='';
  }



  

  editSave(val1:string, val2:string, val3:string){

    this.savEditDrugname=val1;
    this.savEditDDID=val2;
    this.savEditConceptId=val3;

    //console.log(this.savEditDrugname);
    //console.log(this.savEditDDID);
    //console.log(this.savEditConceptId);
    this.httpClient.post('http://18.214.223.82:5000/edit-drug/',{"drugname":this.savEditDrugname, "DDID":this.savEditDDID,"ConceptId":this.savEditConceptId}).subscribe(data => {
      this.edit_drug_res = data as JSON;
      //console.log(this.edit_drug_res);
      alert(this.edit_drug_res['response']);
      
    })
  }

  deleteDrug(val:string){
    
    this.delddId=val;
    console.log(this.delddId);
    this.httpClient.post('http://18.214.223.82:5000/delete-drug/',{"ddid":this.delddId}).subscribe(data => {
      this.getres = data as JSON;
      //console.log(this.getres);
      alert(this.getres['response']);
      
    })
  }

  searchDrug() {
    this.flag=true;
    this.httpClient.post('http://18.214.223.82:5000/search-drug/',{"drugname":this.searchDrugname}).subscribe(data => {
    this.searchDrugResult = data as JSON;
    console.log(this.searchDrugResult);
    alert(this.searchDrugResult['drugname']);
    
  })
  }

  resetDrugval(){

  (<HTMLInputElement>document.getElementById("searchdrugname")).value='';
  }

}

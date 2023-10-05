import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-crear-usuario',
  templateUrl: './crear-usuario.component.html',
  styleUrls: ['./crear-usuario.component.css']
})
export class CrearUsuarioComponent {
  selectedComponent: number = 0;
  varSexo: boolean = false;
  varNoSexo: boolean = true;

  onDaySelected(dayNumber: number) {
    console.log(`Selected day ${dayNumber}`);
  }
  skip() {
      
    if (this.selectedComponent < 6) {
      this.selectedComponent++;
      if (this.selectedComponent == 5){
        this.varSexo=true;
        this.varNoSexo=false;
        localStorage.setItem('dia', '1');
        localStorage.setItem('mes', '1');
        localStorage.setItem('anio', '1900');
        localStorage.setItem('altura', '1');
        localStorage.setItem('peso', '1');

      }
    }
  }
 


  componentsArray = [
   
    {
      "numbers": [],
      "title": "How Old Are You?",
      "description": "Day",
      "minValue": 1,
      "maxValue": 31,
    },
    {
      "numbers": [],
      "title": "How Old Are You?",
      "description": "Month",
      "minValue": 1,
      "maxValue": 12,
    },
    {
      "numbers": [],
      "title": "How Old Are You?",
      "description": "Year",
      "minValue": 1900,
      "maxValue": 2023,
    },
    {
      "numbers": [],
      "title": "What's your height?",
      "description": "Height in cm. Don't worry, you can always change this later.",
      "minValue": 100,
      "maxValue": 250,
    },
    {
      "numbers": [],
      "title": "What's your weight?",
      "description": "Weight in kg. Don't worry, you can always change this later.",
      "minValue": 30,
      "maxValue": 250,

    },
    {
      "numbers": [],
      "title": "Tell Us About Yourself",
      "description": "To give you a better experience and results We need to know your gender.",
      "minValue": 1,
      "maxValue": 2,
    }

  ];
  constructor(private router: Router) {}

   


  onContinue() {
    if (this.selectedComponent < 6) {
      this.selectedComponent++;
      if (this.selectedComponent == 5){
        this.varSexo=true;
        this.varNoSexo=false;
      }
    }
    // if (this.selectedComponent == 6){
    //     this.router.navigate(['/editar_perfil']);
    // } 
  };
  onBack() {
    if (this.selectedComponent ==0) {
      this.deleteadia();}
    if (this.selectedComponent ==1) {
      this.deleteames();}
    if (this.selectedComponent ==2) {
      this.deleteaanio();}
    if (this.selectedComponent ==3) {
      this.deleteaaltura();}
    if (this.selectedComponent ==4) {
      this.deleteapeso();}
    

    if (this.selectedComponent >= 0) {
      this.selectedComponent--;}
      if (this.selectedComponent != 5){
        this.varSexo=false;
        this.varNoSexo=true;
  }
  }
  deleteadia(){
    localStorage.removeItem('dia');
  }
  deleteames(){
    localStorage.removeItem('mes');
  }
  deleteaanio(){
    localStorage.removeItem('anio');
  }
  deleteaaltura(){
    localStorage.removeItem('altura');
  }
  deleteapeso(){
    localStorage.removeItem('peso');
  }
  deleteasexo(){
    localStorage.removeItem('sexo');
  }

}


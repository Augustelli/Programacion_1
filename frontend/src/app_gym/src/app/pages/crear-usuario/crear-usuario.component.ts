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
    if (this.selectedComponent == 6){
        this.router.navigate(['/editar_perfil']);
    } 
  };
  onBack() {
    if (this.selectedComponent >= 0) {
      this.selectedComponent--;}
      if (this.selectedComponent != 5){
        this.varSexo=false;
        this.varNoSexo=true;
  }
  }

}
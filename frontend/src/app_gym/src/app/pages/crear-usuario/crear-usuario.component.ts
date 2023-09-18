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

  componentsArray = [
    {
      "numbers": [],
      "title": "Tell Us About Yourself",
      "description": "To give you a better experience and results We need to know your gender."
    },
    {
      "numbers": [],
      "title": "How Old Are You?",
      "description": "Day"
    },
    {
      "numbers": [],
      "title": "How Old Are You?",
      "description": "Month"
    },
    {
      "numbers": [],
      "title": "How Old Are You?",
      "description": "Year"
    },
    {
      "numbers": [],
      "title": "What's your height?",
      "description": "Height in cm. Don't worry, you can always change this later."
    },
    {
      "numbers": [],
      "title": "What's your weight?",
      "description": "Weight in kg. Don't worry, you can always change this later."
    },
    {
      "numbers": [],
      "title": "Tell Us About Yourself",
      "description": "To give you a better experience and results We need to know your gender."
    }

  ];
  constructor(private router: Router) {}

  

  onContinue() {
    if (this.selectedComponent < 7) {
      this.selectedComponent++;
      if (this.selectedComponent == 6){
        this.varSexo=true;
        this.varNoSexo=false;
      }
    }
    if (this.selectedComponent == 7){
        this.router.navigate(['/editar_perfil']);
    } 
  };
  onBack() {
    if (this.selectedComponent > 0) {
      this.selectedComponent--;}
      if (this.selectedComponent != 6){
        this.varSexo=false;
        this.varNoSexo=true;
  }
  }

}
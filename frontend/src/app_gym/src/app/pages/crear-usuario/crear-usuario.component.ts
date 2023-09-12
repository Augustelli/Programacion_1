import { Component } from '@angular/core';

@Component({
  selector: 'app-crear-usuario',
  templateUrl: './crear-usuario.component.html',
  styleUrls: ['./crear-usuario.component.css']
})
export class CrearUsuarioComponent {
  selectedComponent: number = 0;

  componentsArray = [
    {
      "numbers": [],
      "title": "edad",
      "description": "algo"
    },
    {
      "numbers": [],
      "title": "dia",
      "description": "algo"
    },
    {
      "numbers": [],
      "title": "anio",
      "description": "algo"
    },
    {
      "numbers": [],
      "title": "altura",
      "description": "algo"
    },
    {
      "numbers": [],
      "title": "mes",
      "description": "algo"
    }
  ];

  onContinue() {
    if (this.selectedComponent < 4) {
      this.selectedComponent++;
    }
  }
}
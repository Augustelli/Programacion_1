import { Component } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-ver-planificaciones',
  templateUrl: './ver-planificaciones.component.html',
  styleUrls: ['./ver-planificaciones.component.css']
})
export class VerPlanificacionesComponent {

  @Output() planificacionClickeada = new EventEmitter<void>();

  varVerPlanificaciones = true;

  
  arrayPlanificaciones=[
    {
      img:"../../../assets/planificacion/chicaplanificacion1.png",
      nombreprofesor: "Augusto Mancuso",
      nombreclase: "Entrenamiento Pecho",

    },
    {
      img:"../../../assets/planificacion/chicaplanificacion2.png",
      nombreprofesor: "Franco Narvaez",
      nombreclase: "Entrenamiento Piernas",

    },
    {
      img:"../../../assets/planificacion/chicaplanificacion3.png",
      nombreprofesor: "Juan Perez",
      nombreclase: "Zumba",
    }
  ]
  onPlanificacionClick() {
    this.planificacionClickeada.emit();}
    
  constructor() { }

  ngOnInit(): void {
    console.log('arrayPlanificaciones', this.arrayPlanificaciones);
  }
  
  verPlanificaciones(){
      this.varVerPlanificaciones = true;
    }

  ocultarPlanificaciones(){
      this.varVerPlanificaciones = false;}

}


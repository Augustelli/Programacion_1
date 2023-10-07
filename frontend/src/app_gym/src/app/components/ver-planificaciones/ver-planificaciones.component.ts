import { Component } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-ver-planificaciones',
  templateUrl: './ver-planificaciones.component.html',
  styleUrls: ['./ver-planificaciones.component.css']
})
export class VerPlanificacionesComponent {

  @Output() planificacionClickeada = new EventEmitter<void>();

  varVerPlanificaciones = true;

  
  arrayPlanificaciones=[
    // {
    //   img:"../../../assets/planificacion/chicaplanificacion1.png",
    //   nombreprofesor: "Augusto Mancuso",
    //   nombreclase: "Entrenamiento Pecho",

    // },
    // {
    //   img:"../../../assets/planificacion/chicaplanificacion2.png",
    //   nombreprofesor: "Franco Narvaez",
    //   nombreclase: "Entrenamiento Piernas",

    // },
    // {
    //   img:"../../../assets/planificacion/chicaplanificacion3.png",
    //   nombreprofesor: "Juan Perez",
    //   nombreclase: "Zumba",
    // }
    
      {
        "fecha": "10-05-2023",
        "frecuencia": "Lunes y Viernes",
        "idPlanificacion": 1,
        "idProfesor": 3,
        "id_Alumno": 1,
        "id_Clase": 3,
        "rutina": "Entrenamiento de biceps"
      },
      {
        "fecha": "10-05-2023",
        "frecuencia": "Miercoles y Sabado",
        "idPlanificacion": 2,
        "idProfesor": 3,
        "id_Alumno": 1,
        "id_Clase": 3,
        "rutina": "Entrenamiento de pecho"
      }
    ]
  
  
  onPlanificacionClick() {
    this.planificacionClickeada.emit();}
    
  constructor(
    private planificacionService: PlanificacionService,
    private router: Router,
  ) { }

  ngOnInit(): void {
      this.planificacionService.getPlanificaciones().subscribe((data: any) => {
          console.log('JSON data:', data);
          this.arrayPlanificaciones = data;
      });
    console.log('arrayPlanificaciones', this.arrayPlanificaciones);
  }
  
  verPlanificaciones(){
      this.varVerPlanificaciones = true;
    }

  ocultarPlanificaciones(){
      this.varVerPlanificaciones = false;}

}






























































// import { Component, OnInit } from '@angular/core';
// import { Output, EventEmitter } from '@angular/core';
// import { Router } from '@angular/router';
// import { PlanificacionService } from '../../services/planificacion.service';

// @Component({
//   selector: 'app-ver-planificaciones',
//   templateUrl: './ver-planificaciones.component.html',
//   styleUrls: ['./ver-planificaciones.component.css']
// })
// export class VerPlanificacionesComponent implements OnInit{

//   // @Output() planificacionClickeada = new EventEmitter<void>();

//   // varVerPlanificaciones = true;
  
  
//   arrayPlanificaciones: any[] = [];
//   //   {
//   //     img:"../../../assets/planificacion/chicaplanificacion1.png",
//   //     nombreprofesor: "Augusto Mancuso",
//   //     nombreclase: "Entrenamiento Pecho",

//   //   },
//   //   {
//   //     img:"../../../assets/planificacion/chicaplanificacion2.png",
//   //     nombreprofesor: "Franco Narvaez",
//   //     nombreclase: "Entrenamiento Piernas",

//   //   },
//   //   {
//   //     img:"../../../assets/planificacion/chicaplanificacion3.png",
//   //     nombreprofesor: "Juan Perez",
//   //     nombreclase: "Zumba",
//   //   }
//   // ]
  
//   // onPlanificacionClick() {
//   //   this.planificacionClickeada.emit();}
    
//   constructor(
//     private router: Router,
//     private planificacionService: PlanificacionService
//   ) { }

//   ngOnInit(): void {
//     // console.log('arrayPlanificaciones', this.arrayPlanificaciones);
//     this.planificacionService.getPlanificaciones().subscribe((data) => {
//       this.arrayPlanificaciones = data;
//     },
//     (error) => {
//       console.error('Error al obtener planificaciones: ', error);
//     });
//   }
  
//   // verPlanificaciones(){
//   //     this.varVerPlanificaciones = true;
//   //   }

//   // ocultarPlanificaciones(){
//   //     this.varVerPlanificaciones = false;}

//   editarPlanificacionesBtn(){
//     this.router.navigate(['/EditarPlanificaciones']);}
// }

import { Component } from '@angular/core';

@Component({
  selector: 'app-ver-clases',
  templateUrl: './ver-clases.component.html',
  styleUrls: ['./ver-clases.component.css']
})
export class VerClasesComponent {

  varVerClases = true;
  arrayClases=[
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Pecho",
      nombreProfesor: "Augusto Mancuso",
      horario: "Lunes 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},

    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Piernas",
      nombreProfesor: "Franco Narvaez",
      horario: "Martes 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Zumba",
      nombreProfesor: "Juan Perez",
      horario: "Miercoles 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Pecho",
      nombreProfesor: "Augusto Mancuso",
      horario: "Jueves 18:00hs",
      duracion: "1:00hs",
      cupos: "20"},
    {
      img:"../../../assets/clases/clases.png",
      nombreClase: "Entrenamiento Piernas",
      nombreProfesor: "Franco Narvaez",
      horario: "Viernes 18:00hs",
      duracion: "1:00hs",
      cupos: "20"}


  ]

  constructor() { }

  ngOnInit(): void {
    console.log('arrayClases', this.arrayClases);
  }
  
  verClases(){
      this.varVerClases = true;
    }

  ocultarClases(){
      this.varVerClases = false;}



}

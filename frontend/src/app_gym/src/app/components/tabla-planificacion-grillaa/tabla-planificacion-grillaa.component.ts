import { AfterViewInit, Component, OnInit} from '@angular/core';
import { ViewChild } from '@angular/core';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatTableDataSource, MatTableModule} from '@angular/material/table';;
import { NgIf,NgFor } from '@angular/common';
import { JwtHelperService } from '@auth0/angular-jwt';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; 


@Component({
  selector: 'app-tabla-planificacion-grillaa',
  templateUrl: './tabla-planificacion-grillaa.component.html',
  styleUrls: ['./tabla-planificacion-grillaa.component.css'],
  standalone: true,
  imports: [MatTableModule, NgIf, NgFor],



})


export class TablaPlanificacionGrillaaComponent implements OnInit {
  
  constructor(
    private planificacionService: PlanificacionService,
    private jwtHelper: JwtHelperService
    ) { }

  isToken: boolean = false;
  planificaciones: any = [];
  userRol:string = '';
  arrayPlanificacionesDetalle: any=[];
  idPlanificaciones: any;
  mostrarFormulario = false;
  nuevoEjercicio: string = '';
  nuevasRepeticiones: string = '';
  nuevoRIR: string = '';



  ngOnInit(): void {
    

    const token = localStorage.getItem('token');
    if (token) {
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
      this.isToken = true;
    }
  
    if (this.userRol == 'profesor' || this.userRol == 'admin' || this.userRol == 'alumno') {
      const idPlanificaciones = localStorage.getItem('idPlanificacion');
  
      this.planificacionService.getPlanificacionDetalle(idPlanificaciones).subscribe((data: any) => {
        console.log('JSON data:', data);
        this.arrayPlanificacionesDetalle = data; // Asegúrate de que "PlanificacionDetalle" es la propiedad que contiene los detalles de la planificación
      });
}
  }
  agregarFila() {
    this.mostrarFormulario = true;
    
  }realizarPUT() {
    const data = {
      ejercicio: this.nuevoEjercicio,
      repeticiones: this.nuevasRepeticiones,
      rir: this.nuevoRIR,
    };
  
    this.planificacionService.putPlanificacionDetalle(this.idPlanificaciones, data).subscribe((data: any) => {
      console.log('JSON data:', data);
      this.arrayPlanificacionesDetalle = data; // Asegúrate de que "PlanificacionDetalle" es la propiedad que contiene los detalles de la planificación
    });
  }
  


}

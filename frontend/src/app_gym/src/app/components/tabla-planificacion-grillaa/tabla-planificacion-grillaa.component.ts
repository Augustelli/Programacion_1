import { AfterViewInit, Component, OnInit} from '@angular/core';
import { ViewChild } from '@angular/core';
import {MatPaginator, MatPaginatorModule} from '@angular/material/paginator';
import {MatTableDataSource, MatTableModule} from '@angular/material/table';;
import { NgIf,NgFor } from '@angular/common';
import { JwtHelperService } from '@auth0/angular-jwt';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; 
import { NgForm } from '@angular/forms';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-tabla-planificacion-grillaa',
  templateUrl: './tabla-planificacion-grillaa.component.html',
  styleUrls: ['./tabla-planificacion-grillaa.component.css'],
  // standalone: true,
  // imports: [MatTableModule, NgIf, NgFor],



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
  editableDetalle: any = null;


  nuevaPlanificacion = {
    idPlanificacion: '',
    nombre: '',
    repeticion: '',
    rir: '',
  };
  showEditModal: boolean = false;
  detalleSeleccionado: any = {};

   arrayPlanificacionesDetalleGuess1 = [
    {
        "idPlanificacionDetalle": 1,
        "idPlanificacion": 1,
        "nombre": "biceps alternados",
        "repeticion": 12,
        "rir": 2
    },
    {
        "idPlanificacionDetalle": 3,
        "idPlanificacion": 1,
        "nombre": "biceps alternados",
        "repeticion": 12,
        "rir": 2
    },
    // ... otros datos
    {
        "idPlanificacionDetalle": 10,
        "idPlanificacion": 2,
        "nombre": "Volada Lateral",
        "repeticion": 10,
        "rir": 0
    }
];





  




  ngOnInit(): void {
    

    const token = localStorage.getItem('token');
    if (token) {
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
      this.isToken = true;
    }
    if (this.isToken == false) {
      this.arrayPlanificacionesDetalle = this.arrayPlanificacionesDetalleGuess1;
      console.log('JSON data:', this.arrayPlanificacionesDetalle);
    }
  
    if (this.userRol == 'profesor' || this.userRol == 'admin' || this.userRol == 'alumno') {
      const idPlanificaciones = localStorage.getItem('idPlanificacion');
      this.idPlanificaciones = idPlanificaciones;
  
      this.planificacionService.getPlanificacionDetalle(idPlanificaciones).subscribe((data: any) => {
        console.log('JSON data:', data);
        this.arrayPlanificacionesDetalle = data; // Asegúrate de que "PlanificacionDetalle" es la propiedad que contiene los detalles de la planificación
      });
    }

      

  }
  agregarFila() {
    this.mostrarFormulario = true;
    
  }
  
  realizarPUT() {
    const data = {
      idPlanificacion : this.idPlanificaciones,
      nombre: this.nuevaPlanificacion.nombre,
      repeticion: this.nuevaPlanificacion.repeticion,
      rir: this.nuevaPlanificacion.rir,
    };
    console.log(data);
  
    this.planificacionService.crearPlanificacionDetalle( data).subscribe((data: any) => {
      console.log('JSON data:', data);
       // Asegúrate de que "PlanificacionDetalle" es la propiedad que contiene los detalles de la planificación
    });
    this.mostrarFormulario = false;
    this.ngOnInit();
  }

  
  eliminarDetalle(idPlanificacionDetalle:any) {
    // Lógica para eliminar el detalle
    console.log('Eliminar detalle:', idPlanificacionDetalle);
    this.planificacionService.deletePlanificacionDetalle(idPlanificacionDetalle).subscribe((data: any) => {
      console.log('JSON data:', data);
       // Asegúrate de que "PlanificacionDetalle" es la propiedad que contiene los detalles de la planificación
       this.ngOnInit();
    }
    );
  }
  

}


import { Component, OnInit } from '@angular/core';
import { TablaPlanificacionGrillaaComponent } from 'src/app/components/tabla-planificacion-grillaa/tabla-planificacion-grillaa.component';
import { JwtHelperService } from '@auth0/angular-jwt';
import { PlanificacionService } from 'src/app/services/planificacion.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{
  varVerPlanificaciones = true;
  varNoVerPlanificaciones = false;
  successMessage: string = '';
  userRol:string = '';
  isToken: boolean = false;
  idPlanificaciones: any;

  constructor(
    private jwtHelper: JwtHelperService,
    private planificacionService: PlanificacionService
    ) {}

  onPlanificacionClickeada(idPlanificacion: any) {
    this.varVerPlanificaciones = false;
    this.varNoVerPlanificaciones = true; // Cambia esto según tu lógica
    console.log('ID de la planificacion clickeada:', idPlanificacion);
    localStorage.setItem('idPlanificacion', idPlanificacion);
  ;
  }
  back() {
    this.varVerPlanificaciones = true;
    this.varNoVerPlanificaciones = false;
  }
  ngOnInit() {
    const token = localStorage.getItem('token');
    this.successMessage='Esperando validación de token por el ADMIN, mas tarde verá todas las funcionalidades...';
    if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
      this.isToken = true;
  }else{
    this.isToken = false;
    
    
    this.successMessage='Usted no se ha registrado, la visión sera reducidada...';
  }
  
    // this.usuariosService.getUsers().subscribe((data:any) => {
    //   console.log('JSON data:', data);
    //   this.arrayUsuarios = data.Usuario;
    // })
    // const token = localStorage.getItem('token');
    // if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
    //   const decodedToken = this.jwtHelper.decodeToken(token);
    //   this.userRol = decodedToken.rol;
  }
    
    // this.successMessage='Bienvenido, usted esta registrado...';
  }


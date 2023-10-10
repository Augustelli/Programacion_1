import { Component, OnInit } from '@angular/core';
import { TablaPlanificacionGrillaaComponent } from 'src/app/components/tabla-planificacion-grillaa/tabla-planificacion-grillaa.component';
import { JwtHelperService } from '@auth0/angular-jwt';

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

  constructor(
    private jwtHelper: JwtHelperService
    ) {}

  onPlanificacionClickeada() {
    this.varVerPlanificaciones = false;
    this.varNoVerPlanificaciones = true; // Cambia esto según tu lógica
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
  }
}

}

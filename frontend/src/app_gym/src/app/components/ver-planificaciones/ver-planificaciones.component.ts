import { Component } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { JwtHelperService } from '@auth0/angular-jwt';

@Component({
  selector: 'app-ver-planificaciones',
  templateUrl: './ver-planificaciones.component.html',
  styleUrls: ['./ver-planificaciones.component.css']
})
export class VerPlanificacionesComponent {

  @Output() planificacionClickeada = new EventEmitter<void>();

  arrayPlanificaciones: any;

  varVerPlanificaciones = true;
  isToken: boolean = false;
  userRol:string = '';
  dni: string = '';

  

  
  arrayPlanificacionesGuess=[
    {
      
      nombreprofesor: "Augusto Mancuso",
      nombreclase: "Entrenamiento Pecho",

    },
    {
      
      nombreprofesor: "Franco Narvaez",
      nombreclase: "Entrenamiento Piernas",

    },
    {
      
      nombreprofesor: "Juan Perez",
      nombreclase: "Zumba",
    }
  ]
  onPlanificacionClick() {
    this.planificacionClickeada.emit();}
    
  constructor(
    private planificacionService: PlanificacionService,
    private jwtHelper: JwtHelperService,
  ) { }

  ngOnInit(): void {

    console.log('arrayPlanificaciones', this.arrayPlanificaciones);
    const token = localStorage.getItem('token');
    // this.successMessage='Esperando validación de token por el ADMIN, mas tarde verá todas las funcionalidades...';
    if (token){ // Reemplaza 'tu_variable_token' con el nombre de tu variable local que contiene el token.
      const decodedToken = this.jwtHelper.decodeToken(token);
      this.userRol = decodedToken.rol;
      this.isToken = true;
      this.dni = decodedToken.dni;
  }else{
    this.isToken = false;
    this.arrayPlanificaciones = this.arrayPlanificacionesGuess;
  }
  if (this.userRol=='profesor' || this.userRol=='admin')  {
    // Utiliza el servicio para obtener los datos del usuario
    this.planificacionService.getPlanificaciones().subscribe(
      (data: any) => {
        console.log('Datos del usuario', data);
        this.arrayPlanificaciones = data.Planificacion;
        // console.log('Datos del usuario', this.userData);
        // this.fillFormFields();
      },
      (error) => {
        console.error('Error al obtener los datos del usuario', error);
      }
    );
  }
  if(this.userRol=='alumno'){
    this.planificacionService.getPlanificacionAlumno(this.dni).subscribe(
      (data: any) => {
        console.log('Datos del usuario', data);
        this.arrayPlanificaciones = data.Planificacion;
        // console.log('Datos del usuario', this.userData);
        // this.fillFormFields();
      },
      (error) => {
        console.error('Error al obtener los datos del usuario', error);
      }
    );
  }
}
  
  verPlanificaciones(){
      this.varVerPlanificaciones = true;
    }

  ocultarPlanificaciones(){
      this.varVerPlanificaciones = false;}

    deletePlanificacion(){
      console.log('Planificacion a eliminar');
      
    }

}


import { Component , OnInit} from '@angular/core';
import { Output, EventEmitter } from '@angular/core';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { JwtHelperService } from '@auth0/angular-jwt';

@Component({
  selector: 'app-ver-planificaciones',
  templateUrl: './ver-planificaciones.component.html',
  styleUrls: ['./ver-planificaciones.component.css']
})
export class VerPlanificacionesComponent implements OnInit {

  @Output() planificacionClickeada = new EventEmitter<void>();

  arrayPlanificaciones: any;

  varVerPlanificaciones = true;
  isToken: boolean = false;
  userRol:string = '';
  dni: string = '';
  editando: boolean = false;
  datosEditados: any = {};
  mostrarFormularioCreacion = false;
  nuevaPlanificacion = {
    rutina: '',
    frecuencia: '',
    id_Alumno: '', // El ID del alumno correspondiente
    id_Clase: '', // El ID de la clase correspondiente
    idProfesor: '', // El ID del profesor correspondiente
  };

  

  
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
// activarEdicion() {
//   this.editando = true;
//   // Copiar los datos de la planificación actual a los datos editados
//   this.datosEditados = { ...this.planificacion };
// }
  
  verPlanificaciones(){
      this.varVerPlanificaciones = true;
    }

  ocultarPlanificaciones(){
      this.varVerPlanificaciones = false;}

    deletePlanificacion(idPlanificacion: string){
      this.planificacionService.deletePlanificacion(idPlanificacion).subscribe(
        (data: any) => {
          console.log('Datos del usuario', data);
        },
        (error) => {
          console.error('Error al obtener los datos del usuario', error);
        }
      );

    }
    editarPlanificacion(planificacion: any) {
      // this.editando = true;
      planificacion.editando = true;
      this.datosEditados = { ...planificacion };
    }
    

    guardarCambios(planificacion: any) {
      const datosParaActualizar = {
        rutina: planificacion.rutina,
        frecuencia: planificacion.frecuencia,
        id_Alumno: planificacion.id_Alumno,
        id_Clase: planificacion.id_Clase,
        idProfesor: planificacion.idProfesor
      };
      console.log('datosEditados', datosParaActualizar);
      console.log('Planificación a editar', planificacion);
      delete this.datosEditados.idPlanificacion;
      // Enviar una solicitud de actualización al servidor con this.datosEditados
      this.planificacionService.actualizarPlanificacion(planificacion.idPlanificacion, datosParaActualizar).subscribe(
        (data: any) => {
          console.log('Planificación actualizada', data);
          this.editando = false;
          planificacion.editando = false;
           // Volver al modo de visualización
          // Actualizar la interfaz de usuario o recargar datos si es necesario
        },
        (error) => {
          console.error('Error al actualizar la planificación', error);
          // Manejar errores y proporcionar retroalimentación al usuario
        }
      );
    }
    crearPlanificacion() {
      // Crea un objeto con los datos de la nueva planificación
      console.log('Nueva planificación', this.nuevaPlanificacion);
      const datosParaPost = {
        rutina: this.nuevaPlanificacion.rutina,
        frecuencia: this.nuevaPlanificacion.frecuencia,
        id_Alumno: this.nuevaPlanificacion.id_Alumno,
        id_Clase: this.nuevaPlanificacion.id_Clase,
        idProfesor: this.nuevaPlanificacion.idProfesor
      };

      console.log('datosParaPost', datosParaPost);
     
    
      // Realiza una solicitud POST al servicio para crear la nueva planificación
      this.planificacionService.crearPlanificacion(datosParaPost).subscribe(
        (data: any) => {
          console.log('Nueva planificación creada', data);
          // Actualiza la interfaz de usuario o recarga datos si es necesario
        },
        (error) => {
          console.error('Error al crear la planificación', error);
          // Maneja errores y proporciona retroalimentación al usuario
        }
      );
    }
    

}


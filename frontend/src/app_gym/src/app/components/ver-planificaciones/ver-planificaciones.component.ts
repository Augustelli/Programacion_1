import { Component , OnInit} from '@angular/core';
import { Output, EventEmitter } from '@angular/core';
import { PlanificacionService } from 'src/app/services/planificacion.service';
import { JwtHelperService } from '@auth0/angular-jwt';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-ver-planificaciones',
  templateUrl: './ver-planificaciones.component.html',
  styleUrls: ['./ver-planificaciones.component.css']
})
export class VerPlanificacionesComponent implements OnInit {

  @Output() planificacionClickeada = new EventEmitter<void>();

  arrayPlanificaciones: any;
  page=1;
  perPage=6;
  isLastPage: boolean = true;
  totalItems = 0;

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
    fecha: ''
  };
  mensajeExito: string = '';
  searchTerm: string = '';  
  arrayPlanificacionesGuess=[
    {
      
      rutina: "Entrenamiento de biceps",
     frecuencia: "Lunes",
    fecha : "25-05-2021",

    },
    {
      
      rutina: "Entrenamiento de triceps",
     frecuencia: "Martes",
    fecha : "26-05-2021"},
    {
      
      rutina: "Entrenamiento de pecho",
     frecuencia: "Miercoles",
     fecha : "27-05-2021"},

   
  ]
  onPlanificacionClick(idPlanificacion: any) {
    this.planificacionClickeada.emit(idPlanificacion);
  }
  
    
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
      
      console.log('decodedToken', decodedToken.id);
      this.isToken = true;
      this.dni = decodedToken.id;
  }else{
    this.isToken = false;
    this.arrayPlanificaciones = this.arrayPlanificacionesGuess;
  }
  if (this.userRol=='profesor' || this.userRol=='admin')  {
    // Utiliza el servicio para obtener los datos del usuario
    this.planificacionService.getPlanificaciones(this.page, this.perPage).subscribe(
      (data: any) => {
        console.log('Datos del usuario', data);
        this.arrayPlanificaciones = data.Planificacion;
        this.totalItems = data.Total;
        this.isLastPage = this.totalItems / this.perPage <= this.page;
        
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
  if(this.userRol=='espera'){
    this.arrayPlanificaciones = this.arrayPlanificacionesGuess;
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
        idProfesor: planificacion.idProfesor,
       
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
      const fechaFormateada = new Date(this.nuevaPlanificacion.fecha).toLocaleDateString('es-ES', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
      });
      const fechaFormateadaConGuion = fechaFormateada.split('/').join('-');

      // Crea un objeto con los datos de la nueva planificación
      console.log('Nueva planificación', this.nuevaPlanificacion);
      const datosParaPost = {
        rutina: this.nuevaPlanificacion.rutina,
        frecuencia: this.nuevaPlanificacion.frecuencia,
        id_Alumno: this.nuevaPlanificacion.id_Alumno,
        id_Clase: this.nuevaPlanificacion.id_Clase,
        idProfesor: this.nuevaPlanificacion.idProfesor,
        fecha : fechaFormateadaConGuion
      };

      console.log('datosParaPost', datosParaPost);
     
    
      // Realiza una solicitud POST al servicio para crear la nueva planificación
      this.planificacionService.crearPlanificacion(datosParaPost).subscribe(
        (data: any) => {
          console.log('Nueva planificación creada', data);
          this.mostrarFormularioCreacion = false;
          // this.mensajeExito = 'La planificación se ha creado con éxito';
          this.mensajeExito = 'La planificación se ha creado con éxito';
          setTimeout(() => {
            this.mensajeExito = ''; // Restablecer el mensaje de éxito después de 5 segundos
          }, 3000); // 5000 milisegundos = 5 segundos
          

          // Actualiza la interfaz de usuario o recarga datos si es necesario
        },
        (error) => {
          console.error('Error al crear la planificación', error);
          // Maneja errores y proporciona retroalimentación al usuario
        }
      );
    }
    


    filtrarUsuariosNombre() {
      if (this.searchTerm) {
        this.page = 1;
        this.perPage = 100; // Otra cantidad de elementos por página si es necesario
        this.mostrarTodo(); // Asegúrate de manejar correctamente la lógica de mostrarTodo()
      } else {
        this.page = 1;
        this.perPage = 6; // Otra cantidad de elementos por página si es necesario
        this.mostrarTodo(); // Asegúrate de manejar correctamente la lógica de mostrarTodo()
      }
    }
    
    mostrarTodo() {
      this.planificacionService.getPlanificaciones(this.page, this.perPage).subscribe((data: any) => {
        console.log('HOLAAA:', data);
        if (this.searchTerm) {
          this.arrayPlanificaciones = data.Planificacion.filter((planificacion: any) => {
            const nombreCompleto = `${planificacion.rutina} `;
            return nombreCompleto.toLowerCase().includes(this.searchTerm.toLowerCase());
          });
        } else {
          this.arrayPlanificaciones = data.Planificacion;
        }
      });
    }
    
onClickAnteriorPag(){
    this.page-=1;
    this.ngOnInit();


  }
onClickSiguientePag(){

  this.page+=1;
  this.ngOnInit();
  }

}



import { Component , OnInit} from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { ClasesService } from 'src/app/services/clases.service';

@Component({
  selector: 'app-ver-clases',
  templateUrl: './ver-clases.component.html',
  styleUrls: ['./ver-clases.component.css']
})
export class VerClasesComponent implements OnInit{

  varVerClases = true;
  mostrarFormularioCreacion = false;
  mensajeExito: string = '';
  
  isToken: boolean = false;
  editando: boolean = false;
  datosEditados: any = {};
  userRol:string = '';
  dni: string = '';
  arrayClases: any;
  searchTerm: string = '';



  arrayClasesGuess=[
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
  getClasesEnPares() {
    const clasesEnPares = [];
    for (let i = 0; i < this.arrayClases.length; i += 2) {
      const par = [this.arrayClases[i], this.arrayClases[i + 1]];
      clasesEnPares.push(par);
    }
    return clasesEnPares;
  }

  constructor(
    private jwtHelper: JwtHelperService,
    private clasesService: ClasesService,
  ) { }

  ngOnInit(): void {
   
    
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
    this.arrayClases = this.arrayClasesGuess;
  }
  if (this.userRol=='profesor' || this.userRol=='admin')  {
    // Utiliza el servicio para obtener los datos del usuario
    this.clasesService.getClases().subscribe(
      (data: any) => {
        console.log('Datos del usuario', data);
        this.arrayClases = data.Clases;
        console.log('Datos del usuario', this.arrayClases);
        
        // console.log('Datos del usuario', this.userData);
        // this.fillFormFields();
      },
      (error) => {
        console.error('Error al obtener los datos del usuario', error);
      }
    );
  }
//   if(this.userRol=='alumno'){
//     this.planificacionService.getPlanificacionAlumno(this.dni).subscribe(
//       (data: any) => {
//         console.log('Datos del usuario', data);
//         this.arrayPlanificaciones = data.Planificacion;
//         // console.log('Datos del usuario', this.userData);
//         // this.fillFormFields();
//       },
//       (error) => {
//         console.error('Error al obtener los datos del usuario', error);
//       }
//     );
//   }
//   if(this.userRol=='espera'){
//     this.arrayPlanificaciones = this.arrayPlanificacionesGuess;
//   }
// }

  }
  
  verClases(){
      this.varVerClases = true;
    }

  ocultarClases(){
      this.varVerClases = false;}

      filtrarUsuariosNombre(){
        if (!this.searchTerm) {
          this.mostrarTodo();
          return;
        }
        this.arrayClases = this.arrayClases.filter((Clases: any) => {
          const nombreCompleto = `${Clases.nombre}${Clases.dias} `;
          return nombreCompleto.toLowerCase().includes(this.searchTerm.toLowerCase());
        });  
      }
      
mostrarTodo() {
  this.clasesService.getClases().subscribe((data: any) => {
      console.log('JSON data:', data);
      this.arrayClases = data.Clases;
  });

}
editarClases(clase: any) {
  // this.editando = true;
  clase.editando = true;
  this.datosEditados = { ...clase };
}


guardarCambios(clases: any) {
      

  const datosParaActualizar = {
  nombre : clases.nombre,
  dias : clases.dias,
  // dias : clases.dias
   
  };
  console.log('datosEditados', datosParaActualizar);
  console.log('clase a editar', clases);
  delete this.datosEditados.idClases;
  
  // Enviar una solicitud de actualización al servidor con this.datosEditados
  this.clasesService.updateClase(clases.idClases, datosParaActualizar).subscribe(
    (data: any) => {
      console.log('Clases actualizada', data);
      this.editando = false;
      clases.editando = false;
       // Volver al modo de visualización
      // Actualizar la interfaz de usuario o recargar datos si es necesario
    },
    (error) => {
      console.error('Error al actualizar la clase', error);
      // Manejar errores y proporcionar retroalimentación al usuario
    }
  );
}


deleteClase(idClases: string){
  this.clasesService.deleteClase(idClases).subscribe(
    (data: any) => {
      console.log('Clase Eliminada', data);
      
    },
    (error) => {
      console.error('Error al eliminar la clase', error);
    }
  );

}

}


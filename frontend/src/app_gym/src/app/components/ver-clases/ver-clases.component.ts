import { Component , OnInit} from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';
import { ClasesService } from 'src/app/services/clases.service';
import { Output, EventEmitter } from '@angular/core';
// import { NgxPaginationModule } from 'ngx-pagination';

@Component({
  selector: 'app-ver-clases',
  templateUrl: './ver-clases.component.html',
  styleUrls: ['./ver-clases.component.css']
})
export class VerClasesComponent implements OnInit{
  constructor(
    private jwtHelper: JwtHelperService,
    private clasesService: ClasesService,
  ) { }
  page = 1;
  perPage = 10;
  isLastPage: boolean = false;

  currentPage = 1;
  itemsPerPage = 10;
  totalItems = 0;
  id = '';
  idProfesor = '';

  varVerClases = true;
  mostrarFormularioCreacion = false;
  mensajeExito: string = '';
  nuevaclases = {
    nombre: '',
    dias: ''
  };
  arrayClases: any[] = [];
  extendedCardId = '';
  mostrandoProfesores = false;

  
  isToken: boolean = false;
  editando: boolean = false;
  datosEditados: any = {};
  userRol:string = '';
  dni: string = '';

  searchTerm: string = '';
  paginaActual: number = 1;
  clasesPorPagina: number = 10;
  totalClases: number = 0;
  arrayProfesoresPorClases: any;





  arrayClasesGuess=[
    {
      idClases: "1",
      nombre: "Entrenamiento Pecho",
      dias: "Lunes",
    },
    {
      idClases: "2",
      nombre: "Entrenamiento Espalda",
      dias: "Martes",
    },
    {
      idClases: "3",
      nombre: "Entrenamiento Piernas",
      dias: "Miercoles",
    }

  ]
  getClasesEnPares() {
    const clasesEnPares = [];
    for (let i = 0; i < this.arrayClases.length; i += 2) {
      const par = [this.arrayClases[i], this.arrayClases[i + 1]];
      clasesEnPares.push(par);
    }
    return clasesEnPares;
  }

  

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
    console.log('clases del notoken',this.arrayClases);
  }
  if (this.userRol=='profesor' || this.userRol=='admin' || this.userRol=='alumno'|| this.userRol=='espera')  {
  
    this.getClases();
  }

  // if(this.userRol=='espera'){
  //   this.arrayClases = this.arrayClasesGuess;
  // }
  if (this.isToken==false){
    this.arrayClases = this.arrayClasesGuess;
  }
// }

  }
  getClases() {
    this.clasesService.getClases(this.page, this.perPage).subscribe(
      (data: any) => {
        console.log('Entre al get clases', data);
        this.arrayClases = data.Clases;
        this.totalItems = data.Total;
        this.isLastPage = this.totalItems / this.perPage <= this.page;

        
      },
      (error) => {
        console.error('Error al obtener las clases', error);
      }
    );
  }

  onPageChange(pageNumber: number) {
    this.currentPage = pageNumber;
    this.getClases();
    
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
          const nombreCompleto = `${Clases.nombre}${Clases.dias}${Clases.idClases} `;
          return nombreCompleto.toLowerCase().includes(this.searchTerm.toLowerCase());
        });  
      }
      
mostrarTodo() {
  this.clasesService.getClases(this.paginaActual,this.clasesPorPagina).subscribe((data: any) => {
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

crearClase() {
  const datosParaPost = {
    nombre: this.nuevaclases.nombre,
    dias: this.nuevaclases.dias,
    
  };
  console.log('datosParaPost', datosParaPost);
  this.clasesService.postClase(datosParaPost).subscribe(
    (data: any) => {
      console.log('Nueva clase creada', data);
      this.mostrarFormularioCreacion = false;
     
      this.mensajeExito = 'La clase se ha creado con éxito';
      setTimeout(() => {
        this.mensajeExito = ''; // Restablecer el mensaje de éxito después de 5 segundos
      }, 3000); // 5000 milisegundos = 5 segundos
      

      
    },
    (error) => {
      console.error('Error al crear la clase', error);
      // Maneja errores y proporciona retroalimentación al usuario
    }
  );


  }

  getProfesoresPorClase(idClases: string) {

    const clase = this.arrayClases.find((c: any) => c.idClases === idClases);
    if (clase) {
        clase.mostrandoProfesores = true;
    }
    this.clasesService.getProfebyClase(idClases).subscribe(
      (data: any) => {
        console.log('Profesores por clase', data);
        // clase.mostrandoProfesores = true;
        // this.arrayProfesoresPorClases = Object.values(data);;
        const clase = this.arrayClases.find((c: any) => c.idClases === idClases);
        if (clase) {
          clase.profesores = Object.values(data);
          this.extendedCardId = idClases;
          
        }

        
      },
      (error) => {
        console.error('Error al obtener los profesores por clase', error);
      }
    );
  }

  ocultarProfesores(clase: any) {
    clase.mostrandoProfesores = false;
  }

  profesorAgregando(clase: any) {
    clase.agregandoProfesor = true;
  }

  guardarProfesorEnClase(clases:any){
    const datosParaActualizar = {
      idClase: clases.idClases,
      idProfesor: Number(clases.idProfesor)
    };
    console.log('datosParaActualizar', datosParaActualizar);
    this.clasesService.updateProfesorEnClase(datosParaActualizar).subscribe(
      (data: any) => {
        console.log('Profesor agregado a la clase', data);
        clases.agregandoProfesor = false;
        this.getProfesoresPorClase(clases.idClases);
      },
      (error) => {
        console.error('Error al agregar el profesor a la clase', error);
      }
    );

  }
  cancelarGuardadoProfesorEnClase(clases: any) {
    clases.agregandoProfesor = false;
  }
  onClickAnteriorPag(){
  
      this.page-=1;
      this.getClases();

    
  }
  onClickSiguientePag(){
    
    this.page+=1;
    this.getClases();
  }
  
}


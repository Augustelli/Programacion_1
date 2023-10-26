import { Component, OnInit } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';

@Component({
  selector: 'app-ver-usuarios',
  templateUrl: './ver-usuarios.component.html',
  styleUrls: ['./ver-usuarios.component.css']
})
export class VerUsuariosComponent implements OnInit {
  arrayUsuarios: any;
  searchTerm: string = '';
  userRol:string = '';
  userTodos:boolean=true;
  rolUsuarios: string = '';

  page=1;
  perPage=6;
  isLastPage: boolean = true;
  totalItems = 0;
  isEspera: boolean = false;
  isToken: boolean = false;


 
  constructor(
    private usuariosService: UsuariosService,
    private jwtHelper: JwtHelperService,
    
    private router: Router
  ){}


  filtrarAlumnos() {
    
    this.page = 1
    this.rolUsuarios='alumno'

    this.usuariosService.getAlumnos(this.page, this.perPage).subscribe((data: any) => {
        console.log('Usuarios filtrados por rol "alumno wasaaaaa":', data);
        this.arrayUsuarios = data.Usuario;
        this.userTodos=false;
        this.totalItems = data.Total;
        this.isLastPage = this.totalItems / this.perPage <= this.page;  
        this.isEspera = false;
    });
}
// filtrarAlumnosEspera(rol:string) {
//   this.usuariosService.getUsers(this.page, this.perPage).subscribe((data: any) => {
//     console.log(`Usuarios filtrados por rol "${rol}":`, data);
//     // Filtra los usuarios por el rol específico
//     this.arrayUsuarios = data.Usuario.filter((usuario: any) => {
//       this.userTodos=false;
//       this.isEspera = true;
//       return usuario.rol === rol;
//     });
// }
filtrarAlumnosEspera() {
  
  this.page = 1
  this.rolUsuarios='espera'

  this.usuariosService.getUsers1(this.page, this.perPage, this.rolUsuarios).subscribe((data: any) => {
   
    this.arrayUsuarios = data.Usuario;
      this.userTodos = false;
      this.isEspera = true;
      this.totalItems = data.Total;
      this.isLastPage = this.totalItems / this.perPage <= this.page;
    });
  

    // Cuenta la cantidad de usuarios con el rol específico

}



  editarUsuario(usuario:any){
    console.log('Usuario a editar', usuario);
    // this.router.navigate(['/usuario/'+usuario.id+'/Editar']);
  }

ngOnInit(){
  const token = localStorage.getItem('token');
  if (token){ 
    const decodedToken = this.jwtHelper.decodeToken(token);
    this.userRol = decodedToken.rol;
    this.isToken = true;
}
if (this.userRol === 'admin') {
  this.usuariosService.getUsers(this.page, this.perPage).subscribe((data:any) => {
    console.log('JSON data:', data);
    this.userTodos=true;
    this.arrayUsuarios = data.Usuario;
    this.totalItems = data.Total;
    this.isLastPage = this.totalItems / this.perPage <= this.page; 
    this.isEspera = false;   
  })
}
if (this.userRol === 'profesor') {
  this.usuariosService.getAlumnos(this.page,this.perPage).subscribe((data:any) => {
    this.userTodos=true;
    console.log('JSON data:', data);
    this.arrayUsuarios = data.Usuario
    this.totalItems = data.Total;
    this.isLastPage = this.totalItems / this.perPage <= this.page;   
    this.isEspera = false;
  });
}

}
mostrarTodo() {

  this.rolUsuarios=''
  this.page=1
  this.ngOnInit();
}
filtrarUsuariosNombre(){
  if (!this.searchTerm) {
    this.mostrarTodo();
    return;
  }
  this.arrayUsuarios = this.arrayUsuarios.filter((usuario: any) => {
    const nombreCompleto = `${usuario.nombre} ${usuario.apellido}${usuario.dni}`;
    return nombreCompleto.toLowerCase().includes(this.searchTerm.toLowerCase());
  });  
}
nuevoUsuario(){
  this.router.navigate(['/crear_usuario_admin']);

}

deleteUsuario(user_id: string) {
  this.usuariosService.deleteUser(user_id)
  .subscribe(
    (response) => {
      if (response.status === 0) {
        // El código de estado es 0, considera que la eliminación se realizó correctamente
        console.log('Eliminación exitosa (código de estado 0)');
        // Puedes realizar acciones adicionales aquí si es necesario
      } else if (response.status === 200) {
        // La eliminación se realizó correctamente, código de estado 200
        console.log('Eliminación exitosa (código de estado 200)');
        // Puedes realizar acciones adicionales aquí si es necesario
      } else {
        // Otro código de estado inesperado
        console.error('Error en la eliminación (código de estado ' + response.status + ')');
        // Puedes manejar otros códigos de estado aquí si es necesario
      }
    },
    (error) => {
      // Manejar errores aquí
      console.error('Error en la solicitud de eliminación', error);
    }
  );
}
onClickAnteriorPag(){
  this.page-=1;


  this.ngOnInit();


}
onClickSiguientePag(){
  this.page+=1;
  if (this.rolUsuarios === 'alumno'){
    this.usuariosService.getAlumnos(this.page, this.perPage).subscribe((data: any) => {
      console.log('Usuarios filtrados por rol "alumno wasaaaaa":', data);
      this.arrayUsuarios = data.Usuario;
      this.userTodos=false;
      this.totalItems = data.Total;
      this.isLastPage = this.totalItems / this.perPage <= this.page;  
      this.isEspera = false;
  });
  }
  if (this.rolUsuarios === 'espera'){
   
    this.usuariosService.getUsers1(this.page, this.perPage, this.rolUsuarios).subscribe((data: any) => {
      console.log('Usuarios filtrados por rol "alumno wasaaaaa":', data);
      this.arrayUsuarios = data.Usuario;
      this.userTodos=false;
      this.totalItems = data.Total;
      this.isLastPage = this.totalItems / this.perPage <= this.page;  
      this.isEspera = false;
  });
  }
  if (this.rolUsuarios === '') {
   
    this.ngOnInit();
  }
}

}


    


import { Component } from '@angular/core';
import { UsuariosService } from 'src/app/services/usuarios.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-ver-usuarios',
  templateUrl: './ver-usuarios.component.html',
  styleUrls: ['./ver-usuarios.component.css']
})
export class VerUsuariosComponent {
  arrayUsuarios: any;
  searchTerm: string = '';

  // arrayUsuarios = [
  //   {
  //     id: 1,
  //     nombre:' Usuario 1',
  //     imagen : "chica_fachera.svg"
  //   },
  //   {
  //     id: 2,
  //     nombre:' Usuario 2',
  //     imagen : "chico_fachero2.svg"
  //   },
  //   {
  //     id: 3,
  //     nombre:' Usuario 3',
  //     imagen : "pibe_fachero.svg"
  //   }
  // ];
  
  constructor(
    private usuariosService: UsuariosService,
    
    private router: Router
  ){}

  mostrarTodo() {
    this.usuariosService.getUsers().subscribe((data: any) => {
        console.log('JSON data:', data);
        this.arrayUsuarios = data.Usuario;
    });
}
  filtrarAlumnos() {
    this.usuariosService.getAlumnos().subscribe((data: any) => {
        console.log('Usuarios filtrados por rol "alumno":', data);
        this.arrayUsuarios = data.Usuario;
    });
}
filtrarAlumnosEspera(rol:string) {
  this.usuariosService.getUsers().subscribe((data: any) => {
    console.log(`Usuarios filtrados por rol "${rol}":`, data);
    // Filtra los usuarios por el rol específico
    this.arrayUsuarios = data.Usuario.filter((usuario: any) => {
      return usuario.rol === rol;
    });
});
}

  editarUsuario(usuario:any){
    console.log('Usuario a editar', usuario);
    // this.router.navigate(['/usuario/'+usuario.id+'/Editar']);
  }

ngOnInit(){
  this.usuariosService.getUsers().subscribe((data:any) => {
    console.log('JSON data:', data);
    this.arrayUsuarios = data.Usuario;
  })
}
nuevoUsuario(){
  this.router.navigate(['/crear_usuario_admin']);

}
filtrarUsuariosNombre(){
  if (!this.searchTerm) {
    this.mostrarTodo();
    return;
  }
  this.arrayUsuarios = this.arrayUsuarios.filter((usuario: any) => {
    const nombreCompleto = `${usuario.nombre} ${usuario.apellido}`;
    return nombreCompleto.toLowerCase().includes(this.searchTerm.toLowerCase());
  });  
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
}

    


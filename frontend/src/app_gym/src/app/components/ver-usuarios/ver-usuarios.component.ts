import { Component } from '@angular/core';

@Component({
  selector: 'app-ver-usuarios',
  templateUrl: './ver-usuarios.component.html',
  styleUrls: ['./ver-usuarios.component.css']
})
export class VerUsuariosComponent {
  arrayUsuarios = [
    {
      id: 1,
      nombre:' Usuario 1'
    },
    {
      id: 2,
      nombre:' Usuario 2'
    },
    {
      id: 3,
      nombre:' Usuario 3'
    }
  ];
  
  constructor(
    //private router: Router
  ){}

  editarUsuario(usuario:any){
    console.log('Usuario a editar', usuario);
    //this.router.navigate(['/usuario/'+usuario.id+'/Editar']);

  }

}

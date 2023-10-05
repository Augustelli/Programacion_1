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
}

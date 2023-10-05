import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sexo',
  templateUrl: './sexo.component.html',
  styleUrls: ['./sexo.component.css']
})
export class SexoComponent {

  constructor(
    private authService: AuthService,
    private router: Router,
  ) { }
  

  sexoHombre(){
    localStorage.setItem('sexo', 'Hombre');
    // llamar funcion para pushear al back
    this.registrarUsuario();
  }
  sexoMujer(){
    localStorage.setItem('sexo', 'Mujer') 
    this.registrarUsuario();
    // llamar funcion para pushear al back   
  }
  registrarUsuario() {
    // Llama a la función signup del servicio AuthService
    this.authService.signup().subscribe(
      (response) => {
        // Maneja la respuesta exitosa si es necesario
        console.log('Registro exitoso', response);
        this.clearLocalStorage();
        this.router.navigate(['/home']);

      },
      (error) => {
        // Maneja cualquier error que ocurra durante el registro
        console.error('Error durante el registro', error);
      }
    );
  }
  
  clearLocalStorage() {
    localStorage.removeItem('email');
    localStorage.removeItem('contrasegna');
    localStorage.removeItem('nombre');
    localStorage.removeItem('apellido');
    localStorage.removeItem('dni');
    localStorage.removeItem('day');
    localStorage.removeItem('dia');
    localStorage.removeItem('mes');
    localStorage.removeItem('anio');
    localStorage.removeItem('nombre_usuario');
    localStorage.removeItem('altura');
    localStorage.removeItem('peso');
    localStorage.removeItem('sexo');

    // Agrega cualquier otra variable local que desees eliminar aquí
  }
  
}

// login(dataLogin: any={}) {
//   // dataLogin = {email:'admin@example.com', contrasegna:'admin'};
//     console.log('comprobando credenciales');
//     this.authService.login(dataLogin).subscribe({
//       next: (rta:any) => {
//         alert('Login correcto');
//         console.log('Respuesta Login:',rta.access_token);
//         localStorage.setItem('token', rta.access_token);
//         this.router.navigate(['/home']);

//       }, error: (error) => {
//         alert('Login incorrecto');
//         localStorage.removeItem('token');
//       }, complete: () => {
//         console.log('Login finalizado');
//       }});
//     }


    





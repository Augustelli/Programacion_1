import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take, switchMap , tap} from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  // url='http://127.0.0.1:5002';
  url = '/api';

  constructor(
    private httpClient: HttpClient,
    private router: Router,
  ) { }

  login (dataLogin:any):Observable<any>{
    console.log('comprobando credenciales');

    // let dataLogin = {email:'admin@example.com', contrasegna:'admin'};
    return this.httpClient.post(this.url + '/auth/login',dataLogin).pipe(take(1));
  }


  signup(): Observable<any> {
    // Obtener los valores necesarios de localStorage o de donde sea que los tengas
    let dni = localStorage.getItem('dni');
    let nombre = localStorage.getItem('nombre');
    let apellido = localStorage.getItem('apellido');
    let email = localStorage.getItem('email');
    let dia = localStorage.getItem('dia');
    let mes = localStorage.getItem('mes');
    let anio = localStorage.getItem('anio');
    let nombre_usuario = localStorage.getItem('nombre_usuario');
    let contrasegna = localStorage.getItem('contrasegna');
    let altura = localStorage.getItem('altura');
    let peso = localStorage.getItem('peso');
  
    // Crear el objeto de datos que deseas enviar en la solicitud POST
    const dataSignup = {
      dni: dni,
      nombre: nombre,
      apellido: apellido,
      email: email,
      fecha_nacimiento: `${dia}-${mes}-${anio}`,
      nombre_usuario: nombre_usuario,
      contrasegna: contrasegna,
      altura: altura,
      peso: peso
    };
      
    // Realizar la solicitud POST con los datos construidos
    // return this.httpClient.post(this.url + '/auth/register', dataSignup).pipe(take(1));
    return this.httpClient.post(this.url + '/auth/register', dataSignup).pipe(
      take(1),
      switchMap(() => {
        // Después del registro exitoso, realizar el inicio de sesión
        return this.login({ email: email, contrasegna: contrasegna });
        
      })
    );
  }



  logout(){
    localStorage.removeItem('token');
    this.router.navigate(['/', 'home']);
  }
}


// this.authService.login(dataLogin).subscribe({
//   next: (rta:any) => {
//     alert('Login correcto');
//     console.log('Respuesta Login:',rta.access_token);
//     localStorage.setItem('token', rta.access_token);
//     this.router.navigate(['/home']);

//   }, error: (error) => {
//     alert('Login incorrecto');
//     localStorage.removeItem('token');
//   }, complete: () => {
//     console.log('Login finalizado');
//   }});
// }
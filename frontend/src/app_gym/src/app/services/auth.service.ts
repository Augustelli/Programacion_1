import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take, switchMap , tap} from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
 
  url = '/api';

  constructor(
    private httpClient: HttpClient,
    private router: Router,
  ) { }

  login (dataLogin:any):Observable<any>{
    console.log('comprobando credenciales');

    return this.httpClient.post(this.url + '/auth/login',dataLogin).pipe(take(1));
  }


  signup(): Observable<any> {
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
      
    
    return this.httpClient.post(this.url + '/auth/register', dataSignup).pipe(
      take(1),
      switchMap(() => {
   
        return this.login({ email: email, contrasegna: contrasegna });
        
      })
    );
  }



  logout(){
    localStorage.removeItem('token');
    this.router.navigate(['/', 'home']);
  }
}


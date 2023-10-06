import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';


@Injectable({
  providedIn: 'root'
})
export class UsuariosService {
  url = '/api';

  constructor(
    private httpClient: HttpClient,
  ) {}


// mostar todos los usuarios
  getUsers(){
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.get(this.url + '/usuarios', {headers: headers});
  }

  // mostar todos los alumnos
 
  getAlumnos() {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    // Cambia la URL a tu endpoint específico para obtener usuarios con rol "alumno"
    return this.httpClient.get(this.url + '/alumnos',{headers: headers});
}
  

}

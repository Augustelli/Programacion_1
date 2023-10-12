import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders , HttpResponse} from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';
import { catchError } from 'rxjs/operators';


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
  //mostar alumno por dni

  getUserData(user_id: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.get(this.url + '/usuario?nrDni='+user_id, {headers: headers});
  }

  //hacer put en alumno
  updateUserData(user_id: string, updatedUserData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.put(this.url + '/usuario?nrDni='+user_id, updatedUserData,{headers: headers});
  }
  //hacer delete de usuario
  deleteUser(user_id: string): Observable<any> {

    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.delete(this.url + '/usuario?nrDni=' + user_id,{headers: headers});
    
  }

  //hacer post de usuario POR QUE NO ANDAAAAAAAA
  createUser(newUserData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    console.log('Datos del nuevo usuario', newUserData);
    return this.httpClient.post(this.url + '/usuarios', {...newUserData},{headers: headers});
  }
  checkEmailExists(email: string) {
    return this.httpClient.get(this.url + '/usuarios_login?email=' + email);
  }
  checkDniExists(dni: string) {
    return this.httpClient.get(this.url + '/usuarios_login?nrDni=' + dni);
  }
}



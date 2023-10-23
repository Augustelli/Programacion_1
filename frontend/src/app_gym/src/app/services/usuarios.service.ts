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
  getUsers(pageNumber: number, pageSize: number){
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const params = {
      page: pageNumber.toString(),
      per_page: pageSize.toString()
    };
    return this.httpClient.get(this.url + '/usuarios', {headers: headers,params: params});
  }

  // mostar todos los alumnos
 
  getAlumnos(pageNumber: number, pageSize: number) {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const params = {
      page: pageNumber.toString(),
      per_page: pageSize.toString()
    };

    // Cambia la URL a tu endpoint específico para obtener usuarios con rol "alumno"
    return this.httpClient.get(this.url + '/alumnos',{headers: headers, params: params});
}
getAlumnos1(pageNumber: number, pageSize: number, state: any) {
  let auth_token = localStorage.getItem('token');
  const headers = new HttpHeaders({
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${auth_token}`
  });
  const params = {
    page: pageNumber.toString(),
    per_page: pageSize.toString(),
    estado: state.toString()
  };

  // Cambia la URL a tu endpoint específico para obtener usuarios con rol "alumno"
  return this.httpClient.get(this.url + '/alumnos',{headers: headers, params: params});
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
  getUserDataAlumno(user_id: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.get(this.url + '/alumno?nrDni='+user_id, {headers: headers});
  }

  getUserDataProfesor(user_id:string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.get(this.url + '/profesor?nrDni='+user_id, {headers: headers});
  }


  //hacer put en alumno
  updateUserData(user_id: string, updatedUserData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    console.log('Datos del usuario actualizado', updatedUserData);
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

  updateUserDataAlumno(user_id: string, updatedUserData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.put(this.url + '/alumno?nrDni='+user_id, updatedUserData,{headers: headers});
  }
  updateUserDataProfesor(user_id: string, updatedUserData: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.put(this.url + '/profesor?nrDni='+user_id, updatedUserData,{headers: headers});
  }
  getProfes1(pageNumber: number, pageSize: number){
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({ 
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`

    });
    const params = {
      page: pageNumber.toString(),
      per_page: pageSize.toString()
    };
    return this.httpClient.get(this.url + '/profesor',{headers: headers, params: params});
  }
  deleteProfesor(user_id: string): Observable<any> {
      
      let auth_token = localStorage.getItem('token');
      const headers = new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${auth_token}`
  
      });
      return this.httpClient.delete(this.url + '/profesor?idProfesor=' + user_id,{headers: headers});
      
    }
}




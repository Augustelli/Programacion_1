import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PlanificacionService {
  url = '/api';

  constructor(
    private httpClient: HttpClient
    ) {}

  getPlanificaciones(): Observable<any[]> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.get<any[]>(`${this.url}/planificaciones_profesores`, {headers: headers});
  }
}
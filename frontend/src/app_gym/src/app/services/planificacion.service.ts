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

  getPlanificaciones(): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.get(this.url +'/planificaciones_profesores', {headers: headers});
  }
  deletePlanificacion(planificacion_id: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.delete(this.url +'/planificacion_profesor?nrIdPlanificacion='+planificacion_id, {headers: headers});
  }
  getPlanificacionAlumno(alumno_dni: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return this.httpClient.get(this.url +'/planificacion_profesor?nrDni='+alumno_dni, {headers: headers});
  }

  actualizarPlanificacion(planificacion_id: string, planificacion: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.put(this.url +'/planificacion_profesor?nrIdPlanificacion='+planificacion_id, planificacion, {headers: headers});
  }
  crearPlanificacion(planificacion: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.post(this.url +'/planificacion_profesor', planificacion, {headers: headers});
  }
}
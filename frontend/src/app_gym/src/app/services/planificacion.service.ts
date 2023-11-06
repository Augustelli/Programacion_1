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

  getPlanificaciones(pageNumber: number, pageSize: number): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const params = {
          page: pageNumber.toString(),
          per_page: pageSize.toString()
        };
    return this.httpClient.get(this.url +'/planificaciones_profesores', {headers: headers,params: params});
  }
  getPlanificaciones1(): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
  
    return this.httpClient.get(this.url +'/planificaciones_profesores', {headers: headers});
  }


  // getClases(pageNumber: number, pageSize: number): Observable<any> {
  //   let auth_token = localStorage.getItem('token');
  //   const headers = new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     'Authorization': `Bearer ${auth_token}`
  //   });
  //   const params = {
  //     page: pageNumber.toString(),
  //     per_page: pageSize.toString()
  //   };
  //   return this.httpClient.get(this.url +'/clases', {headers: headers, params: params});
 
  // }

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
    console.log(planificacion);

    return this.httpClient.post(this.url +'/planificaciones_profesores', planificacion, {headers: headers});
  }
  
  crearPlanificacionDetalle(planificacion_detalle: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`,
    });
    console.log(planificacion_detalle);

    return this.httpClient.post(this.url + '/planificaciones_detalle', planificacion_detalle, { headers: headers });
  }
  getPlanificacionDetalle(planificacion_id: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });
    console.log(planificacion_id);
    return this.httpClient.get(this.url + '/planificacion_detalle?idPlanificacion=' +planificacion_id, { headers: headers });
  }

  getPlanificacionesDetalle(): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });
    return this.httpClient.get(this.url + '/planificaciones_detalle', { headers: headers });
  }
  deletePlanificacionDetalle(planificacion_detalle_id: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });
    return this.httpClient.delete(this.url + '/planificacion_detalle?idPlanificacionDetalle=' + planificacion_detalle_id, { headers: headers });
  }

  putPlanificacionDetalle(planificacion_detalle_id: any, planificacion_detalle: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `Bearer ${auth_token}`,
    });
    return this.httpClient.put(this.url + '/planificacion_detalle?idPlanificacionDetalle=' + planificacion_detalle_id, planificacion_detalle, { headers: headers });
  }



}
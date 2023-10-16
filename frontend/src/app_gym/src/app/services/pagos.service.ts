import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PagosService {

  constructor(
    private httpClient: HttpClient
  ) { }
  url = '/api';

  realizarPago(pago: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.post(this.url +'/pagos', pago, {headers: headers});
  }

  getPagosByDni(dni: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.get(this.url +'/pagos?nrDni='+dni, {headers: headers});
  }

  crearPago(pago: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.post(this.url +'/pagos', pago, {headers: headers});
  }

  deletePago(id: number): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.delete(this.url +'/pago?idPago='+id, {headers: headers});
  }
  putPago(idPago:any ,pago: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.put(this.url +'/pagos?idPago='+idPago, pago, {headers: headers});
  }






}

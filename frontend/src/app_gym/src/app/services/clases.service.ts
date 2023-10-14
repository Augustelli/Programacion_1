import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ClasesService {

  constructor(
    private httpClient: HttpClient
  ) { }
  url = '/api';

  getClases(pageNumber: number, pageSize: number): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const params = {
      page: pageNumber.toString(),
      per_page: pageSize.toString()
    };
    return this.httpClient.get(this.url +'/clases', {headers: headers, params: params});
  }

  updateClase(idClases: string, clase: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    console.log(clase);

    return this.httpClient.put(this.url +'/clases?idClases='+idClases, clase, {headers: headers});
  }
  deleteClase(idClases: string): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.delete(this.url +'/clases?idClases='+idClases, {headers: headers});
  }

  postClase(clase: any): Observable<any> {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });

    return this.httpClient.post(this.url +'/clases', clase, {headers: headers});
  }

  

  
}
